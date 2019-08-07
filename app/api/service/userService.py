#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-19 15:25

from flask import g
from app import db
from app.models.models import User
from app.models.models import UserRole
import uuid, time

def creata_user(data):
    phone = data.get('phone')

    user = User()
    user.id = str(uuid.uuid1())
    user.username = data.get('username')
    user.nickname = data.get('nickname')
    user.password = user.hash_password(data.get('password'))
    user.phone = str(phone)
    if g.user and g.user.id and g.user.username:
        user.founder = g.user.id
        user.founder_name = g.user.username
    user.foundtime = time.strftime('%Y-%m-%d %H:%M:%S')

    db.session.add(user)
    db.session.commit()

def update_user(id, data):
    user = User.query.filter(User.id == id).one()
    # one() 仅返回一个查询结果，结果数量不足一个或多余一个时报错
    user.username = data.get('username')
    user.nickname = data.get('nickname')
    user.password = data.get('password')
    user.phone = data.get('phone')
    user.updatetime = time.strftime('%Y-%m-%d %H:%M:%S')

    db.session.add(user)
    db.session.commit()

def delete_user(id):
    user = User.query.filter(User.id == id).one()
    # one() 仅返回一个查询结果，结果数量不足一个或多余一个时报错
    db.session.delete(user)
    db.session.commit()

def bind_role(data):
    user_id = data.get('user_id')
    role_ids = data.get('role_ids')
    for role_id in role_ids:
        userRole = UserRole()
        userRole.user_id = user_id
        # 已存在，跳过
        sameUserRoleCount = UserRole.query.filter(UserRole.user_id == user_id, UserRole.role_id == role_id).count()
        if sameUserRoleCount > 0:
            continue
        userRole.status = '1'
        userRole.foundtime = time.strftime('%Y-%m-%d %H:%M:%S')
        id = str(uuid.uuid1())
        userRole.id = id
        userRole.role_id = role_id
        db.session.add(userRole)
        db.session.flush()
    db.session.commit()