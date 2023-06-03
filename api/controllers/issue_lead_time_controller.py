from datetime import datetime
from flask_restful import Resource
from metrics.kanban import IssueLeadTime
from database.metrics.kanban import IssueLeadTimeDB
from psycopg2.errorcodes import UNIQUE_VIOLATION
import psycopg2

class IssueLeadTimeController(Resource):
    def get(self, issue_no):
        """
        Get the issue lead time.
        ---
        parameters:
          - name: issue_no
            in: path
            type: integer
            required: true
            description: The issue lead time.
        responses:
          200:
            description: The issue lead time.
            schema:
              type: object
              properties:
                lead_time:
                  type: string
                pr_info:
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
            description: Invalid parameter.
            schema:
              type: object
              properties:
                error:
                  type: string
        """
        try:
            issue_lead_time = IssueLeadTime.get_lead_time_of_issue(issue_no)

            try:
                IssueLeadTimeDB.insert_data(issue_lead_time)
            except psycopg2.errors.lookup(UNIQUE_VIOLATION):
                None
            except TypeError:
                return {'error': 'This number is not an issue'}

            if issue_lead_time is None:
                return {'error': 'Issue is None'}, 400

            return {'issue_lead_time': issue_lead_time}
        except ValueError:
            return {'error': 'Invalid  parameter'}, 400
