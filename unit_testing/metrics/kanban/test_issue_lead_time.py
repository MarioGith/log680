import os
from unittest import TestCase, mock
from metrics.kanban import IssueLeadTime


class TestIssueLeadTime(TestCase):
    def setUp(self):
        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ["TOKEN"])}

    # After each unit_testing do the following
    def tearDown(self):
        pass

    def test_run_query_success(self):
        # Issue with a valid number of the TEST
        issue_no = 1

        # Calling Method
        result = IssueLeadTime.get_lead_time_of_issue(issue_no)

        # Assert data
        self.assertEqual(result["lead_time"], 288228.0)
        self.assertIsNotNone(result["issue_info"])

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
        with mock.patch("requests.post") as mock_test:
            mock_test.return_value.status_code = 500

            # Calling the method
            with self.assertRaises(Exception):
                IssueLeadTime.get_lead_time_of_issue(issue_no)

            # Assert
            mock_test.assert_called_once_with(
                "https://api.github.com/graphql",
                json={"query": mock.ANY, "variables": {"issue_no": issue_no}},
                headers=self.headers,
            )
