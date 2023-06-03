import psycopg2
from datetime import datetime

connection = psycopg2.connect(
    user='postgres',
    password='postgres',
    host='127.0.0.1',
    port='5432'
)
connection.autocommit = True

cursor = connection.cursor()

# Create the database
sql_statement = '''CREATE DATABASE devopsmetrics;'''
cursor.execute(sql_statement)

# Connect to the new database
connection = psycopg2.connect(
    database='devopsmetrics',
    user='postgres',
    password='postgres',
    host='127.0.0.1',
    port='5432'
)
connection.autocommit = True

cursor = connection.cursor()

# Create tables
sql_statement = '''CREATE TABLE KANBAN_SNAPSHOT(
    SNAPSHOT_DATE timestamp with time zone NOT NULL,
    COLUMN_1_NAME VARCHAR(50), 
    COLUMN_1_ISSUES_COUNT INT, 
    COLUMN_2_NAME VARCHAR(50), 
    COLUMN_2_ISSUES_COUNT INT, 
    COLUMN_3_NAME VARCHAR(50), 
    COLUMN_3_ISSUES_COUNT INT, 
    COLUMN_4_NAME VARCHAR(50), 
    COLUMN_4_ISSUES_COUNT INT, 
    COLUMN_5_NAME VARCHAR(50), 
    COLUMN_5_ISSUES_COUNT INT 
    );'''
cursor.execute(sql_statement)

sql_statement = '''CREATE TABLE ISSUE(
    ID_ISSUE VARCHAR(25) NOT NULL UNIQUE PRIMARY KEY,
    NUMBER INTEGER NOT NULL,
    TITLE VARCHAR(250),
    CREATED_AT TIMESTAMP WITH TIME ZONE NOT NULL,
    CLOSED_AT TIMESTAMP WITH TIME ZONE,
    LEAD_TIME INTEGER
);'''
cursor.execute(sql_statement)

sql_statement = '''CREATE TABLE METRIC_ISSUE_LEAD_TIME_IN_PERIOD(
    ID_METRIC SERIAL PRIMARY KEY,
    START_DATE TIMESTAMP WITH TIME ZONE NOT NULL,
    END_DATE TIMESTAMP WITH TIME ZONE NOT NULL,
    AVG_LEAD_TIME REAL
);'''
cursor.execute(sql_statement)

sql_statement = '''CREATE TABLE METRIC_ACTIVE_ISSUES_BY_COLUMN(
    ID_METRIC SERIAL PRIMARY KEY,
    SNAPSHOT_DATE TIMESTAMP WITH TIME ZONE NOT NULL,
    COLUMN_NAME VARCHAR(50) NOT NULL,
    ACTIVE_ISSUES INTEGER NOT NULL 
);'''
cursor.execute(sql_statement)

sql_statement = '''CREATE TABLE METRIC_ISSUES_COMPLETED_WITHIN_PERIOD(
    ID_METRIC SERIAL PRIMARY KEY,
    START_DATE TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    END_DATE TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    COMPLETED_ISSUES INTEGER NOT NULL
);'''
cursor.execute(sql_statement)

sql_statement = '''CREATE TABLE METRIC_PR_LEAD_TIME(
    ID_METRIC SERIAL PRIMARY KEY,
    SNAPSHOT_DATE TIMESTAMP WITH TIME ZONE NOT NULL,
    AVG_LEAD_TIME REAL
);'''
cursor.execute(sql_statement)

sql_statement = '''CREATE TABLE METRIC_PR_MERGED_IN_PERIOD(
    ID_METRIC SERIAL PRIMARY KEY,
    START_DATE TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    END_DATE TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    TOTAL_PR_MERGED INTEGER NOT NULL
);'''
cursor.execute(sql_statement)

sql_statement = '''CREATE TABLE METRIC_PR_LINES_CODE(
    ID_METRIC SERIAL PRIMARY KEY,
    START_DATE TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    END_DATE TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    TOTAL_LINES_CODE INTEGER NOT NULL,
    TOTAL_PR_COUNT INTEGER NOT NULL,
    AVG_LINES_CODE REAL NOT NULL
);'''
cursor.execute(sql_statement)

sql_statement = '''CREATE TABLE METRIC_PR_AVG_DELAY_UNTIL_FIRST_COMMENT(
    ID_METRIC SERIAL PRIMARY KEY,
    SNAPSHOT_DATE TIMESTAMP WITH TIME ZONE NOT NULL,
    AVG_DELAY REAL
);'''
cursor.execute(sql_statement)

sql_statement = '''CREATE TABLE METRIC_PR_AVG_COMMENTS(
    ID_METRIC SERIAL PRIMARY KEY,
    SNAPSHOT_DATE TIMESTAMP WITH TIME ZONE NOT NULL,
    PR_COUNT INTEGER NOT NULL,
    TOTAL_COMMENTS INTEGER NOT NULL,
    AVG_COMMENTS REAL NOT NULL
);'''
cursor.execute(sql_statement)

connection.close()
