from app import Flask, jsonify, make_celery, liblxc, time

app = Flask(__name__)
celery = make_celery(app)


@app.route('/container/create/<name>')
def container_create(name):
    create_container_task.delay(name)
    response = {
        'status': 'CONTAINER {} CREATION IN PROGRESS...'.format(name)}
    return jsonify(response)


@celery.task(name='{}.create_container_task'.format(__name__))
def create_container_task(name):
    print('PROCESSING')
    time.sleep(3)
    return 'CONTAINER {} CREATED WITOUT ERRORS'.format(name)

#celery -A app.main.celery worker --loglevel=info
#docker run -d --hostname flask-rabbit --name flask-task-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management