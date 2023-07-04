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

    # print(json_result['pr_count'])
    # print(json_result['total_comments'])
    # print(json_result['average_comments_per_pr'])

    cursor.execute('''INSERT INTO METRIC_PR_AVG_COMMENTS(SNAPSHOT_DATE,
                                                         PR_COUNT,
                                                         TOTAL_COMMENTS,
                                                         AVG_COMMENTS
                                                         )
                                                         VALUES (current_timestamp, %s, %s, %s);''',
                                                         (
                                                             json_result['pr_count'],
                                                             json_result['total_comments'],
                                                             json_result['average_comments_per_pr']
                                                         )
                 )
    connection.commit()

    connection.close()