import os
from unittest import TestCase
from unittest.mock import patch

from flask import Flask
from flask_restful import Api, fields

from api.controllers.issue_lead_time_controller import IssueLeadTimeController


class TestIssueLeadTimeIntegration(TestCase):

    # Before each unit_testing do the following
    def setUp(self):
        # Creating the API for unit_testing
        self.app = Flask(__name__)
        self.api = Api(self.app)

        # Disable error catching
        self.app.testing = True

        # Adding ressource
        self.api.add_resource(IssueLeadTimeController, '/IssueLeadTime/<int:issue_no>')

        # Starting the client
        self.client = self.app.test_client()

        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # After each unit_testing do the following
    def tearDown(self):
        pass

    def test_get_lead_time_valid_issue(self):
        # Issue with a valid number of the TEST
        issue_no = 1

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTime/{issue_no}', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data)

    def test_get_lead_time_invalid_issue(self):
        # Issue with a invalid number of the TEST
        issue_no = 999

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTime/{issue_no}', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Issue is None')

    def test_get_invalid_parameters(self):
        # Issue with a value error
        issue_no = 999

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTime/{issue_no}', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], 'Issue is None')

    def test_get_invalid_type_parameters(self):
        # Issue with a value error
        issue_no = "abc"

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTime/{issue_no}', headers=self.headers)

        # Assert the response status code
        self.assertEqual(response.status_code, 404)
