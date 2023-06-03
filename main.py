from datetime import datetime

from metrics.kanban import IssueLeadTime, IssuesCompletedWithinPeriod, IssuesActiveByColumn
from metrics.pullrequests import PRLinesCode, PRAvgLeadTime
from metrics.pullrequests import PRMergedInPeriod
from metrics.pullrequests import PRAvgDelayUntilComment
from metrics.pullrequests import PRAvgComments
from metrics.kanban import IssueLeadTimePeriod
from metrics.snapshot import IssuesSnapshot
from datetime import datetime

print("Métrique : Lead time pour les tâches")
issue_no = 1
IssueLeadTime.get_lead_time_of_issue(issue_no)

print("---")

print("Métrique : Lead time pour les tâches terminées dans une période donnée")
IssueLeadTimePeriod.get_issue_lead_time_within_period(datetime(year=2023, month=5, day=10),
                                                      datetime(year=2023, month=5, day=20))

print("---")

print("Métrique : Nombre de tâches actives pour une colonne donnée")
IssuesActiveByColumn.get_number_of_active_issues_by_column("Backlog")

print("---")

print("Métrique : Nombre de tâches complétées pour une période donnée")
IssuesCompletedWithinPeriod.get_number_issues_completed_within_period(datetime(year=2023, month=5, day=10),
                                                                      datetime(year=2023, month=5, day=25))

print("---")

print("Métrique : Lead time moyen de tous les PRs")
PRAvgLeadTime.get_average_lead_time()

print("---")

print("Métrique : Total des PR fusionnées dans une période donnée")
PRMergedInPeriod.get_pr_lead_time_in_period(datetime(year=2023, month=5, day=18), datetime(year=2023, month=5, day=18))

print("---")

print("Métrique : Nombre de lignes de code par PR")
PRLinesCode.get_pr_lines_code_in_period(datetime(year=2023, month=5, day=18), datetime(year=2023, month=5, day=19))

print("---")

print("Métrique : Délai moyen jusqu'au premier commentaire sur le PR")
PRAvgDelayUntilComment.get_pr_avg_delay_until_comment()

print("---")

print("Métrique : Moyenne de commentaires par PR")
PRAvgComments.avg_number_of_comments_per_pr()

print("---")

print ("Métrique Snapshot")

# Our project: PVT_kwHOAbaNX84AQEYe
# Liquibase project: PVT_kwDOAAaxFM4AAXda (https://github.com/liquibase/liquibase)
# Uptime Kuma: PVT_kwHOABRlys4AF-jf  (https://github.com/louislam/uptime-kuma)
project_id = "PVT_kwHOAbaNX84AQEYe"

# Our project: repository(owner: "Tzuyunii", name: "metrics-grp2-eq10-e23")
#               projectV2(number: 2)
# Liquibase project: repository(owner: "liquibase", name: "liquibase")
#               projectV2(number: 3)
# Uptime Kuma: repository(owner: "louislam", name: "uptime-kuma") {
#               projectV2(number: 4)
repo_owner = "Tzuyunii"
repo_name = "metrics-grp2-eq10-e23"
repo_project_number = 2

IssuesSnapshot.get_snapshot(project_id, repo_owner, repo_name, repo_project_number)
