from api.controllers.issue_lead_time_controller import IssueLeadTimeController
from api.controllers.issue_lead_time_period_controller import IssueLeadTimePeriodController
from api.controllers.issues_completed_within_period_controller import IssuesCompletedWithinPeriodController
from api.controllers.isues_actives_by_column_controller import IssuesActiveByColumnController
from api.controllers.pr_avg_delay_until_comment_controller import PRAvgDelayUntilCommentController
from api.controllers.pr_lines_code_controller import PRLinesCodeController
from api.controllers.pr_merged_in_period_controller import PRMergedInPeriodController
from api.controllers.pr_avg_lead_time_controller import PRAvgLeadTimeControler
from api.controllers.pr_avg_comments import PRAvgCommentsController
from api.controllers.issue_snapshot_controller import IssueSnapshotController
from api.controllers.pipeline_execution_time_controller import PipelineExecutionTimeController
from api.controllers.pipeline_number_build_controller import PipelineNumberBuildController
from api.controllers.pipeline_build_period import PipelineBuildPeriodController
from api.controllers.pipeline_success_rate_controller import PipelineSuccessRateController

def register_routes(api):
    api.add_resource(IssueLeadTimeController, '/IssueLeadTime/<int:issue_no>')
    api.add_resource(IssueLeadTimePeriodController, '/IssueLeadTimePeriod')
    api.add_resource(IssuesCompletedWithinPeriodController, '/IssuesCompletedWithinPeriod')
    api.add_resource(IssuesActiveByColumnController, '/IssuesActiveByColumn')
    api.add_resource(PRAvgCommentsController, '/PRAvgComments')
    api.add_resource(PRAvgDelayUntilCommentController, '/PRAvgDelayUntilComment')
    api.add_resource(PRLinesCodeController, '/PRLinesCode')
    api.add_resource(PRMergedInPeriodController, '/PRMergedInPeriod')
    api.add_resource(PRAvgLeadTimeControler, '/PRAvgLeadTime')
    api.add_resource(IssueSnapshotController, '/metric/snapshot/')
    api.add_resource(PipelineExecutionTimeController, '/PipelineExecutionTime')
    api.add_resource(PipelineNumberBuildController, '/PipelineNumberBuild')
    api.add_resource(PipelineBuildPeriodController, '/PipelineBuildPeriod')
    api.add_resource(PipelineSuccessRateController, '/PipelineSuccessRate')