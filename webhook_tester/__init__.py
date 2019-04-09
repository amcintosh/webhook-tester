import logging
from flask import Flask, request

log = logging.getLogger(__name__)


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        return 'Running'

    @app.route('/listen', methods=['GET', 'POST'])
    def listen():
        resp = 'Received: {}. -- '.format(request.full_path)
        log.info(resp)
        log.info('parameters: ')
        for key in request.form:
            arg = '{}:{} '.format(key, request.form[key])
            log.info(arg)
            resp += arg

        log.info('headers: ')
        for arg in request.headers:
            log.info(arg)

        return resp

    @app.route('/listen_fail', methods=['GET', 'POST'])
    def listen_fail():
        return listen(), 404

    return app
