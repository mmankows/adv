from typing import List, Generator, TYPE_CHECKING

import petl

from django.db import models
from django.utils.timezone import now

if TYPE_CHECKING:
    from petl.transform.basics import RowSliceView


class FetchedDataset(models.Model):
    """Tracks downloaded dataset file."""
    download_path = models.CharField(max_length=1024)
    fetched_timestamp = models.DateTimeField(default=now)

    def get_contents(self, limit: int, offset: int = 0) -> "RowSliceView":
        """List dataset contents, supports slicing."""
        contents = petl.fromcsv(self.download_path)
        return petl.rowslice(contents, offset, offset + limit)

    def get_grouped_count(self, column_names: List[str], limit: int, offset: int = 0) -> "RowSliceView":
        """Get count of results grouped by column names."""
        return (
            self.get_contents(limit, offset)
                .cut(*column_names)
                .aggregate(key=column_names, aggregation=len)
        )
