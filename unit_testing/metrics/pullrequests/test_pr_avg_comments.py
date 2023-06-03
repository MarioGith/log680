import os
from unittest import TestCase, mock
from metrics.pullrequests import PRAvgComments



class TestPRAvgComments(TestCase):
    def setUp(self):
        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # After each unit_testing do the following
    def tearDown(self):
        pass
    def test_run_query_success(self):
        # Calling Method
        result = PRAvgComments.avg_number_of_comments_per_pr()

        # Assert data
        self.assertIsNotNone(result['pr_count'])
        self.assertIsNotNone(result['pr_list'])
    def test_run_query_failure(self):
        # Mocking
        with mock.patch('requests.post') as mock_test:
            mock_test.return_value.status_code = 500

            # Calling the method
            with self.assertRaises(Exception):
                PRAvgComments.avg_number_of_comments_per_pr()

            # Assert
            mock_test.assert_called_once_with(
                'https://api.github.com/graphql',
                json={'query': mock.ANY, 'variables': mock.ANY},
                headers=self.headers
            )
