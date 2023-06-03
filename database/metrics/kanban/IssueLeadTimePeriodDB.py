import psycopg2

def insert_data(json_result):

    # print(json_result)

    # Connect to the database
    connection = psycopg2.connect(
        database='devopsmetrics',
        user='postgres',
        password='postgres',
        host='127.0.0.1',
        port='5432'
    )
    connection.autocommit = True

    cursor = connection.cursor()

    # print(json_result['start_date'])
    # print(json_result['end_date'])
    # print(json_result['average_time'])

    cursor.execute('''INSERT INTO METRIC_ISSUE_LEAD_TIME_IN_PERIOD(START_DATE,
                                                                   END_DATE,
                                                                   AVG_LEAD_TIME
                                                                   )
                                                                   VALUES (%s, %s, %s);''',
                                                                   (
                                                                       json_result['start_date'],
                                                                       json_result['end_date'],
                                                                       json_result['average_time']
                                                                   )
                )
    connection.commit()

    connection.close()