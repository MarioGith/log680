import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

# Source : https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad
headers = {"Authorization": "token {}".format(os.environ["TOKEN"])}


def run_query(
    query, variables
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


def get_lead_time_of_issue(issue_no):
    # Create the GraphQL query
    query = """
    query($issue_no: Int!){
      repository(owner:"Tzuyunii", name:"metrics-grp2-eq10-e23") {
        issue(number: $issue_no) {
          id
          title
          url
          bodyText
          number
          createdAt
          closedAt
        }
      }
    }
    """

    # Create a dictionary of variables for the query
    variables = {"issue_no": issue_no}

    # Execute the query
    result = run_query(query, variables)
    print(result)

    issue_data = result["data"]["repository"]["issue"]

    if issue_data is None:
        return None

    # Extract data and print it
    issue_title = issue_data["title"]
    print("title: {}".format(issue_title))

    issue_createdAt = issue_data["createdAt"]
    print("createdAt: {}".format(issue_createdAt))

    issue_closedAt = issue_data["closedAt"]
    print("closedAt: {}".format(issue_closedAt))

    # Calculate the lead time based on the issue's created and closed dates
    date_created = datetime.datetime.strptime(issue_createdAt, "%Y-%m-%dT%H:%M:%SZ")
    date_closed = datetime.datetime.strptime(issue_closedAt, "%Y-%m-%dT%H:%M:%SZ")
    lead_time = date_closed - date_created
    print(lead_time)

    issue_info = {
        "id": issue_data["id"],
        "number": issue_data["number"],
        "title": issue_data["title"],
        "description": issue_data["bodyText"],
        "createdAt": issue_data["createdAt"],
        # Ternary expression in python
        "closedAt": issue_data["closedAt"] if issue_data["closedAt"] else None,
    }

    json_result = {"lead_time": lead_time.total_seconds(), "issue_info": issue_info}

    return json_result
