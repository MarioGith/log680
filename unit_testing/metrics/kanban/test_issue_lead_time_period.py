import os
from datetime import datetime
from unittest import TestCase, mock
from metrics.kanban import IssueLeadTimePeriod

class TestIssueLeadTimePeriod(TestCase):
    def setUp(self):
        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # After each unit_testing do the following
    def tearDown(self):
        pass
    def test_run_query_success(self):
        startdate = datetime(year=2023, month=5, day=10)
        enddate = datetime(year=2023, month=5, day=20)

        # Calling Method
        result = IssueLeadTimePeriod.get_issue_lead_time_within_period(startdate,enddate)
        # Assert data
        self.assertEqual(result['start_date'], "2023-05-10T00:00:00")
        self.assertEqual(result['end_date'], "2023-05-20T00:00:00")
        self.assertIsNotNone(result['issue_list'])

    def test_run_query_none(self):
        startdate = None
        enddate = None

        # Calling the method
        result = IssueLeadTimePeriod.get_issue_lead_time_within_period(startdate,enddate)

        # Assert
        self.assertIsNone(result)
    def test_run_query_failure(self):
        startdate = datetime(year=2023, month=5, day=10)
        enddate = datetime(year=2023, month=5, day=20)
        # Mocking
        with mock.patch('requests.post') as mock_test:
            mock_test.return_value.status_code = 500

            # Calling the method
            with self.assertRaises(Exception) as context:
                IssueLeadTimePeriod.get_issue_lead_time_within_period(startdate,enddate)

            data = mock_test.call_args[1]['json']
            query = data['query']

            # Assert
            self.assertEqual(str(context.exception), "Query failed to run by returning code of 500. {}".format(query))

            mock_test.assert_called_once_with(
                'https://api.github.com/graphql',
                json={'query': mock.ANY, 'variables': mock.ANY},
                headers=self.headers
            )
