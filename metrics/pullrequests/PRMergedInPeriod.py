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


def get_pr_lead_time_in_period(start_date, end_date):
    # Create the GraphQL query
    query = """
    {
      repository(owner:"Tzuyunii", name:"metrics-grp2-eq10-e23"){
		pullRequests(first:50) {
		  edges {
		    node {
		      id
              number
              title
              totalCommentsCount
              createdAt
              mergedAt
              closedAt
		    }
		  }
	    }
      }
    }
    """
    if start_date is None or end_date is None:
        return None

    # Execute the query
    result = run_query(query)

    pull_requests = result["data"]["repository"]["pullRequests"]["edges"]

    total_pr_merged = 0
    pr_list = []
    for pr_node in pull_requests:
        pull_request = pr_node["node"]
        pr_merged_at = pull_request["mergedAt"]

        if pr_merged_at != None:
            date_merged = datetime.strptime(pr_merged_at, "%Y-%m-%dT%H:%M:%SZ")

            # Remove hours, minutes, and seconds
            date_merged_without_time = datetime(
                year=date_merged.year, month=date_merged.month, day=date_merged.day
            )

            if (
                date_merged_without_time >= start_date
                and date_merged_without_time <= end_date
            ):
                total_pr_merged += 1

            pr_info = {
                "id": pull_request["id"],
                "number": pull_request["number"],
                "title": pull_request["title"],
                "createdAt": pull_request["createdAt"],
                # Ternary expression in python
                "closedAt": pull_request["closedAt"]
                if pull_request["closedAt"]
                else None,
            }

            pr_list.append(pr_info)
    print("Total PRs that were merged:" + str(total_pr_merged))

    json_result = {
        "total_pr_merged": total_pr_merged,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "pr_list": pr_list,
    }

    return json_result
