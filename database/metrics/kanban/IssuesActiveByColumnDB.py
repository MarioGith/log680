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

    # print(json_result['column_name'])
    # print(json_result['total_active_tasks'])

    cursor.execute('''INSERT INTO METRIC_ACTIVE_ISSUES_BY_COLUMN(SNAPSHOT_DATE,
                                                                 COLUMN_NAME,
                                                                 ACTIVE_ISSUES
                                                                )
                                                                VALUES (current_timestamp, %s, %s);''',
                                                                (
                                                                    json_result['column_name'],
                                                                    json_result['total_active_tasks']
                                                                )
                )
    connection.commit()

    connection.close()