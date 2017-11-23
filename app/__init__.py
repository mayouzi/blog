# -*- coding: utf-8 -*-

__author__ = 'mayor'

import os

from flask import Flask

# templates & static  path
template_folder = os.path.abspath(os.path.join(os.getcwd(), "templates"))
static_folder = os.path.abspath(os.path.join(os.getcwd(), "static"))

# 创建Flask类的实例
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

# 从config.py读入配置
app.config.from_object('conf.config')

# 这个import语句放在这里, 防止views, models import发生循环import
from app import views, models


