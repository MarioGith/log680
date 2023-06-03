from datetime import datetime

from flask import request
from flask_restful import Resource
from metrics.kanban import IssuesActiveByColumn
from database.metrics.kanban import IssuesActiveByColumnDB

class IssuesActiveByColumnController(Resource):
    def get(self):
        """
        Get the number of active issues in Kanban
        ---
        parameters:
          - name: columnname
            in: query
            type: string
            required: true
            description: The name of the column in Kanban
        responses:
          200:
            description: The number of active issues in Kanban
            schema:
              type: object
              properties:
                column_name:
                  type: string
                total_items:
                  type: string
                total_tasks:
                  type: string
                total_closed_tasks:
                  type: string
                total_active_tasks:
                  type: string
                pr_list:
                    type: array
                    items:
                        type: object
                        properties:
                          id:
                            type: string
                          number:
                            type: integer
                          title:
                            type: string
                          description:
                            type: string
                          createdAt:
                            type: string
                          closedAt:
                            type: string
          400:
            description: Invalid parameter name.
            schema:
              type: object
              properties:
                error:
                  type: string
        """

        column_name = request.args.get('columnname')

        try:

            if column_name in ["Backlog", "À faire", "En cours", "Revue", "Terminée"]:

                issues_actives = IssuesActiveByColumn.get_number_of_active_issues_by_column(column_name)

                IssuesActiveByColumnDB.insert_data(issues_actives)

                return {'issues_actives': issues_actives}

            else:
                return {'error': 'Invalid parameter'}, 400

        except ValueError:
            return {'error': 'Failed try'}, 400

