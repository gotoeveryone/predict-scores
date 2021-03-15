import logging
import os

from flask import Flask

app = Flask(__name__)
logger = app.logger
logger.setLevel(logging.INFO)

if __name__ == '__main__':
    if os.environ.get('DEBUG', False):
        app.debug = True

    from api.routes import api
    app.register_blueprint(api, url_prefix='/')

    app.run()
