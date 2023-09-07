from flask import Blueprint

u_blp = Blueprint('users', __name__)

t_blp = Blueprint('tasks', __name__)


@u_blp.route('/hello')
def Hello_User():
    return "Hello User, This is a Test Run"

@t_blp.route('/t_hello')
def Hello_Tasks():
    return "Hello, This is Introduction to Tasks"