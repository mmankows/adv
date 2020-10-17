import logging
from typing import Generator, Optional
from urllib.parse import urljoin

import requests
from django.conf import settings


logger = logging.getLogger()


class SwapiCli:
    """Wrapper for interacting with Star Wars API."""
    RESOURCE_PEOPLE = 'api/people'
    RESOURCE_PLANETS = 'api/planets'

    # TODO: Better exception handling
    class SomethingWentWrong(Exception):
        """Very generic exception."""

    def __init__(self, base_url: str = None) -> None:
        self.base_url = base_url or settings.SWAPI_BASE_URL

    def get_all_characters(self) -> Generator:
        return self._get_all(self.RESOURCE_PEOPLE)

    def get_all_planets(self) -> Generator:
        return self._get_all(self.RESOURCE_PLANETS)

    def _get(self, path: str, **params: dict) -> dict:
        """Generic requests, returns json"""
        try:
            resp = requests.get(
                url=urljoin(self.base_url, path),
                params=params
            )
            print(resp.content)
            return resp.json()
        except:
            # TODO: Better error logging
            logger.exception("Poor error handling")
            raise self.SomethingWentWrong

    def _get_all(self, resource_path: str) -> Generator:
        """Fetch all entities by iterating throug paginated API response."""
        page_num = 0
        while True:
            params = {'page': page_num} if page_num else {}
            resp_data = self._get(resource_path, **params)
            results = resp_data['results']
            for res in results:
                yield res

            if resp_data['next'] is None:
                break

            page_num += 1
