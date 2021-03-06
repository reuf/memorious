from memorious.core import manager, celery as app
from memorious.logic.context import handle  # noqa


@app.task
def process_schedule():
    manager.run_scheduled()
