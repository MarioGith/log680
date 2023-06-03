import requests
import os
from datetime import datetime

# Source : https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad
headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}


def run_query(query,
              variables=None):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables},
                            headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_number_issues_completed_within_period(start_date, end_date):
    print(f"######### Nombre de tâches complétées pour une période donnée ({start_date} - {end_date})#########")

    query = """
      {
        repository(owner:"Tzuyunii", name:"metrics-grp2-eq10-e23"){
          issues(states: CLOSED, first:50) {
            edges {
              node {
                id
                title
                bodyText
                number
                createdAt
                closedAt
              }
            }
          }
        }
      }
      """

    result = run_query(query)

    issues = result["data"]["repository"]["issues"]["edges"]
    closed_issue_count = 0
    issue_list = []

    if start_date is None or end_date is None:
        return None

    for issue_node in issues:
        issue = issue_node["node"]
        closed_at = issue["closedAt"]

        if start_date < datetime.strptime(closed_at, "%Y-%m-%dT%H:%M:%SZ") < end_date:
            closed_issue_count += 1

            issue_info = {
                "id": issue["id"],
                "number": issue["number"],
                "title": issue["title"],
                "description": issue["bodyText"],
                "createdAt": issue["createdAt"],

                # Ternary expression in python
                "closedAt": issue["closedAt"] if issue["closedAt"] else None
            }

            issue_list.append(issue_info)

    print(f"Nombre de tâches complétées entre {start_date} et {end_date}: {closed_issue_count}")

    json_result = {
        "completed_tasks": closed_issue_count,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "issue_list": issue_info
    }

    return json_result
