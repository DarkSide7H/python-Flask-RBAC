#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-19 13:47

import logging
import traceback

from flask import Blueprint
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

import config.settings

log = logging.getLogger(__name__)

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    app=api_blueprint,
    version='1.0.0',
    title='Swagger',
    description='''Flask,Blueprint, Flask-Restplus and Swagger Api example， 
    参考文案：http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
    ''',
    contact='guohao',
    contact_url='',
    contact_email='511721582@qq.com',
)

# @api.errorhandler装饰器覆盖默认错误处理程序
@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not config.settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': '未找到该数据.'}, 404



