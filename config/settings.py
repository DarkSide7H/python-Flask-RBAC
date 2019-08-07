#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-19 13:01

# Global App setting

# Flask settings
FLASK_DEBUG = True
SECRET_KEY = '123456'

# MySQL 数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/testDB?charset=utf8'
SQLALCHEMY_ENCODING = 'utf-8'
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 屏蔽 sql alchemy 的 FSADeprecationWarning

# Flask-restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
ERROR_404_HELP = False

# Token 时效
TOKEN_EXPIRATION = 60 * 60 * 24

