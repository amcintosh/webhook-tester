import base64
import hmac
import hashlib
import json
import logging
import os

from flask import Flask, request

log = logging.getLogger(__name__)


def signature_match(request):
    verifier = os.getenv('verifier')
    signature = request.headers.get('X-FreshBooks-Hmac-SHA256')
    if not verifier:
        log.warn('no verifier specifief')
        return False

    if not signature:
        log.warn('no signature in request')
        return False

    log.warn(type(json.dumps(request.form)))
    log.warn(json.dumps(request.form))
    dig = hmac.new(
        verifier.encode('utf-8'),
        msg=json.dumps(request.form).encode('utf-8'),
        digestmod=hashlib.sha256
    ).digest()
    sig = base64.b64encode(dig).decode()
    log.info('Received signature: %s', signature)
    log.info('Calculated signature: %s', sig)
    return signature == sig


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

        log.info('signature_match: %s', signature_match(request))

        return resp

    @app.route('/listen_fail', methods=['GET', 'POST'])
    def listen_fail():
        return listen(), 404

    return app
