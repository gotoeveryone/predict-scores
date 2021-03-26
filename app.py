import logging
import os

from flask import Flask

from api.routes import api

app = Flask(__name__)
logger = app.logger
logger.setLevel(logging.INFO)

if os.environ.get('DEBUG', False):
    app.debug = True

app.register_blueprint(api, url_prefix='/')

if __name__ == '__main__':
    app.run()
