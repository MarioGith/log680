import requests
from datetime import datetime
import os

# Set the repository owner and name
owner_name = "Tzuyunii"
repo_name = "metrics-grp2-eq10-e23"

def get_average_lead_time():

    # Source : https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad
    headers = {"Authorization": "token {}".format(os.environ['TOKEN'])}

    # PR state
    state = "closed"

    # Make a GET request to retrieve the PR details
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/pulls?state={state}'
    response = requests.get(url, headers=headers)
    pull_requests = response.json()

    # Variables for calculating average lead time
    total_lead_time = 0
    closed_pull_requests_count = 0
    pr_list = []

    # Loop to calculate average lead time for PR
    for pull_request in pull_requests:

        created_at = datetime.strptime(pull_request['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        closed_at = datetime.strptime(pull_request["closed_at"], '%Y-%m-%dT%H:%M:%SZ')
        closed_time = closed_at - created_at

        pr_info = {
            "id": pull_request["id"],
            "number": pull_request["number"],
            "title": pull_request["title"],
            "description": pull_request.get('body', ''),
            "createdAt": pull_request["created_at"],

            # Ternary expression in python
            "closedAt": pull_request["closed_at"] if pull_request["closed_at"] else None
        }

        pr_list.append(pr_info)

        #days = closed_time.total_seconds() / (24 * 60 * 60)
        total_lead_time += closed_time.total_seconds()
        closed_pull_requests_count += 1


    # Calculate the average lead time
    if closed_pull_requests_count > 0:
        average_delay = total_lead_time / closed_pull_requests_count
        print("Average lead time in seconds: {}".format(average_delay))
    else:
        print("Average lead time in seconds: 0")
        average_delay = 0

    json_result = {
        "average_lead_time": average_delay,
        "pr_list": pr_list
    }

    return json_result

