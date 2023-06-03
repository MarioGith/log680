from datetime import datetime
from flask_restful import Resource
from metrics.pullrequests import PRAvgDelayUntilComment
from database.metrics.pullrequests import PRAvgDelayUntilCommentDB

class PRAvgDelayUntilCommentController(Resource):
    def get(self):
        """
        Get the average delay time for the first comment on a PR.
        ---
        responses:
          200:
            description: The average delay time for the first comment on a PR
            schema:
              type: object
              properties:
                avg_time_for_first_comment:
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
            description: Error from server.
            schema:
              type: object
              properties:
                error:
                  type: string
        """
        try:
            avg_delay_time = PRAvgDelayUntilComment.get_pr_avg_delay_until_comment()

            PRAvgDelayUntilCommentDB.insert_data(avg_delay_time)

            return {'avg_delay_time_until_comment': avg_delay_time}
        except ValueError:
            return {'error': 'Could not fetch from server'}, 400


