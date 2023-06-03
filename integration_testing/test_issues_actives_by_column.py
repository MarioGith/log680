import os
from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from api.controllers.isues_actives_by_column_controller import IssuesActiveByColumnController


class TestIssuesActiveByColumnIntegration(TestCase):

    # Before each unit_testing do the following
    def setUp(self):
        # Creating the API for unit_testing
        self.app = Flask(__name__)
        self.api = Api(self.app)

        # Disable error catching
        self.app.testing = True

        # Adding ressource
        self.api.add_resource(IssuesActiveByColumnController, '/IssuesActiveByColumn')

        # Starting the client
        self.client = self.app.test_client()

        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # After each unit_testing do the following
    def tearDown(self):
        pass

    def test_get_with_valid_parameter(self):

        # Sending a GET request to the API
        response = self.client.get(f'/IssuesActiveByColumn?columnname=Backlog',
                                   headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data)

    def test_get_with_invalid_parameter(self):
        # Sending a GET request to the API
        response = self.client.get(f'/IssuesActiveByColumn?columnname=123',
                                   headers=self.headers)
        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Invalid parameter'})

    def test_get_with_missing_parameter(self):
        # Sending a GET request to the API
        response = self.client.get(f'/IssuesActiveByColumn?columnname=', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Invalid parameter'})
