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


def get_number_of_active_issues_by_column(column):
    print(
        f"######### Nombre de tâches actives pour une colonne donnée: {column} #########"
    )

    query = """
      {
        repository(owner: "Tzuyunii", name: "metrics-grp2-eq10-e23"){
          projectV2(number: 2) {
              title
              items(first: 100) {
                nodes {
                  fieldValues(last: 2) {
                    nodes {
                      ... on ProjectV2ItemFieldTextValue {
                        text
                        item {
                          content {
                            ... on Issue {
                              id
                              title
                              bodyText
                              number
                              createdAt
                              closedAt
                              closed
                              state
                            }
                          }
                        }
                      }
                      ... on ProjectV2ItemFieldSingleSelectValue {
                        field {
                          ... on ProjectV2FieldCommon {
                            name
                          }
                        }
                        name
                      }
                    }
                  }
                }
              }
            }
        }
      }
      """
    if column is None:
        return None
    result = run_query(query)
    project_items = result["data"]["repository"]["projectV2"]["items"]["nodes"]
    # print(project_items)
    item_count = 0
    issues_count = 0
    active_issues_count = 0
    closed_issues_count = 0
    issue_list = []

    for items in project_items:
        column_name = items["fieldValues"]["nodes"][1]["name"]

        # all items in the specified column
        if column_name.lower() == column.lower():
            item_count += 1
            # print(items["fieldValues"]["nodes"])
            # filter to issues only
            if "closed" in items["fieldValues"]["nodes"][0]["item"]["content"]:
                issues_count += 1
                is_closed = items["fieldValues"]["nodes"][0]["item"]["content"][
                    "closed"
                ]
                if is_closed:
                    closed_issues_count += 1
                elif not is_closed:
                    active_issues_count += 1

            if items["fieldValues"]["nodes"][0]["item"]["content"]:
                issue_info = {
                    "id": items["fieldValues"]["nodes"][0]["item"]["content"]["id"],
                    "number": items["fieldValues"]["nodes"][0]["item"]["content"][
                        "number"
                    ],
                    "title": items["fieldValues"]["nodes"][0]["item"]["content"][
                        "title"
                    ],
                    "description": items["fieldValues"]["nodes"][0]["item"]["content"][
                        "bodyText"
                    ],
                    "createdAt": items["fieldValues"]["nodes"][0]["item"]["content"][
                        "createdAt"
                    ],
                    "closedAt": items["fieldValues"]["nodes"][0]["item"]["content"][
                        "closedAt"
                    ]
                    if items["fieldValues"]["nodes"][0]["item"]["content"]["closedAt"]
                    else None,
                }

                issue_list.append(issue_info)

    result = (
        f"Dans colonne: {column}\n"
        f"Nombre total de items: {item_count}\n"
        f"Nombre total de taches: {issues_count}\n"
        f"Nombre total de taches fermees: {closed_issues_count}\n"
        f"Nombre total de taches actives: {active_issues_count}"
    )

    print(result)

    json_result = {
        "column_name": column,
        "total_items": item_count,
        "total_tasks": issues_count,
        "total_closed_tasks": closed_issues_count,
        "total_active_tasks": active_issues_count,
        "issue_list": issue_list,
    }

    return json_result
