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

    # print(json_result['issue_info']['id'])
    # print(json_result['issue_info']['number'])
    # print(json_result['issue_info']['title'])
    # print(json_result['issue_info']['createdAt'])
    # print(json_result['issue_info']['closedAt'])
    # print(json_result['lead_time'])

    cursor.execute('''INSERT INTO ISSUE(ID_ISSUE,
                                        NUMBER,
                                        TITLE,
                                        CREATED_AT,
                                        CLOSED_AT,
                                        LEAD_TIME
                                        )
                                        VALUES (%s, %s, %s, %s, %s, %s);''',
                                        (
                                            json_result['issue_info']['id'],
                                            json_result['issue_info']['number'],
                                            json_result['issue_info']['title'],
                                            json_result['issue_info']['createdAt'],
                                            json_result['issue_info']['closedAt'],
                                            json_result['lead_time']
                                        )
                )
    connection.commit()

    connection.close()