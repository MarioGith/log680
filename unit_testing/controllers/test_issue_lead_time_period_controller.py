import os
from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from api.controllers.issue_lead_time_period_controller import IssueLeadTimePeriodController

class TestIssueLeadTimePeriodController(TestCase):

    # Before each unit_testing do the following
    def setUp(self):
        # Creating the API for unit_testing
        self.app = Flask(__name__)
        self.api = Api(self.app)

        # Disable error catching
        self.app.testing = True

        # Adding ressource
        self.api.add_resource(IssueLeadTimePeriodController, '/IssueLeadTimePeriod')

        # Starting the client
        self.client = self.app.test_client()

        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # After each unit_testing do the following
    def tearDown(self):
        pass

    @patch('metrics.kanban.IssueLeadTimePeriod.get_issue_lead_time_within_period')
    def test_get_with_valid_parameter(self, mock_get_issue_lead_time_within_period):
        # Issue with a valid number of the TEST
        lead_time = '10'
        pr_list = [
            {'id': '1', 'number': 1, 'title': 'Issue 1', 'description': 'Description 1',
             'createdAt': '2023-05-10', 'closedAt': '2023-05-20'},
            {'id': '2', 'number': 2, 'title': 'Issue 2', 'description': 'Description 2',
             'createdAt': '2023-05-10', 'closedAt': '2022-05-20'}
        ]


        # Mocking return value
        mock_get_issue_lead_time_within_period.return_value = (lead_time, pr_list)

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTimePeriod?startdate=2023-05-10&enddate=2023-05-20', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(data, {'issue_lead_time_period': [lead_time, pr_list]})

    @patch('metrics.kanban.IssueLeadTimePeriod.get_issue_lead_time_within_period')
    def test_get_with_invalid_parameter(self, mock_get_issue_lead_time_within_period):

        # Mocking return value
        mock_get_issue_lead_time_within_period.side_effect = ValueError('Invalid date parameters')

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTimePeriod?startdate=2023-05-10&enddate=2023-05-20', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Invalid date parameters'})

    @patch('metrics.kanban.IssueLeadTimePeriod.get_issue_lead_time_within_period')
    def test_get_with_invalid_date_format(self, mock_get_issue_lead_time_within_period):

        # Mocking return value
        mock_get_issue_lead_time_within_period.return_value = {'error': 'Invalid date format'}

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTimePeriod?startdate=10-05-2023&enddate=20-05-2023    ', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Invalid date format'})

    @patch('metrics.kanban.IssueLeadTimePeriod.get_issue_lead_time_within_period')
    def test_get_with_missing_parameter(self, mock_get_issue_lead_time_within_period):

        # Mocking return value
        mock_get_issue_lead_time_within_period.return_value = {'error': 'Missing parameters'}

        # Sending a GET request to the API
        response = self.client.get(f'/IssueLeadTimePeriod?startdate=&enddate=    ', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Missing parameters'})



