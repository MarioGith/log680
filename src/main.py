import os

from signalrcore.hub_connection_builder import HubConnectionBuilder
import logging
import requests
import json
import time


class NullTokenException(Exception):
    # raised when token is None
    pass

DEFAULT_HOST = 'localhost'
DEFAULT_TOKEN = 'dummy_token'
DEFAULT_TICKETS = 'dummy_tickets'
DEFAULT_T_MAX = '0'
DEFAULT_T_MIN = '0'
DEFAULT_DATABASE = 'dummy_database'
DEFAULT_DATABASE_USER = 'dummy_user'
DEFAULT_DATABASE_PASSWORD = 'dummy_password'
DEFAULT_DATABASE_HOST = 'localhost'

class Main:
    def __init__(self):
        self._hub_connection = None
        self.HOST = os.getenv('HOST', DEFAULT_HOST)  # Setup your host here
        self.TOKEN = os.getenv('TOKEN', None)  # Setup your token here
        self.TICKETS = os.getenv('TICKETS', DEFAULT_TICKETS)  # Setup your tickets here
        self.T_MAX = os.getenv('T_MAX', DEFAULT_T_MAX)  # Setup your max temperature here
        self.T_MIN = os.getenv('T_MIN', DEFAULT_T_MIN)  # Setup your min temperature here
        self.DATABASE = os.getenv('DATABASE', DEFAULT_DATABASE)  # Setup your database here
        self.DATABASE_HOST = os.getenv('DATABASE_HOST', DEFAULT_DATABASE_HOST)
        self.DATABASE_USER = os.getenv('DATABASE_USER', DEFAULT_DATABASE_USER)
        self.DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', DEFAULT_DATABASE_PASSWORD)

    def validate_token(self):
        if self.TOKEN is None:
            raise NullTokenException('Token is None, must set value')

    def __del__(self):
        if self._hub_connection != None:
            self._hub_connection.stop()

    def setup(self):
        self.setSensorHub()

    def start(self):
        self.setup()
        self._hub_connection.start()

        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def setSensorHub(self):
        self._hub_connection = (
            HubConnectionBuilder()
            .with_url(f"http://{self.HOST}/SensorHub?token={self.TOKEN}")
            .configure_logging(logging.INFO)
            .with_automatic_reconnect(
                {
                    "type": "raw",
                    "keep_alive_interval": 10,
                    "reconnect_interval": 5,
                    "max_attempts": 999,
                }
            )
            .build()
        )

        self._hub_connection.on("ReceiveSensorData", self.onSensorDataReceived)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(lambda data: print(f"||| An exception was thrown closed: {data.error}"))

    def onSensorDataReceived(self, data):
        try:
            print(data[0]["date"] + " --> " + data[0]["data"])
            date = data[0]["date"]
            dp = float(data[0]["data"])
            self.send_temperature_to_fastapi(date, dp)
            self.analyzeDatapoint(date, dp)
        except Exception as err:
            print(err)

    def analyzeDatapoint(self, date, data):
        if float(data) >= float(self.T_MAX):
            self.sendActionToHvac(date, "TurnOnAc", self.TICKETS)
        elif float(data) <= float(self.T_MIN):
            self.sendActionToHvac(date, "TurnOnHeater", self.TICKETS)

    def sendActionToHvac(self, date, action, nbTick):
        r = requests.get(f"http://{self.HOST}/api/hvac/{self.TOKEN}/{action}/{nbTick}")
        details = json.loads(r.text)
        print(details)

    def send_temperature_to_fastapi(self, date, dp):
        # to implement
        pass

    def send_event_to_database(self, timestamp, event):
        try:
            # To implement
            pass
        except requests.exceptions.RequestException as e:
            # To implement
            pass


if __name__ == "__main__":
    main = Main()
    main.validate_token()
    main.start()
