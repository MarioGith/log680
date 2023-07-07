from signalrcore.hub_connection_builder import HubConnectionBuilder
import logging
import requests
import json
import time
from datetime import datetime
from .db_manager import DBManager
import os


class Main:
    def __init__(self):
        self._hub_connection = None
        self.HOST = os.getenv("HOST")  # Setup your host here
        self.TOKEN = os.getenv("TOKEN")  # Setup your token here
        self.TICKETS = os.getenv("TICKETS")  # Setup your tickets here
        self.T_MAX = os.getenv("T_MAX")  # Setup your max temperature here
        self.T_MIN = os.getenv("T_MIN")  # Setup your min temperature here
        print(f"Token: {self.TOKEN}; Host: {self.HOST}")

    def __del__(self):
        if self._hub_connection is not None:
            self._hub_connection.stop()

    def setup(self):
        self.set_sensor_hub()

    def start(self):
        self.setup()
        self._hub_connection.start()

        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def set_sensor_hub(self):
        print("Attempting connection...")
        self._hub_connection = (
            HubConnectionBuilder()
            .with_url(f"{self.HOST}/SensorHub?token={self.TOKEN}")
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

        self._hub_connection.on("ReceiveSensorData", self.on_sensor_data_received)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(lambda data: print(f"||| An exception was thrown closed: {data.error}"))

    def on_sensor_data_received(self, data):
        try:
            print("Receiving data...")
            print(data[0]["date"] + " --> " + data[0]["data"])
            date = data[0]["date"]
            dp = float(data[0]["data"])
            self.send_event_to_database(date, dp)
            self.analyze_datapoint(date, dp)
        except Exception as err:
            print(err)

    def analyze_datapoint(self, date, data):
        if float(data) >= float(self.T_MAX):
            self.send_action_to_hvac(date, "TurnOnAc", self.TICKETS)
        elif float(data) <= float(self.T_MIN):
            self.send_action_to_hvac(date, "TurnOnHeater", self.TICKETS)

    def send_action_to_hvac(self, date, action, nbTick):
        r = requests.get(f"{self.HOST}/api/hvac/{self.TOKEN}/{action}/{nbTick}")
        details = json.loads(r.text)
        print(details)

    def send_event_to_database(self, timestamp, event):
        table_name = "OxygenCSTemperatureData"
        column_names = ', '.join(["DateCreated", "Temperature"])

        # Removing element after character '+' to convert to datetime object
        timestamp_string_truncated = timestamp.split('+', 1)[0]

        # Slicing last element of string and converting to datetime object for database insertion
        timestamp_datetime_converted = datetime.strptime(timestamp_string_truncated[:-1], '%Y-%m-%dT%H:%M:%S.%f')

        try:
            with DBManager() as db:
                print("Inserting data in database")
                cursor = db.cursor
                sql_query = f'''INSERT INTO {table_name} ({column_names}) VALUES (?, ?)'''
                cursor.execute(sql_query, [timestamp_datetime_converted, event])
                db.commit()
                print("Inserting values in database...")

        except requests.exceptions.RequestException as e:
            print(f"Exception occurred while attempting to insert data in database. Stacktrace: {e}")


if __name__ == "__main__":
    main = Main()
    main.start()
