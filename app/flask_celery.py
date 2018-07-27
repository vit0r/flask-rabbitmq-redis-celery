from celery import Celery
from app import celeryconfig


def make_celery(app):
    app.config.from_object(celeryconfig)
    celery = Celery(app.import_name)
    celery.config_from_object(celeryconfig)
    print(celery.conf)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
