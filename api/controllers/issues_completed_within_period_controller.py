from datetime import datetime

from flask import request
from flask_restful import Resource
from metrics.kanban import IssuesCompletedWithinPeriod
from database.metrics.kanban import IssuesCompletedWithinPeriodDB
import re

date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')


def validate_date_format(date_string):
    if date_pattern.match(date_string):
        return True
    else:
        return False


class IssuesCompletedWithinPeriodController(Resource):
    def get(self):
        """
        Get the issues completed within a specified period.
        ---
        parameters:
          - name: startdate
            in: query
            type: string
            format: date
            required: true
            description: The start date of the period as YYYY-MM-DD.
          - name: enddate
            in: query
            type: string
            format: date
            required: true
            description: The end date of the period as YYYY-MM-DD.
        responses:
          200:
            description: The number of issues completed within a specified period.
            schema:
              type: object
              properties:
                completed_tasks:
                  type: string
                start_date:
                  type: string
                end_date:
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
            description: Invalid parameters.
            schema:
              type: object
              properties:
                error:
                  type: string
        """

        start_date = request.args.get('startdate')
        end_date = request.args.get('enddate')

        if not start_date or not end_date:
            return {'error': 'Missing parameters'}, 400

        if not validate_date_format(start_date) or not validate_date_format(end_date):
            return {'error': 'Invalid date format'}, 400

        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

            issues_completed = IssuesCompletedWithinPeriod.get_number_issues_completed_within_period(start_date_obj, end_date_obj)

            IssuesCompletedWithinPeriodDB.insert_data(issues_completed)

            return {'issues_completed': issues_completed}
        except ValueError:
            return {'error': 'Invalid date parameters'}, 400

