import unittest
from unittest.mock import MagicMock, patch
from src.main import Main

class TestDatabaseMethods(unittest.TestCase):

    @patch('src.main.psycopg2')
    def test_send_event_to_database(self, mock_psycopg2):
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        mock_psycopg2.connect.return_value = mock_db
        mock_db.cursor.return_value = mock_cursor

        # Initializing Main class with mock database
        main = Main()
        main.DATABASE = mock_db

        # Calling the method to test
        timestamp = '2023-06-30T14:46:14.9628352+00:00'
        event = 42.29
        main.send_event_to_database(timestamp, event)

        # Assert that the execute method was called with the expected query
        query = "INSERT INTO oxygen12db.hvac_events (eventDate, hvac_value) VALUES (%s, %s);"
        mock_cursor.execute.assert_called_once_with(query, (timestamp, event))
        
        # Assert that commit was called
        mock_db.commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
