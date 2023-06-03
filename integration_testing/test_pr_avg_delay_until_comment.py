import os
from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from flask_restful import Api
from api.controllers.pr_avg_delay_until_comment_controller import PRAvgDelayUntilCommentController


class TestPRAvgDelayUntilCommentIntegration(TestCase):

    # Before each unit_testing do the following
    def setUp(self):
        # Creating the API for unit_testing
        self.app = Flask(__name__)
        self.api = Api(self.app)

        # Disable error catching
        self.app.testing = True

        # Adding ressource
        self.api.add_resource(PRAvgDelayUntilCommentController, '/PRAvgDelayUntilComment')

        # Starting the client
        self.client = self.app.test_client()

        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # After each unit_testing do the following
    def tearDown(self):
        pass

    def test_get_with_valid_pr(self):
        # Sending a GET request to the API
        response = self.client.get(f'/PRAvgDelayUntilComment',
                                   headers=self.headers)

        # Data from response
        data = response.json

        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data)
