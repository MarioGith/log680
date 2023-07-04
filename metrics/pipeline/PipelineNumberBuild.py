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
def get_number_build():

    owner = "CAMaji"
    repo = "oxygen-cs-grp2-eq10"
    pipeline_list = []
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()

        for workflow in result['workflow_runs']:

            pipeline_id = workflow['id']
            pipeline_name = workflow['name']
            created_at = datetime.datetime.fromisoformat(workflow['created_at'].replace("Z", "+00:00"))
            updated_at = datetime.datetime.fromisoformat(workflow['updated_at'].replace("Z", "+00:00"))

            pipeline_info = {
                "id": pipeline_id,
                "name": pipeline_name,
                "created": created_at.isoformat(),
                "updated": updated_at.isoformat()
            }

            pipeline_list.append(pipeline_info)

        json_result = {
            "total_count": result['total_count'],
            "pipeline_list": pipeline_list if pipeline_list else "0"
        }

        return json_result

