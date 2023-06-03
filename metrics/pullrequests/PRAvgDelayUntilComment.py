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


def get_pr_avg_delay_until_comment():
    print(f"######### Délai moyen jusqu'au premier commentaire #########")

    query = """
      {
        repository(owner:"Tzuyunii", name:"metrics-grp2-eq10-e23"){
          pullRequests(first:50) {
            edges {
              node {
                id
                title
                bodyText
                number
                createdAt
                closedAt
                comments(first:50) {
                  edges {
                    node {
                      createdAt
                    }
                  }
                }
              }
            }
          }
        }
      }
      """

    result = run_query(query)
    pull_requests = result["data"]["repository"]["pullRequests"]["edges"]

    temp = datetime.now()
    pr_with_comment_count = 0
    pr_list = []

    for pr_node in pull_requests:
        pull_request = pr_node["node"]
        pull_request_number = pull_request["number"]
        pr_created_at = pull_request["createdAt"]
        comments = pull_request["comments"]["edges"]
        first_comment = "no comment"
        if comments:
            pr_with_comment_count += 1

            first_comment = comments[0]["node"]
            first_comment_created_at = first_comment["createdAt"]
            delay = datetime.strptime(first_comment_created_at, "%Y-%m-%dT%H:%M:%SZ") - datetime.strptime(pr_created_at,
                                                                                                          "%Y-%m-%dT%H:%M:%SZ")
            temp += delay
            print(
                f"PR #{pull_request_number}, PR createdAt {pr_created_at}, first comment createdAt {first_comment}, delay: {delay}")
        if not comments:
            print(f"PR #{pull_request_number}, PR createdAt {pr_created_at}, no comment")

        pr_info = {
            "id": pull_request["id"],
            "number": pull_request["number"],
            "title": pull_request["title"],
            "description": pull_request["bodyText"],
            "createdAt": pull_request["createdAt"],
            "time_first_comment": str(first_comment),
            # Ternary expression
            "closedAt": pull_request["closedAt"] if pull_request["closedAt"] else None
        }

        pr_list.append(pr_info)

    average_delay = (temp - datetime.now()) / pr_with_comment_count
    print(f"Le délai moyen pour le premier commentaire est de {average_delay}")

    json_result = {
        "avg_time_for_first_comment": average_delay.total_seconds(),
        "pr_list": pr_list
    }

    return json_result
