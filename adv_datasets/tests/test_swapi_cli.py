from unittest import mock

from django.test import TestCase

from adv_datasets.swapi_cli import SwapiCli


# TODO: Add more tests
class TestSwapiCli(TestCase):
    PEOPLE_RESP = {
        "count": 82,
        "next": "http://swapi:8000/api/people/?page=2",
        "previous": None,
        "results": [
            {
                "name": "Luke Skywalker",
                "height": "172",
                "mass": "77",
                "hair_color": "blond",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": "19BBY",
                "gender": "male",
                "homeworld": "http://swapi:8000/api/planets/1/",
                "films": ["http://swapi:8000/api/films/1/", "http://swapi:8000/api/films/2/"],
                "species": [],
                "vehicles": ["http://swapi:8000/api/vehicles/14/"],
                "starships": ["http://swapi:8000/api/starships/12/"],
                "created": "2014-12-09T13:50:51.644000Z",
                "edited": "2014-12-20T21:17:56.891000Z",
                "url": "http://swapi:8000/api/people/1/"
            },
            {
                "name": "C-3PO",
                "height": "167",
                "mass": "75",
                "hair_color": "n/a",
                "skin_color": "gold",
                "eye_color": "yellow",
                "birth_year": "112BBY",
                "gender": "n/a",
                "homeworld": "http://swapi:8000/api/planets/1/",
                "films": ["http://swapi:8000/api/films/1/", "http://swapi:8000/api/films/2/"],
                "vehicles": [],
                "starships": [],
                "created": "2014-12-10T15:10:51.357000Z",
                "edited": "2014-12-20T21:17:50.309000Z",
                "url": "http://swapi:8000/api/people/2/"
            },
        ]
    }

    @mock.patch('adv_datasets.swapi_cli.SwapiCli._get')
    def test_get_all_people__two_pages(self, mock_get):
        page1 = self.PEOPLE_RESP
        page2 = self.PEOPLE_RESP.copy()
        page2['next'] = None
        mock_get.side_effect = [page1, page2]
        c = SwapiCli()
        all_results = list(c.get_all_people())
        self.assertEqual(len(all_results), 4)
