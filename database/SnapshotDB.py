import psycopg2

def insert_data(json_result):

    print(json_result)

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

    backlog = 'Backlog'
    print(json_result[backlog]['columnName'])
    print(json_result[backlog]['issuesCount'])

    cursor.execute('''INSERT INTO KANBAN_SNAPSHOT(SNAPSHOT_DATE,
                                                  COLUMN_1_NAME,
                                                  COLUMN_1_ISSUES_COUNT,
                                                  COLUMN_2_NAME,
                                                  COLUMN_2_ISSUES_COUNT,
                                                  COLUMN_3_NAME,
                                                  COLUMN_3_ISSUES_COUNT,
                                                  COLUMN_4_NAME,
                                                  COLUMN_4_ISSUES_COUNT,
                                                  COLUMN_5_NAME,
                                                  COLUMN_5_ISSUES_COUNT
                                                  )
                                           VALUES (current_timestamp, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',
                                                  (
                                                      json_result['Backlog']['columnName'],
                                                      json_result['Backlog']['issuesCount'],
                                                      json_result['À faire']['columnName'],
                                                      json_result['À faire']['issuesCount'],
                                                      json_result['En cours']['columnName'],
                                                      json_result['En cours']['issuesCount'],
                                                      json_result['Revue']['columnName'],
                                                      json_result['Revue']['issuesCount'],
                                                      json_result['Terminée']['columnName'],
                                                      json_result['Terminée']['issuesCount']
                                                  )
                )

    connection.commit()

    connection.close()