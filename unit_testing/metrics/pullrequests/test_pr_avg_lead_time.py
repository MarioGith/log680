import os
from unittest import TestCase, mock
from metrics.pullrequests import PRAvgLeadTime


class TestPRAvgLeadTime(TestCase):
    def setUp(self):
        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ["TOKEN"])}

    # After each unit_testing do the following
    def tearDown(self):
        pass

    def test_run_query_success(self):
        # Calling Method
        result = PRAvgLeadTime.get_average_lead_time()

        # Assert data
        self.assertIsNotNone(result["average_lead_time"])
        self.assertIsNotNone(result["pr_list"])

    # def test_run_query_failure(self):
    #     # Mocking
    #     with mock.patch("requests.post") as mock_test:
    #         mock_test.return_value.status_code = 500
    #
    #         # Calling the method
    #         with self.assertRaises(Exception) as context:
    #             PRAvgLeadTime.get_average_lead_time()
    #
    #         data = mock_test.call_args[1]["json"]
    #         query = data["query"]
    #
    #         # Assert
    #         self.assertEqual(
    #             str(context.exception),
    #             "Query failed to run by returning code of 500. {}".format(query),
    #         )
    #
    #         mock_test.assert_called_once_with(
    #             "https://api.github.com/graphql",
    #             json={"query": mock.ANY, "variables": mock.ANY},
    #             headers=self.headers,
    #         )
