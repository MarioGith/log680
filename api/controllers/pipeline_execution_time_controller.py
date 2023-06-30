from datetime import datetime
from flask_restful import Resource
from metrics.pipeline import PipelineExecutionTime
from flask import request
from database.metrics.kanban import IssueLeadTimeDB
from psycopg2.errorcodes import UNIQUE_VIOLATION
import psycopg2

class PipelineExecutionTimeController(Resource):
    def get(self):
        """
        Get the execution time.
        ---
        parameters:
          - name: pipeline_name
            in: query
            type: string
            required: true
            description: The name of the pipeline.
        responses:
          200:
            description: The name of the pipeline.
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
        pipeline_name = request.args.get('pipeline_name')

        try:
            pipeline_execution_time = PipelineExecutionTime.get_execution_time_pipeline(pipeline_name)
            # try:
            #     IssueLeadTimeDB.insert_data(issue_lead_time)
            # except psycopg2.errors.lookup(UNIQUE_VIOLATION):
            #     None
            # except TypeError:
            #     return {'error': 'This number is not an issue'}
            #
            # if pipeline_execution_time is None:
            #     return {'error': 'Pipeline is None'}, 400

            return {'pipeline_execution_time': pipeline_execution_time}
        except ValueError:
            return {'error': 'Invalid  parameter'}, 400
