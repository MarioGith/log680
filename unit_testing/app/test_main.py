from unittest import TestCase

from dotenv import load_dotenv
import unittest
import os
from unittest.mock import patch, MagicMock

from src.main import Main

load_dotenv()


class TestMain(TestCase):
    def setUp(self):
        self.obj = Main()

    def test_host_variable_exists(self):
        self.assertIsNotNone(os.environ.get("HOST"), "HOST is missing")

    def test_token_variable_exists(self):
        self.assertIsNotNone(
            os.environ.get("OXYGENCS_TOKEN"), "OXYGENCS_TOKEN is missing"
        )

    def test_tickets_variable_exists(self):
        self.assertIsNotNone(os.environ.get("TICKETS"), "TICKETS is missing")

    def test_t_max_variable_exists(self):
        self.assertIsNotNone(os.environ.get("T_MAX"), "T_MAX is missing")

    def test_t_min_variable_exists(self):
        self.assertIsNotNone(os.environ.get("T_MIN"), "T_MIN is missing")

    def test_env_variables_are_valid(self):
        host = os.environ.get("HOST")
        self.assertIsNotNone(host, "HOST is missing")
        self.assertNotEqual(host, "", "HOST is empty")

        token = os.environ.get("OXYGENCS_TOKEN")
        self.assertIsNotNone(token, "OXYGENCS_TOKEN is missing")
        self.assertNotEqual(token, "", "OXYGENCS_TOKEN is empty")

        tickets = os.environ.get("TICKETS")
        self.assertIsNotNone(tickets, "TICKETS is missing")
        self.assertTrue(tickets.isdigit(), "TICKETS should be a positive integer")

        t_min = os.environ.get("T_MAX")
        self.assertIsNotNone(t_min, "T_MAX is missing")
        self.assertTrue(t_min.isdigit(), "T_MAX should be a positive integer")

        t_min = os.environ.get("T_MIN")
        self.assertIsNotNone(t_min, "T_MIN is missing")
        self.assertTrue(t_min.isdigit(), "T_MIN should be a positive integer")

    def test_onSensorDataReceived(self):
        data = [
            {"date": "2023-06-30T19:01:28.2222471+00:00", "data": "30"},
        ]
        self.obj.send_temperature_to_fastapi = MagicMock()
        self.obj.analyzeDatapoint = MagicMock()
        try:
            self.obj.onSensorDataReceived(data)
        except Exception as err:
            self.fail((f"onSensorDataReceived raised an exception: {err}"))
        # self.obj.send_temperature_to_fastapi.assert_called_once()
        self.obj.analyzeDatapoint.assert_called_once()

    def test_analyzeDatapoint(self):
        self.obj.sendActionToHvac = MagicMock()
        try:
            self.obj.analyzeDatapoint("2023-06-30T19:01:28.2222471+00:00", 30)
        except Exception as err:
            self.fail((f"analyzeDatapoint raised an exception: {err}"))
        self.obj.sendActionToHvac.assert_called_once_with(
            "2023-06-30T19:01:28.2222471+00:00", "TurnOnAc", "1"
        )

    def test_set_env_variable(self):
        os.environ["T_MAX"] = "20"
        self.assertEquals(os.environ.get("T_MAX"), "20")
