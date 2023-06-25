import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL server host
    user="root",  # Replace with your MySQL username
    password="1234"  # Replace with your MySQL password
)

# Create a new database
database_name = "OxygenDB"  # Replace with your desired database name
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

# Switch to the newly created database
cursor.execute(f"USE {database_name}")

# Create a table
table_name = "AC_Event"  # Replace with your desired table name
cursor = conn.cursor()
create_table_query = f"""
    CREATE TABLE {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        event Varchar(64) NOT NULL,
        
    )
"""
cursor.execute(create_table_query)

# Close the cursor and connection
cursor.close()
conn.close()

print(f"Database {database_name} and table {table_name} created successfully!")
