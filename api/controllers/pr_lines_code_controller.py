from datetime import datetime

from flask import request
from flask_restful import Resource
from metrics.pullrequests import PRLinesCode
from database.metrics.pullrequests import PRLinesCodeDB
import re

date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')


def validate_date_format(date_string):
    if date_pattern.match(date_string):
        return True
    else:
        return False


class PRLinesCodeController(Resource):
    def get(self):
        """
        Get the number of code lines within a specified period.
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
            description: The number of code lines within the period.
            schema:
              type: object
              properties:
                total_additions:
                  type: string
                total_count:
                  type: string
                avg_additions_per_pr:
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

            pr_lines_code = PRLinesCode.get_pr_lines_code_in_period(start_date_obj, end_date_obj)

            PRLinesCodeDB.insert_data(pr_lines_code)

            return {'pr_lines_code': pr_lines_code}
        except ValueError:
            return {'error': 'Invalid date parameters'}, 400


