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

    # print(json_result['avg_time_for_first_comment'])

    cursor.execute('''INSERT INTO METRIC_PR_AVG_DELAY_UNTIL_FIRST_COMMENT(SNAPSHOT_DATE,
                                                                          AVG_DELAY
                                                                          )
                                                                          VALUES (current_timestamp, %s);''',
                                                                          (
                                                                              (json_result['avg_time_for_first_comment'],)
                                                                          )
                 )
    connection.commit()

    connection.close()