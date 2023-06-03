import os
from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from api.controllers.pr_lines_code_controller import PRLinesCodeController

class TestPRLinesCodeController(TestCase):

    # Before each unit_testing do the following
    def setUp(self):
        # Creating the API for unit_testing
        self.app = Flask(__name__)
        self.api = Api(self.app)

        # Disable error catching
        self.app.testing = True

        # Adding ressource
        self.api.add_resource(PRLinesCodeController, '/PRLinesCode')

        # Starting the client
        self.client = self.app.test_client()

        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # After each unit_testing do the following
    def tearDown(self):
        pass

    @patch('metrics.pullrequests.PRLinesCode.get_pr_lines_code_in_period')
    def test_get_with_valid_parameter(self, mock_get_pr_lines_code_in_period):
        # Issue with a valid number of the TEST
        total_additions=2
        total_count=2
        avg_additions_per_pr=2
        start_date='2023-05-10'
        end_date='2023-05-20'

        pr_list = [
            {'id': '1', 'number': 1, 'title': 'Issue 1', 'description': 'Description 1',
             'createdAt': '2023-05-10', 'closedAt': '2023-05-20'},
            {'id': '2', 'number': 2, 'title': 'Issue 2', 'description': 'Description 2',
             'createdAt': '2023-05-10', 'closedAt': '2022-05-20'}
        ]


        # Mocking return value
        mock_get_pr_lines_code_in_period.return_value = (total_additions,total_count,avg_additions_per_pr,start_date,end_date, pr_list)

        # Sending a GET request to the API
        response = self.client.get(f'/PRLinesCode?startdate=2023-05-10&enddate=2023-05-20', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(data, {'pr_lines_code': [total_additions,total_count,avg_additions_per_pr,start_date,end_date, pr_list]})

    @patch('metrics.pullrequests.PRLinesCode.get_pr_lines_code_in_period')
    def test_get_with_invalid_parameter(self, mock_get_pr_lines_code_in_period):

        # Mocking return value
        mock_get_pr_lines_code_in_period.side_effect = ValueError('Invalid date parameters')

        # Sending a GET request to the API
        response = self.client.get(f'/PRLinesCode?startdate=2023-05-10&enddate=2023-05-20', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Invalid date parameters'})

    @patch('metrics.pullrequests.PRLinesCode.get_pr_lines_code_in_period')
    def test_get_with_invalid_date_format(self, mock_get_pr_lines_code_in_period):

        # Mocking return value
        mock_get_pr_lines_code_in_period.return_value = {'error': 'Invalid date format'}

        # Sending a GET request to the API
        response = self.client.get(f'/PRLinesCode?startdate=10-05-2023&enddate=20-05-2023    ', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Invalid date format'})

    @patch('metrics.pullrequests.PRLinesCode.get_pr_lines_code_in_period')
    def test_get_with_missing_parameter(self, mock_get_pr_lines_code_in_period):

        # Mocking return value
        mock_get_pr_lines_code_in_period.return_value = {'error': 'Missing parameters'}

        # Sending a GET request to the API
        response = self.client.get(f'/PRLinesCode?startdate=&enddate=    ', headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Missing parameters'})



