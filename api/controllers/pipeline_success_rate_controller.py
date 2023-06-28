from datetime import datetime
from flask_restful import Resource
from metrics.pipeline import PipelineSuccessRate
from flask import request
from database.metrics.kanban import IssueLeadTimeDB
from psycopg2.errorcodes import UNIQUE_VIOLATION
import psycopg2

class PipelineSuccessRateController(Resource):
    def get(self):
        """
        Get the number of build.
        ---
        responses:
          200:
            description: The number of build.
            schema:
              type: object
              properties:
                success_count:
                  type: string
                failure_count:
                  type: string
                success_list:
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
                          status:
                            type: string
                          conclusion:
                            type: string
                failure_list:
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
                          status:
                            type: string
                          conclusion:
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
            pipeline_success_rate = PipelineSuccessRate.get_success_rate()
            # try:
            #     IssueLeadTimeDB.insert_data(issue_lead_time)
            # except psycopg2.errors.lookup(UNIQUE_VIOLATION):
            #     None
            # except TypeError:
            #     return {'error': 'This number is not an issue'}
            #
            # if pipeline_execution_time is None:
            #     return {'error': 'Pipeline is None'}, 400

            return {'pipeline_success_rate': pipeline_success_rate}
        except ValueError:
            return {'error': 'Error in the fetch'}, 400
