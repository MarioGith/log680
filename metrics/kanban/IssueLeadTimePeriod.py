import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Source : https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad
headers = {"Authorization": "token {}".format(os.environ["TOKEN"])}


def run_query(
    query, variables=None
):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": variables},
        headers=headers,
    )
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(
            "Query failed to run by returning code of {}. {}".format(
                request.status_code, query
            )
        )


def get_issue_lead_time_within_period(start_date, end_date):
    print(
        f"######### Temps (lead time) pour les tâches terminées dans une période donnée ({start_date} - {end_date})#########"
    )

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

    issue_data = result["data"]["repository"]["issues"]

    issues = issue_data["edges"]
    temp = datetime.now()
    closed_issue_count = 0
    issue_list = []

    for issue_node in issues:
        issue = issue_node["node"]
        issue_number = issue["number"]
        created_at = issue["createdAt"]
        closed_at = issue["closedAt"]

        if (
            start_date is not None
            and end_date is not None
            and start_date
            < datetime.strptime(closed_at, "%Y-%m-%dT%H:%M:%SZ")
            < end_date
        ):
            closed_issue_count += 1
            # Time between the issue's creation and closure
            time = datetime.strptime(
                closed_at, "%Y-%m-%dT%H:%M:%SZ"
            ) - datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
            temp += time
            print(f"Pour l'issue #{issue_number}, le temps (lead time) a été de {time}")

            issue_info = {
                "id": issue["id"],
                "number": issue["number"],
                "title": issue["title"],
                "description": issue["bodyText"],
                "createdAt": issue["createdAt"],
                # Ternary expression in python
                "closedAt": issue["closedAt"] if issue["closedAt"] else None,
            }

            issue_list.append(issue_info)

    # Calculate the average lead time
    average = (
        (temp - datetime.now()) / closed_issue_count if closed_issue_count != 0 else 0
    )
    print(f"Le temps moyen est de {average}")
    json_result = None
    if average != 0:
        json_result = {
            "average_time": average.total_seconds()
            if average.total_seconds() == 0
            else average.total_seconds(),
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "issue_list": issue_info,
        }

    return json_result
