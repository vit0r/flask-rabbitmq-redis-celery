from celery import Celery
from app import celeryconfig


def make_celery(app):
    app.config.from_object(celeryconfig)
    celery = Celery(app.import_name,
                    broker=app.config['CELERY_BROKER_URL'],
                    backend=app.config['CELERY_BACKEND']
                    )
    celery.conf.update(app.config)
    #print(celery.conf)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
