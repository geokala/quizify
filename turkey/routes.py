from turkey import app
from turkey.auth import (login_view, logout_view, register_view,
                         my_account_view)
from turkey.goal import create_goal_view
from turkey.task import (
    create_task_view,
    complete_task_view,
    complete_old_task_view,
    task_history_view,
    confirm_archive_task_view,
)
from turkey.task_break import task_break_view
from turkey.archived_tasks import archived_tasks_view
from turkey.home import home_view
from turkey.errors import not_found_view, not_allowed_view
from turkey.site_admin import site_admin_view
from turkey.version_history import version_history_view

app.add_url_rule(
    '/',
    'home',
    home_view,
    methods=['GET', 'POST'],
)
