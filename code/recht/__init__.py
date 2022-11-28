import os

from flask import (Flask, render_template)
from flask import g

def create_app(test_config=None):

    FILE_FOLDER = './upload'
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='1209jawdnm@/()=94adwkawd',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    import routes
    from flask import request

    @app.before_request
    def log_request_info():
        app.logger.debug(f'Body: {request.form}')
        app.logger.debug(f'Data: {request.get_data()}')
        app.logger.debug(f'Files: {request.files}')



    app.register_blueprint(routes.bp)
    app.config['UPLOAD_FOLDER'] = FILE_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
    app.config['DEFAULT_PARSERS'] = [
    'flask.ext.api.parsers.JSONParser',
    'flask.ext.api.parsers.URLEncodedParser',
    'flask.ext.api.parsers.MultiPartParser'
]

    return app
