import os
from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from api.controllers.pr_avg_lead_time_controller import PRAvgLeadTimeControler


class TestPRAvgLeadTimeControler(TestCase):

    # Before each unit_testing do the following
    def setUp(self):
        # Creating the API for unit_testing
        self.app = Flask(__name__)
        self.api = Api(self.app)

        # Disable error catching
        self.app.testing = True

        # Adding ressource
        self.api.add_resource(PRAvgLeadTimeControler, '/PRAvgLeadTime')

        # Starting the client
        self.client = self.app.test_client()

        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # After each unit_testing do the following
    def tearDown(self):
        pass

    @patch('metrics.pullrequests.PRAvgLeadTime.get_average_lead_time')
    def test_get_with_valid_pr(self, mock_get_average_lead_time):
        # Issue with a valid number of the TEST
        avg_lead_time = 2
        pr_list = [
            {'id': '1', 'number': 1, 'title': 'Issue 1', 'description': 'Description 1',
             'createdAt': '2023-05-10', 'closedAt': '2023-05-20'},
            {'id': '2', 'number': 2, 'title': 'Issue 2', 'description': 'Description 2',
             'createdAt': '2023-05-10', 'closedAt': '2022-05-20'}
        ]

        # Mocking return value
        mock_get_average_lead_time.return_value = (avg_lead_time,pr_list)

        # Sending a GET request to the API
        response = self.client.get(f'/PRAvgLeadTime',
                                   headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(data, {'pr_avg_lead_time': [avg_lead_time,pr_list]})

    @patch('metrics.pullrequests.PRAvgLeadTime.get_average_lead_time')
    def test_get_with_invalid_pr(self, mock_get_average_lead_time):
        # Mocking return value
        mock_get_average_lead_time.side_effect = ValueError('Could not fetch from server')

        # Sending a GET request to the API
        response = self.client.get(f'/PRAvgLeadTime',
                                   headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(data, {'error': 'Could not fetch from server'})

