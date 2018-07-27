CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'
CELERY_BACKEND = 'redis://localhost:6379/0'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
task_annotations = {
    'tasks.reverse_string': {'rate_limit': '10/m'}
}
task_routes = {
    'tasks.reverse_string': 'low-priority',
}
