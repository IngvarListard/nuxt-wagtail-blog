from backend.core.celery import app
from backend.users.services.notifications import SendUserPassword


@app.task(
    name='task_with_uncaught_exception',
    max_retries=3,
    autoretry_for=(Exception,),
    throw=(ValueError,),
    default_retry_delay=3,
    ignore_result=True
)
def send_user_password(email, password, **kwargs):
    SendUserPassword(email, password).execute()
