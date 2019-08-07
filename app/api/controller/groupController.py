#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-20 08:41 

import logging
from flask import request
from flask_restplus import Namespace, Resource
from app.models.models import Group
from app.api.controller.serializers import group, groupBindRole
from app.api.service.groupService import create_group, update_group, delete_group, bind_role

log = logging.getLogger(__name__)
ns_group = Namespace(name='groups', description='用户组相关操作')

@ns_group.route('/getGroupList')
class GetGroupList(Resource):
    @ns_group.marshal_list_with(group)
    def get(self):
        """
        返回用户组列表
        """
        groups = Group.query.all()
        return groups

@ns_group.route('/createGroup')
class CreateGroup(Resource):
    @ns_group.response(201, '创建用户组成功')
    @ns_group.expect(group)
    def post(self):
        """
        创建用户组
        """
        data = request.json
        create_group(data)
        return None, 201


@ns_group.route('/updateGroup/<string:id>')
class UpdateGroup(Resource):
    @ns_group.response(204, '修改用户成功')
    @ns_group.expect(group)
    def put(self, id):
        """
        修改用户组
        """
        data = request.json
        update_group(id, data)
        return None, 204

@ns_group.route('/deleteGroup/<string:id>')
class DeleteGroup(Resource):
    def delete(self, id):
        """
        删除用户组
        """
        delete_group(id)
        return None, 204

@ns_group.route('/bindRole')
class BindRole(Resource):
    @ns_group.response(204, '绑定用户角色')
    @ns_group.expect(groupBindRole)
    def post(self):
        """
        用户组绑定角色
        :return:
        """
        data = request.json
        bind_role(data)
        return None, 204