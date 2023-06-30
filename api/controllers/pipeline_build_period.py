from datetime import datetime
import re

from flask_restful import Resource
from metrics.pipeline import PipelineBuildPeriod
from flask import request
from database.metrics.kanban import IssueLeadTimeDB
from psycopg2.errorcodes import UNIQUE_VIOLATION
import psycopg2

date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')


def validate_date_format(date_string):
    if date_pattern.match(date_string):
        return True
    else:
        return False
class PipelineBuildPeriodController(Resource):
    def get(self):
        """
        Get the average build time.
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
            description: The average build time.
            schema:
              type: object
              properties:
                pipeline_id:
                  type: string
                pipeline_name:
                  type: string
                pipeline_list:
                    type: array
                    items:
                        type: object
                        properties:
                          id:
                            type: string
                          name:
                            type: string
                          created:
                            type: string
                          updated:
                            type: string
                          started:
                            type: string
                          execution_time:
                            type: string

          400:
            description: Invalid parameter.
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

            if end_date_obj <= start_date_obj:
                return {'error': 'End date must be after start date'}, 400


            pipeline_build_period = PipelineBuildPeriod.get_build_period(start_date_obj, end_date_obj)

            #IssuesCompletedWithinPeriodDB.insert_data(issues_completed)

            return {'pipeline_build_period': pipeline_build_period}
        except ValueError:
            return {'error': 'Invalid date parameters'}, 400
