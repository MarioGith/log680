import unittest
from unittest.mock import patch, MagicMock
from src.main import Main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.main = Main()

    @patch('src.main.HubConnectionBuilder')
    def test_set_sensorhub(self, MockHubConnectionBuilder):
        self.main.set_sensorhub()
        MockHubConnectionBuilder.assert_called_once()

    @patch('src.main.requests.get')
    def test_send_action_to_hvac(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '{"status": "ok"}'
        mock_get.return_value = mock_response

        action = "TurnOnAc"
        self.main.send_action_to_hvac(action)

        expected_url = f"{self.main.HOST}/api/hvac/{self.main.TOKEN}/{action}/{self.main.TICKETS}"
        mock_get.assert_called_once_with(expected_url)

    def test_take_action(self):
        with patch.object(self.main, 'send_action_to_hvac') as mock_send_action:
            self.main.take_action(self.main.T_MAX + 1)
            mock_send_action.assert_called_with("TurnOnAc")

            self.main.take_action(self.main.T_MIN - 1)
            mock_send_action.assert_called_with("TurnOnHeater")

if __name__ == "__main__":
    unittest.main()