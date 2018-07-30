from app import Flask, jsonify, make_celery, liblxc, time

app = Flask(__name__)
celery = make_celery(app)


@app.route('/container/create/<name>', methods=['POST','GET'])
def container_create(name):
    task = create_container_task.delay(name)
    response = {
        'status': 'CONTAINER {} CREATION IN PROGRESS... {}'.format(name, task.id)}
    return jsonify(response)


@celery.task(exchange='lxc-client', name='{}.create_container_task'.format(__name__))
def create_container_task(name):
    time.sleep(3)
    return 'CONTAINER {} CREATED WITOUT ERRORS'.format(name)

# celery -A app.main.celery worker --loglevel=info
# docker run -d --hostname flask-rabbit --name flask-task-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
# celery amqp
