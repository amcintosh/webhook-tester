import logging
import os

from webhook_tester import create_app


logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Use this for development only. Supports hot reloading
app = create_app()
app.debug = True

port = os.environ['PORT']
app.run(host='0.0.0.0', port=int(port))
