import os
from datetime import datetime
from unittest import TestCase, mock
from metrics.kanban import IssuesActiveByColumn

class TestIssuesActiveByColumn(TestCase):
    def setUp(self):
        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # After each unit_testing do the following
    def tearDown(self):
        pass
    def test_run_query_success(self):
        column_name = "Backlog"

        # Calling Method
        result = IssuesActiveByColumn.get_number_of_active_issues_by_column(column_name)
        # Assert data
        self.assertEqual(result['column_name'], column_name)
        self.assertIsNotNone(result['issue_list'])

    def test_run_query_none(self):
        column_name = None

        # Calling the method
        result = IssuesActiveByColumn.get_number_of_active_issues_by_column(column_name)

        # Assert
        self.assertIsNone(result)
    def test_run_query_failure(self):
        column_name = "Backlog"
        # Mocking
        with mock.patch('requests.post') as mock_test:
            mock_test.return_value.status_code = 500

            # Calling the method
            with self.assertRaises(Exception) as context:
                IssuesActiveByColumn.get_number_of_active_issues_by_column(column_name)

            data = mock_test.call_args[1]['json']
            query = data['query']

            # Assert
            self.assertEqual(str(context.exception), "Query failed to run by returning code of 500. {}".format(query))

            mock_test.assert_called_once_with(
                'https://api.github.com/graphql',
                json={'query': mock.ANY, 'variables': mock.ANY},
                headers=self.headers
            )
