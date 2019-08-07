#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-19 14:46

# 接口输入输出
from flask_restplus import fields
from app.api import api

user = api.model('Model User', {
    'id': fields.String(readOnly=False, description='用户id'),
    'username': fields.String(required=False, description='用户名'),
    'nickname': fields.String(required=False, description='昵称'),
    'password': fields.String(required=False, description='密码'),
    'phone': fields.String(required=False, description='手机号码'),
    'email': fields.String(required=False, description=''),
    'is_children': fields.Integer(required=False, description=''),
    'parent_id': fields.String(required=False, description=''),
    'status': fields.String(required=False, description=''),
    'founder': fields.String(required=False, description=''),
    'founder_name': fields.String(required=False, description=''),
    'foundtime': fields.DateTime(required=False, description=''),
    'updater': fields.String(required=False, description=''),
    'updater_name': fields.String(required=False, description=''),
    'updatetime': fields.DateTime(required=False, description='')
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_users = api.inherit('Page of user', pagination, {
    'items': fields.List(fields.Nested(user))
})

role = api.model('Model Role', {
    'id': fields.String(),
    'role_name': fields.String(),
    'role_desc': fields.String(),
    'status': fields.String(),
    'founder': fields.String(),
    'founder_name': fields.String(),
    'foundtime': fields.DateTime(),
    'updater': fields.String(),
    'updater_name': fields.String(),
    'updatetime': fields.DateTime()
})

userBindRole = api.model('Model userBindRole', {
    'user_id': fields.String(),
    'role_ids': fields.List(fields.String)
})

group = api.model('Model Group', {
    'id': fields.String(),
    'groupname': fields.String(),
    'parent_id': fields.String(),
    'parent_name': fields.String(),
    'status': fields.String(),
    'founder': fields.String(),
    'founder_name': fields.String(),
    'foundtime': fields.DateTime(),
    'updater': fields.String(),
    'updater_name': fields.String(),
    'updatetime': fields.DateTime()
})

groupBindRole = api.model('Model groupBindRole', {
    'group_id': fields.String(),
    'role_ids': fields.List(fields.String)
})

menu = api.model('Model Menu', {
    'id': fields.String(),
    'menu_code': fields.String(),
    'menu_name': fields.String(),
    'menu_icon': fields.String(),
    'menu_path': fields.String(),
    'parent_id': fields.String(),
    'sort': fields.Integer(),
    'is_hidden': fields.Integer(),
    'status': fields.String(),
    'state': fields.Integer(),
    'founder': fields.String(),
    'founder_name': fields.String(),
    'foundtime': fields.DateTime(),
    'updater': fields.String(),
    'updater_name': fields.String(),
    'updatetime': fields.DateTime()
})

menuElement = api.model('Model menuElement', {
    'id': fields.String(),
    'element_code': fields.String(),
    'element_name': fields.String()
})
menuOperation = api.model('Model menuOperation', {
    'id': fields.String(),
    'operation_code': fields.String(),
    'operation_name': fields.String()
})

# 模型继承
menuElementOperation = api.inherit('Model menuElementOperation',  menu, {
    'elements': fields.List(fields.Nested(menuElement)),
    'operations': fields.List(fields.Nested(menuOperation))
})