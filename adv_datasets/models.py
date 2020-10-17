from django.db import models
from django.utils.timezone import now


class FetchedDataset(models.Model):
    """Tracks downloaded dataset file."""
    download_path = models.CharField(max_length=1024)
    fetched_timestamp = models.DateTimeField(default=now)