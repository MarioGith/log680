# Explication du choix de la suite de tests
La suite de test que nous utilisons pour tester notre API est **Pytest**.
Nous choisissons Pytest pour sa popularité et la facilité à écrire des tests.
Pour lancer un test, clique droit sur le fichier de test et clique ```Run Test 'Python tests in tests```.
I faut que le token dans la variable d'environnement PyCharm soit valide.


# Exemple de nos tests
## Pour tester le lead time (Unit-test)
```
    import os
    from unittest import TestCase, mock
    from metrics.kanban import IssueLeadTime
    
    class TestIssueLeadTime(TestCase):
        def setUp(self):
            # Seting the TOKEN
            self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}
    
        # After each unit_testing do the following
        def tearDown(self):
            pass
        def test_run_query_success(self):
            # Issue with a valid number of the TEST
            issue_no = 1
    
            # Calling Method
            result = IssueLeadTime.get_lead_time_of_issue(issue_no)
    
            # Assert data
            self.assertEqual(result['lead_time'], 288228.0)
            self.assertIsNotNone(result['issue_info'])
        def test_run_query_none(self):
            # Issue with an invalid number for testing
            issue_no = -999
    
            # Calling the method
            result = IssueLeadTime.get_lead_time_of_issue(issue_no)
    
            # Assert
            self.assertIsNone(result)
        def test_run_query_failure(self):
            # Issue with a valid number for testing
            issue_no = 1
    
            # Mocking
            with mock.patch('requests.post') as mock_test:
                mock_test.return_value.status_code = 500
    
                # Calling the method
                with self.assertRaises(Exception):
                    IssueLeadTime.get_lead_time_of_issue(issue_no)
    
                # Assert
                mock_test.assert_called_once_with(
                    'https://api.github.com/graphql',
                    json={'query': mock.ANY, 'variables': {'issue_no': issue_no}},
                    headers=self.headers
                )
```

## Pour tester le lead time (Integration-testing)
```
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

```