#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-20 08:44 


from app import db
from app.models.models import Group, GroupRole
import uuid, time

def create_group(data):
    group = Group()

    group.id = str(uuid.uuid1())
    group.groupname = data.get('groupname')
    group.parent_id = data.get('parent_id')
    group.parent_name = data.get('parent_name')
    group.status = data.get('status')
    group.foundtime = time.strftime('%Y-%m-%d %H:%M:%S')

    db.session.add(group)
    db.session.commit()

def update_group(id, data):
    group = Group.query.filter(Group.id == id).one()
    group.groupname = data.get('groupname')
    group.parent_id = data.get('parent_id')
    group.parent_name = data.get('parent_name')
    group.status = data.get('status')
    group.updatetime = time.strftime('%Y-%m-%d %H:%M:%S')

    db.session.add(group)
    db.session.commit()

def delete_group(id):
    group = Group.query.filter(Group.id == id).one()
    db.session.delete(group)
    db.session.commit()

def bind_role(data):
    group_id = data.get('group_id')
    role_ids = data.get('role_ids')
    for role_id in role_ids:
        groupRole = GroupRole()
        groupRole.group_id = group_id
        # 已存在，跳过
        sameGroupRoleCount = GroupRole.query.filter(GroupRole.group_id == group_id, GroupRole.role_id == role_id).count()
        if sameGroupRoleCount > 0:
            continue
        groupRole.status = '1'
        groupRole.foundtime = time.strftime('%Y-%m-%d %H:%M:%S')
        id = str(uuid.uuid1())
        groupRole.id = id
        groupRole.role_id = role_id
        db.session.add(groupRole)
        db.session.flush()
    db.session.commit()