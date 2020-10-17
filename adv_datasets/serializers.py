from rest_framework import serializers

from adv_datasets.models import FetchedDataset


class FetchedDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FetchedDataset
        fields = serializers.ALL_FIELDS
