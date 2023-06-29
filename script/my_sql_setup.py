"""Imports"""
import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL server host
    user="root",  # Replace with your MySQL username
    password="1234"  # Replace with your MySQL password
)

# Create a new database
DATABAS_NAME = "OxygenDB"  # Replace with your desired database name
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABAS_NAME}")

# Switch to the newly created database
cursor.execute(f"USE {DATABAS_NAME}")

# Create a table
TABLE_NAME = "AC_Event"  # Replace with your desired table name
cursor = conn.cursor()
create_table_query = f"""
    CREATE TABLE {TABLE_NAME} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        event VARCHAR(64) NOT NULL,
        temp DECIMAL(6,2) NOT NULL         
    )
"""
cursor.execute(create_table_query)

# Close the cursor
cursor.close()
