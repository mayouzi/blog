# -*- coding: utf-8 -*-

__author__ = 'mayor'


from flask import Flask

# 创建Flask类的实例
app = Flask(__name__)

# 从config.py读入配置
app.config.from_object("config")

# 这个import语句放在这里, 防止views, models import发生循环import
from app import views, models


