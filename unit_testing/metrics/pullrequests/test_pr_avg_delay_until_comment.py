import os
from unittest import TestCase, mock
from metrics.pullrequests import PRAvgDelayUntilComment



class TestPRAvgDelayUntilComment(TestCase):
    def setUp(self):
        # Seting the TOKEN
        self.headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # After each unit_testing do the following
    def tearDown(self):
        pass
    def test_run_query_success(self):
        # Calling Method
        result = PRAvgDelayUntilComment.get_pr_avg_delay_until_comment()

        # Assert data
        self.assertIsNotNone(result['avg_time_for_first_comment'])
        self.assertIsNotNone(result['pr_list'])

