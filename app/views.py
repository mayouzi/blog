# coding=utf-8

__author__ = 'mayor'


from app import app
from flask import render_template


@app.route('/')
def index():
    home_title = 'Welcome to mayor`s blog'
    html_file = 'welcome.html'

    return render_template(html_file, title=home_title)