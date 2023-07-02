import os
import unittest

class TestEnvVariables(unittest.TestCase):
    def test_env_variables(self):
        MANDATORY_VARIABLES = ["HOST","TOKEN","TICKETS","T_MAX","T_MIN","DATABASE_HOST"]

        for var in MANDATORY_VARIABLES:
            self.assertTrue(var in os.environ.keys(), f"{var} environment variable is not set")
            self.assertTrue(os.environ[var] != "",f"{var} environment variable should not be empty")

if __name__ == '__main__':
    unittest.main()