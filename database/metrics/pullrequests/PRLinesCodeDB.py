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
    # print(json_result['total_additions'])
    # print(json_result['total_count'])
    # print(json_result['avg_additions_per_pr'])

    cursor.execute('''INSERT INTO METRIC_PR_LINES_CODE(START_DATE,
                                                       END_DATE,
                                                       TOTAL_LINES_CODE,
                                                       TOTAL_PR_COUNT,
                                                       AVG_LINES_CODE
                                                       )
                                                      VALUES (%s, %s, %s, %s, %s);''',
                                                      (
                                                          json_result['start_date'],
                                                          json_result['end_date'],
                                                          json_result['total_additions'],
                                                          json_result['total_count'],
                                                          json_result['avg_additions_per_pr']
                                                      )
                 )
    connection.commit()

    connection.close()