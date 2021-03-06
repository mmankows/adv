from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from adv_datasets.fetchers import SwapiCsvFetcher
from adv_datasets.models import FetchedDataset
from adv_datasets.serializers import FetchedDatasetSerializer


class FetchedDatasetViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = FetchedDataset.objects.order_by('-id')
    serializer_class = FetchedDatasetSerializer
    DATASET_PAGE_LIMIT = 10
    GROUPBY_LIMIT = 1000
    PARAM_OFFSET = 'offset'
    PARAM_COLOMUNS = 'cols'

    @action(detail=False, methods=['post'])
    def fetch(self, request, *args, **kwargs):
        """Overrides default create, performs fetching."""
        new_dataset = SwapiCsvFetcher().fetch_characters_dataset()
        serializer = self.get_serializer(instance=new_dataset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def contents(self, request, *args, **kwargs):
        """Overrides default create, performs fetching."""
        # TODO - improve get params parsing and validation
        try:
            offset = int(request.GET.get(self.PARAM_OFFSET, 0))
            assert offset >= 0
        except (ValueError, AssertionError):
            raise ParseError("Offset param must be integer")

        dataset = self.get_object()
        data = dataset.get_contents(self.DATASET_PAGE_LIMIT, offset)
        return Response(list(data.dicts()), status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def groupby_count(self, request, pk, *args, **kwargs):
        """Returns count for rows grouped by sumset of columns."""
        # TODO - improve get params parsing and validation
        try:
            column_names = request.GET[self.PARAM_COLOMUNS]
            column_names = [c.strip() for c in column_names.split(',')]
        except (KeyError, ValueError):
            raise ParseError("Comma separated column name list required.")

        dataset = self.get_object()
        data = dataset.get_grouped_count(column_names, self.GROUPBY_LIMIT)
        return Response(list(data.dicts()), status=status.HTTP_200_OK)
