import os
from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from api.controllers.isues_actives_by_column_controller import IssuesActiveByColumnController


class TestIssuesActiveByColumnController(TestCase):

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

    @patch('metrics.kanban.IssuesActiveByColumn.get_number_of_active_issues_by_column')
    def test_get_with_valid_parameter(self, mock_get_number_of_active_issues_by_column):
        # Issue with a valid number of the TEST
        column_name = "Backlog"
        total_items = 8
        total_tasks = 2
        total_closed_tasks = 2
        total_active_tasks = 2
        pr_list = [
            {'id': '1', 'number': 1, 'title': 'Issue 1', 'description': 'Description 1',
             'createdAt': '2023-05-10', 'closedAt': '2023-05-20'},
            {'id': '2', 'number': 2, 'title': 'Issue 2', 'description': 'Description 2',
             'createdAt': '2023-05-10', 'closedAt': '2022-05-20'}
        ]

        # Mocking return value
        mock_get_number_of_active_issues_by_column.return_value = (column_name, total_closed_tasks,
                                                                   total_items, total_tasks,
                                                                   total_active_tasks, pr_list)

        # Sending a GET request to the API
        response = self.client.get(f'/IssuesActiveByColumn?columnname=Backlog',
                                   headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(data, {'issues_actives': [column_name, total_closed_tasks,
                                                       total_items, total_tasks, total_active_tasks,
                                                       pr_list]})

    @patch('metrics.kanban.IssuesActiveByColumn.get_number_of_active_issues_by_column')
    def test_get_with_invalid_parameter(self, mock_get_number_of_active_issues_by_column):
        # Mocking return value
        mock_get_number_of_active_issues_by_column.side_effect = ValueError('Failed try')

        # Sending a GET request to the API
        response = self.client.get(f'/IssuesActiveByColumn?columnname=Backlog',
                                   headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Failed try'})

    @patch('metrics.kanban.IssuesActiveByColumn.get_number_of_active_issues_by_column')
    def test_get_with_missing_parameter(self, mock_get_issue_lead_time_within_period):
        # Mocking return value
        mock_get_issue_lead_time_within_period.return_value = {'error': 'Missing parameters'}

        # Sending a GET request to the API
        response = self.client.get(f'/IssuesActiveByColumn?columnname=', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Invalid parameter'})
