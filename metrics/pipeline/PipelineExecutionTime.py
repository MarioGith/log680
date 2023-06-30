import json
import subprocess

import requests
import os
import datetime
import json

# Source : https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "token {}".format(os.environ['TOKEN']),
    "X-GitHub-Api-Version": "2022-11-28"
}

def run_query(query, variables):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables},
                            headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_execution_time_pipeline(pipeline_name):
    # Create the GraphQL query
    query = """
        query($repositoryName: String!, $ownerName: String!)  {
          repository(name: $repositoryName, owner: $ownerName) {
            id
            refs(refPrefix: "refs/heads/", first: 10) {
              edges {
                node {
                  id
                  target {
                    ... on Commit {
                      id
                      checkSuites(first: 10) {
                        nodes {
                          workflowRun {
                            id
                            event
                            createdAt
                            updatedAt
                            runNumber
                            workflow {
                              name
                            }
                            resourcePath
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
    """

    owner = "CAMaji"
    repo = "oxygen-cs-grp2-eq10"

    # Create a dictionary of variables for the query
    variables = {
        "repositoryName": repo,
        "ownerName": owner
    }

    result = run_query(query, variables)

    # Extract the information from the query result
    workflow_runs = result['data']['repository']['refs']['edges']
    pipeline_list = []

    for run in workflow_runs:

        workflows = run['node']['target']['checkSuites']['nodes']

        if workflows is not None:

            for workflow in workflows:
                workflow_run = workflow['workflowRun']
                if workflow_run is not None and workflow_run['workflow']['name'] == pipeline_name:
                    name = workflow_run['workflow']['name']
                    resource_path = workflow_run['resourcePath']
                    pipeline_info = get_workflow_info(name, resource_path)

                    pipeline_list.append(pipeline_info)

    json_result = {
        "pipeline_name": pipeline_name,
        "pipeline_list": pipeline_list if pipeline_list else "No workflow with this name"
    }

    return json_result


def get_workflow_info(pipeline_name, resource_path):
    pipeline_list = []
    url = f"https://api.github.com/repos{resource_path}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()

        print(result)

        pipeline_id = result['id']
        created_at = datetime.datetime.fromisoformat(result['created_at'].replace("Z", "+00:00"))
        updated_at = datetime.datetime.fromisoformat(result['updated_at'].replace("Z", "+00:00"))
        run_started_at = datetime.datetime.fromisoformat(result['run_started_at'].replace("Z", "+00:00"))
        execution_time = updated_at - run_started_at

        pipeline_info = {
            "id": pipeline_id,
            "name": pipeline_name,
            "created": created_at.isoformat(),
            "updated": updated_at.isoformat(),
            "run_started_at": run_started_at.isoformat(),
            "execution_time": str(execution_time.total_seconds()) + " seconds"
        }

        pipeline_list.append(pipeline_info)

        return pipeline_list
