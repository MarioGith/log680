from datetime import datetime
from flask import request
from flask_restful import Resource
from metrics.snapshot import IssuesSnapshot
from database import SnapshotDB

class IssueSnapshotController(Resource):
    def get(self):
        """
                Get the snapshot containing column names and number of issues per column.
                ---
                parameters:
                  - name: projectid
                    in: query
                    type: string
                    required: true
                    description: The project's id
                  - name: repoowner
                    in: query
                    type: string
                    required: true
                    description: The repository's owner
                  - name: reponame
                    in: query
                    type: string
                    required: true
                    description: The repository's name
                  - name: repoprojectnumber
                    in: query
                    type: integer
                    required: true
                    description: The repository's project number
                responses:
                  200:
                    description: The snapshot of the project.
                  400:
                    description: Invalid parameters.
                    schema:
                      type: object
                      properties:
                        error:
                          type: string
                """
        try:
            project_id = request.args.get('projectid')
            repo_owner = request.args.get('repoowner')
            repo_name = request.args.get('reponame')
            repo_project_number = int(request.args.get('repoprojectnumber'))

            if not project_id or not repo_owner or not repo_name or not repo_project_number:
                return {'error': 'Missing parameters'}, 400

            json_result = IssuesSnapshot.get_snapshot(project_id, repo_owner, repo_name, repo_project_number)

            SnapshotDB.insert_data(json_result)

        except ValueError:
            return {'error': 'Unknown error?'}, 400

        return json_result
