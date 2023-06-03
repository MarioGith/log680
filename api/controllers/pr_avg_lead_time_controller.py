from datetime import datetime
from flask_restful import Resource
from metrics.pullrequests import PRAvgLeadTime
from database.metrics.pullrequests import PRAvgLeadTimeDB

class PRAvgLeadTimeControler(Resource):
    def get(self):
        """
        Get the average lead time for the all closed PR.
        ---
        responses:
          200:
            description: The average lead time for the all closed PR.
            schema:
              type: object
              properties:
                avg_lead_time:
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
            pr_avg_lead_time = PRAvgLeadTime.get_average_lead_time()

            PRAvgLeadTimeDB.insert_data(pr_avg_lead_time)

            return {'pr_avg_lead_time': pr_avg_lead_time}
        except ValueError:
            return {'error': 'Could not fetch from server'}, 400

