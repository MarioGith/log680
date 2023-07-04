import psycopg2

def insert_data(json_result):

    # print(json_result)

    # Connect to the database
    connection = psycopg2.connect(
        database='devopsmetrics',
        user='postgres',
        password='postgres',
        host='postgres',
        port='5432'
    )
    connection.autocommit = True

    cursor = connection.cursor()

    # print(json_result['average_lead_time'])

    cursor.execute('''INSERT INTO METRIC_PR_LEAD_TIME(SNAPSHOT_DATE,
                                                      AVG_LEAD_TIME
                                                      )
                                                      VALUES (current_timestamp, %s);''',
                                                      (
                                                          (json_result['average_lead_time'],)
                                                      )
                 )
    connection.commit()

    connection.close()