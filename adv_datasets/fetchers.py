import os
import csv
from uuid import uuid4

from django.conf import settings
from django.utils.functional import cached_property

from adv_datasets.models import FetchedDataset
from adv_datasets.swapi_cli import SwapiCli


# TODO: Make it async, celery?
class SwapiCsvFetcher:
    CHARACTER_FIELDS = [
        'name',
        'height',
        'mass',
        'hair_color',
        'skin_color',
        'eye_color',
        'birth_year',
        'gender',
        'homeworld',
        'date',
    ]

    def __init__(self):
        self.cli = SwapiCli()

    @cached_property
    def planets_mapping(self) -> dict:
        """Planets mapping is pre-loaded and cached."""
        return {p['url']: p for p in self.cli.get_all_planets()}

    def transform_character_data(self, data: dict) -> dict:
        """Map person data to csv row."""
        # Rewrite all relevant fields if exist
        out_data = {f_name: data.get(f_name, '') for f_name in self.CHARACTER_FIELDS}

        # `homeworld`: map url to homeworld name
        out_data['homeworld'] = self.planets_mapping[data['homeworld']]['name']
        # `date`: re-format `edited` timestamp into `YYYY-MM-DD`
        out_data['date'] = data['edited'][:10]

        return out_data

    def fetch_characters_dataset(self) -> FetchedDataset:
        """Fetch all characters dataset into csv file, returns datased object meta."""

        # Prepare file and location
        path = os.path.join(settings.DATASETS_DIR, str(uuid4()))
        with open(path, 'w') as dataset_file:
            csv_writer = csv.DictWriter(dataset_file, fieldnames=self.CHARACTER_FIELDS)
            csv_writer.writeheader()

            # Save rows
            for char_data in self.cli.get_all_characters():
                csv_writer.writerow(self.transform_character_data(char_data))

        return FetchedDataset.objects.create(download_path=path)
