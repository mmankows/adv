from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from adv_datasets.serializers import FetchedDatasetSerializer


class FetchedDatasetViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
#    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = FetchedDatasetSerializer

    @action(detail=False, methods=['post'])
    def fetch(self, request):
        email = request.data['email']
        password = request.data['password']
        try:
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
            assert user
        except (User.DoesNotExist, AssertionError):
            raise ParseError('Login failed.')

        login(request, user)
