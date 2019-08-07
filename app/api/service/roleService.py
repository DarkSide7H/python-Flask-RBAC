#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-19 17:32 

from app import db
from app.models.models import Role
import uuid, time

def creata_role(data):
    role_name = data.get('role_name')

    role = Role(role_name)

    role.id = str(uuid.uuid1())
    role.role_desc = data.get('role_desc')
    role.status = data.get('status')

    role.foundtime = time.strftime('%Y-%m-%d %H:%M:%S')

    db.session.add(role)
    db.session.commit()

def update_role(id, data):
    role = Role.query.filter(Role.id == id).one()
    role.role_name = data.get('role_name')
    role.role_desc = data.get('role_desc')
    role.status = data.get('status')
    role.updatetime = time.strftime('%Y-%m-%d %H:%M:%S')

    db.session.add(role)
    db.session.commit()

def delete_role(id):
    role = Role.query.filter(Role.id == id).one()
    db.session.delete(role)
    db.session.commit()