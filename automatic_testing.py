import coverage
import unittest

from unit_testing.app.test_main import TestMain

# Starting coverage
cov = coverage.Coverage()
cov.start()

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMain)

    test_results = unittest.TextTestRunner().run(test_suite)

    if not test_results.wasSuccessful():
        raise Exception("One or more tests failed. Workflow action crashed.")

    # Stop coverage and save report
    cov.stop()
    cov.save()
    cov.report()
