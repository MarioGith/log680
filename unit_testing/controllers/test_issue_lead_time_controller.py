import os
from unittest import TestCase
from unittest.mock import patch

from flask import Flask
from flask_restful import Api, fields

from api.controllers.issue_lead_time_controller import IssueLeadTimeController


class TestIssueLeadTimeController(TestCase):

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

    @patch('metrics.kanban.IssueLeadTime.get_lead_time_of_issue')
    def test_get_lead_time_valid_issue(self, mock_get_lead_time_of_issue):
        # Issue with a valid number of the TEST
        issue_no = 1

        # Mocking return value
        mock_get_lead_time_of_issue.return_value = 1

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTime/{issue_no}', headers=self.headers)

        # Testing endpoint parameter
        mock_get_lead_time_of_issue.assert_called_once_with(issue_no)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['issue_lead_time'], issue_no)


    @patch('metrics.kanban.IssueLeadTime.get_lead_time_of_issue')
    def test_get_lead_time_invalid_issue(self, mock_get_lead_time_of_issue):
        # Issue with a invalid number of the TEST
        issue_no = 999

        # Mocking return value
        mock_get_lead_time_of_issue.return_value = None

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTime/{issue_no}', headers=self.headers)

        # Testing endpoint parameter
        mock_get_lead_time_of_issue.assert_called_once_with(issue_no)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Issue is None')

    @patch('metrics.kanban.IssueLeadTime.get_lead_time_of_issue')
    def test_get_invalid_parameters(self, mock_get_lead_time_of_issue):
        # Issue with a value error
        issue_no = 999

        # Mocking return value
        mock_get_lead_time_of_issue.side_effect = ValueError('Invalid date parameter')

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTime/{issue_no}', headers=self.headers)
        # Testing endpoint parameter
        mock_get_lead_time_of_issue.assert_called_once_with(issue_no)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], 'Invalid  parameter')

    @patch('metrics.kanban.IssueLeadTime.get_lead_time_of_issue')
    def test_get_invalid_type_parameters(self, mock_get_lead_time_of_issue):
        # Issue with a value error
        issue_no = "abc"

        # Mocking return value
        mock_get_lead_time_of_issue.side_effect = ValueError('Invalid date parameter')

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTime/{issue_no}', headers=self.headers)
        # Testing endpoint parameter
        mock_get_lead_time_of_issue.assert_not_called()

        # Assert the response status code
        self.assertEqual(response.status_code, 404)
