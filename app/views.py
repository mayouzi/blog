# coding=utf-8

__author__ = 'mayor'


from app import app
from flask import render_template


@app.route('/')
def index():
    """
        home page
    :return:
    """
    kwargs = dict()
    kwargs['title'] = 'Welcome to mayor`s blog'
    kwargs['name'] = 'mayor'
    kwargs['city'] = 'Beijing (China)'

    return render_template('home/index.html', **kwargs)