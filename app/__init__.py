#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author : Guohao
# @Time : 2019-07-19 13:06

# Create a Flask WSGI application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
# 读取配置
app.config.from_object('config.settings')

# flask的跨域解决
CORS(app)

# 数据库初始化
db = SQLAlchemy(app)
# 验证的初始化
auth = HTTPTokenAuth(scheme='Bearer')


from app.api import api, api_blueprint
from app.api.controller.userController import ns_user
from app.api.controller.roleController import ns_role
from app.api.controller.groupController import ns_group
from app.api.controller.menuController import ns_menu

api.add_namespace(ns_user)
api.add_namespace(ns_role)
api.add_namespace(ns_group)
api.add_namespace(ns_menu)
app.register_blueprint(blueprint=api_blueprint)

from app.site.routes import site_blueprint
app.register_blueprint(blueprint=site_blueprint)

db.create_all()