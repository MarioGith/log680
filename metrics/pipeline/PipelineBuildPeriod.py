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


def get_build_period(start_date, end_date):
    owner = "CAMaji"
    repo = "oxygen-cs-grp2-eq10"
    pipeline_list = []
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs"
    average_build_time = 0
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()

        for workflow in result['workflow_runs']:
            pipeline_id = workflow['id']
            pipeline_name = workflow['name']
            created_at = datetime.datetime.fromisoformat(workflow['created_at'].replace("Z", "+00:00"))
            updated_at = datetime.datetime.fromisoformat(workflow['updated_at'].replace("Z", "+00:00"))
            run_started_at = datetime.datetime.fromisoformat(workflow['run_started_at'].replace("Z", "+00:00"))
            execution_time = updated_at - run_started_at
            pipeline_info = {
                "id": pipeline_id,
                "name": pipeline_name,
                "created": created_at.isoformat(),
                "updated": updated_at.isoformat(),
                "run_started_at": run_started_at.isoformat(),
                "execution_time": str(execution_time.total_seconds()) + " seconds"
            }

            average_build_time += execution_time.total_seconds()

            pipeline_list.append(pipeline_info)

        json_result = {
            "total_average_build_time": str(average_build_time/len(pipeline_list)) + " seconds" if average_build_time != 0 else 0,
            "pipeline_list": pipeline_list if pipeline_list else "0"
        }

        return json_result
