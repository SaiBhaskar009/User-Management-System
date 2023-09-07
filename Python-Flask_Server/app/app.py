from flask import Flask
from conn_db import config_database
from routes import config_routes


def Create_app():

    app = Flask(__name__)
    config_database(app)
    config_routes(app)

    from blueprints import u_blp,t_blp
    app.register_blueprint(u_blp, url_prefix='/users_data')
    app.register_blueprint(t_blp, url_prefix='/tasks_data')

    return app

APP = Create_app()

if __name__=="__main__":
    APP.run(debug=True)
