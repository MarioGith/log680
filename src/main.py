import json
import logging
import time
import psycopg2
import os

import requests
from signalrcore.hub_connection_builder import HubConnectionBuilder

#ajout d'un commentaire pour lancer le build

class Main:
    def __init__(self):
        self._hub_connection = None
        self.HOST = os.environ.get('HOST') # Setup your host here
        self.TOKEN = os.environ.get('TOKEN') # Setup your token here
        self.TICKETS = os.environ.get('TICKETS')  # Setup your tickets here
        self.T_MAX = os.environ.get('T_MAX')  # Setup your max temperature here
        self.T_MIN = os.environ.get('T_MIN')  # Setup your min temperature here
        self.DATABASE = psycopg2.connect(
            host=os.environ.get('DATABASE_HOST'),
            dbname=os.environ.get('DATABASE_DBNAME'),
            user=os.environ.get('DATABASE_USER'),
            password=os.environ.get('DATABASE_PASSWORD')
        )

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

        self._hub_connection.on("ReceiveSensorData", self.onSensorDataReceived)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(
            lambda data: print(f"||| An exception was thrown closed: {data.error}")
        )

    def onSensorDataReceived(self, data):
        try:
            print(data[0]["date"] + " --> " + data[0]["data"])
            date = data[0]["date"]
            dp = float(data[0]["data"])
            #self.send_temperature_to_fastapi(date, dp)
            self.analyzeDatapoint(date, dp)

            self.send_event_to_database(date, dp)
        except Exception as err:
            print(err)

    def analyzeDatapoint(self, date, data):
        if float(data) >= float(self.T_MAX):
            self.sendActionToHvac(date, "TurnOnAc", self.TICKETS)
        elif float(data) <= float(self.T_MIN):
            self.sendActionToHvac(date, "TurnOnHeater", self.TICKETS)

    def sendActionToHvac(self, date, action, nbTick):
        r = requests.get(f"{self.HOST}/api/hvac/{self.TOKEN}/{action}/{nbTick}")
        details = json.loads(r.text)
        print(details)

    def send_event_to_database(self, timestamp, event):
        #print timestamp and event
        #print(timestamp + " --> " + str(event))
        print(timestamp)
        print(event)
        try:
            #SQL query to insert data into the hvac_events table
            query = "INSERT INTO oxygen12db.hvac_events (eventDate, hvac_value) VALUES (%s, %s);"

            cursor = self.DATABASE.cursor()
            cursor.execute(query, (timestamp, event))
            self.DATABASE.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"Error inserting data into the database: {e}")
            self.DATABASE.rollback()
        pass


if __name__ == "__main__":
    main = Main()
    main.start()
