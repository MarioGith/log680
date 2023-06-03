import requests
import os
import json
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

def get_snapshot(project_id, repo_owner, repo_name, repo_project_number):

    project_columns_query = """
      query($project_id: ID!){
        node(id: $project_id) {
          ... on ProjectV2 {
            fields(first: 100) {
              nodes {
                ... on ProjectV2SingleSelectField {
                  options {
                    name
                  }
                }
              }
            }
          }
        }
      }
    """

    # Create a dictionary of variables for the columns query
    project_columns_variables = {
        "project_id": project_id
    }

    columns_result = run_query(project_columns_query, project_columns_variables)
    #print(columns_result)

    column_items = columns_result["data"]["node"]["fields"]["nodes"][2]["options"]
    #print(column_items)

    json_result = {}

    for column in column_items:
        current_column_name = column["name"]
        # print(current_column_name)

        active_issues_query = """
          query($repo_owner: String!, $repo_name: String!, $repo_project_number: Int!){
            repository(owner: $repo_owner, name: $repo_name){
              projectV2(number: $repo_project_number) {
                  title
                  items(last: 100) {
                    nodes {
                      fieldValues(last: 2) {
                        nodes {
                          ... on ProjectV2ItemFieldTextValue {
                            text
                            item {
                              content {
                                ... on Issue {
                                  closed
                                  title
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

        # Create a dictionary of variables for the issues query
        active_issues_variables = {
            "repo_owner": repo_owner,
            "repo_name": repo_name,
            "repo_project_number": repo_project_number
        }

        issues_result = run_query(active_issues_query, active_issues_variables)
        #print(active_issues_result)

        project_items = issues_result["data"]["repository"]["projectV2"]["items"]["nodes"]
        #print(project_items)

        issues_count = 0

        # Calculate how many issues are in the current column
        for items in project_items:
            column_name = items["fieldValues"]["nodes"][1]["name"]

            # all items in the specified column
            if column_name.lower() == current_column_name.lower():
                #print(items["fieldValues"]["nodes"])
                # filter to issues only
                if "closed" in items["fieldValues"]["nodes"][0]["item"]["content"]:
                    issues_count += 1

        # Update the json dictionary with the column's data
        json_result.update({current_column_name : {'columnName': current_column_name, 'issuesCount': issues_count}})

    print(json_result)

    return json_result