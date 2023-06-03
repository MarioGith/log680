import unittest
import coverage
from unit_testing.controllers.test_issue_lead_time_controller import TestIssueLeadTimeController
from unit_testing.controllers.test_issue_lead_time_period_controller import TestIssueLeadTimePeriodController
from unit_testing.controllers.test_issue_completed_within_period_controller import TestIssuesCompletedWithinPeriodController
from unit_testing.controllers.test_issues_actives_by_column_controller import TestIssuesActiveByColumnController
from unit_testing.controllers.test_pr_avg_comments import TestPRAvgCommentsController
from unit_testing.controllers.test_pr_avg_delay_until_comment_controller import TestPRAvgDelayUntilCommentController
from unit_testing.controllers.test_pr_avg_lead_time_controller import TestPRAvgLeadTimeControler
from unit_testing.controllers.test_pr_lines_code import TestPRLinesCodeController
from unit_testing.controllers.test_pr_merged_in_period_controller import TestPRMergedInPeriodController
from unit_testing.metrics.kanban.test_issue_lead_time import TestIssueLeadTime
from unit_testing.metrics.kanban.test_issue_lead_time_period import TestIssueLeadTimePeriod
from unit_testing.metrics.kanban.test_issues_active_by_column import TestIssuesActiveByColumn
from unit_testing.metrics.kanban.test_issues_completed_within_period import TestIssuesCompletedWithinPeriod
from unit_testing.metrics.pullrequests.test_pr_avg_comments import TestPRAvgComments
from unit_testing.metrics.pullrequests.test_pr_avg_delay_until_comment import TestPRAvgDelayUntilComment
from unit_testing.metrics.pullrequests.test_pr_avg_lead_time import TestPRAvgLeadTime
from unit_testing.metrics.pullrequests.test_pr_lines_code import TestPRLinesCode
from unit_testing.metrics.pullrequests.test_pr_merged_in_period import TestPRMergedInPeriod
from integration_testing.test_issue_lead_time import TestIssueLeadTimeIntegration
from integration_testing.test_issue_lead_time_period import TestIssueLeadTimePeriodIntegration
from integration_testing.test_issues_actives_by_column import TestIssuesActiveByColumnIntegration
from integration_testing.test_issues_completed_wthin_period import TestIssuesCompletedWithinPeriodIntegration
from integration_testing.test_pr_avg_comments import TestPRAvgCommentsIntegration
from integration_testing.test_pr_avg_delay_until_comment import TestPRAvgDelayUntilCommentIntegration
from integration_testing.test_pr_lines_code import TestPRLinesCodeIntegration
from integration_testing.test_pr_merged_in_period import TestPRMergedInPeriodIntegration
from integration_testing.test_pr_avg_lead_time import TestPRAvgLeadTimeIntegration

# Starting coverage
cov = coverage.Coverage()
cov.start()

if __name__ == '__main__':
    # Create a set of tests
    all_tests = unittest.TestSuite()

    # Create a loader for the tests
    load_test = unittest.TestLoader()

    # Load unit_testing for routes
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssueLeadTimeController))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssueLeadTimePeriodController))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssuesCompletedWithinPeriodController))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssuesActiveByColumnController))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRAvgCommentsController))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRAvgDelayUntilCommentController))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRAvgLeadTimeControler))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRLinesCodeController))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRMergedInPeriodController))

    # Load unit_testing for metrics kanban
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssueLeadTime))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssueLeadTimePeriod))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssuesActiveByColumn))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssuesCompletedWithinPeriod))

    # Load unit_testing for metrics pull_requests
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRAvgComments))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRAvgDelayUntilComment))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRAvgLeadTime))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRLinesCode))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRMergedInPeriod))

    # Load integration_testing for api
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssueLeadTimeIntegration))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssueLeadTimePeriodIntegration))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssuesCompletedWithinPeriodIntegration))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestIssuesActiveByColumnIntegration))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRAvgCommentsIntegration))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRAvgDelayUntilCommentIntegration))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRAvgLeadTimeIntegration))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRLinesCodeIntegration))
    all_tests.addTests(load_test.loadTestsFromTestCase(TestPRMergedInPeriodIntegration))



    # Run the test suite
    unittest.TextTestRunner().run(all_tests)


    # Stop coverage and save report
    cov.stop()
    cov.save()
    cov.report()