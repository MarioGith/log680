from datetime import datetime
from flask_restful import Resource
from metrics.pullrequests import PRAvgComments
from database.metrics.pullrequests import PRAvgCommentsDB

class PRAvgCommentsController(Resource):
    def get(self):
        """
        Get the average comment rate on a PR.
        ---
        responses:
          200:
            description: The average comment rate on a PR.
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    pr_count:
                      type: integer
                    comments_count:
                      type: integer
                    average_comments_per_pr:
                      type: number
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
            description: Error from server.
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
        """
        try:
            avg_comments = PRAvgComments.avg_number_of_comments_per_pr()

            PRAvgCommentsDB.insert_data(avg_comments)

            return {'avg_comments': avg_comments}
        except ValueError:
            return {'error': 'Could not fetch from server'}, 400

