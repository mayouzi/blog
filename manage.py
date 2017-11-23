# coding=utf-8

__author__ = 'mayor'


from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)

manager.add_command("runserver", Server(port=5001, use_debugger=True))


if __name__ == '__main__':
    manager.run()
