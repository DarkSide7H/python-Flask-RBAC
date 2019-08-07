#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-08-01 15:20
from flask import jsonify, g
from itsdangerous import SignatureExpired, BadSignature
from app.models.models import User, Serializer
from app import auth
from utils.response_code import Ret
import config.settings

@auth.error_handler
def error_handler():
    return jsonify(code=Ret.TOKENERR, msg='token无效')

@auth.verify_token
def verify_token(token):
    s = Serializer(config.settings.SECRET_KEY)
    try:
        data = s.loads(token)
        print(data['id'], 'data')
    except SignatureExpired:
        return False  # token过期
    except BadSignature:
        return False  # token无效
    if 'id' in data:
        g.user = User.query.filter(User.id == data['id']).first()
        return True
    return False
