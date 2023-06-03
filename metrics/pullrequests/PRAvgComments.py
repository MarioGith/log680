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

def avg_number_of_comments_per_pr():
    print(f"######### Nombre moyen de commentaires sur un PR #########")

    query = """
      {
        repository(owner:"Tzuyunii", name:"metrics-grp2-eq10-e23"){
          pullRequests(first:50) {
            edges {
              node {
                id
                number
                title
                bodyText
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

    pr_count = 0
    comments_count = 0
    pr_list = []

    for pr_node in pull_requests:
        pr_count += 1
        pull_request = pr_node["node"]
        comments = pull_request["comments"]["edges"]
        comments_count += len(comments)
        comments_on_pr = len(comments)

        pr_info  = {
            "id": pull_request["id"],
            "number": pull_request["number"],
            "title": pull_request["title"],
            "description": pull_request["bodyText"],
            "createdAt": pull_request["createdAt"],
            "nombre de commentaires": str(comments_on_pr),
            # Ternary expression in python
            "closedAt": pull_request["closedAt"] if pull_request["closedAt"] else None
        }

        comments_on_pr = 0

        pr_list.append(pr_info)

    average_comments = comments_count/pr_count
    result = (f"Nombre total de PR: {pr_count}\n"
          f"Nombre total de commentaires: {comments_count}\n"
          f"Nombre moyen de commentaires par PR: {average_comments}")

    json_result = {
        "pr_count": pr_count,
        "total_comments": comments_count,
        "average_comments_per_pr": average_comments,
        "pr_list": pr_list
    }

    print(result)

    return json_result