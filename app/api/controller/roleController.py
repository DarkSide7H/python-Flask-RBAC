#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-19 17:24

import logging
from flask import request
from flask_restplus import Namespace, Resource
from app.models.models import Role
from app.api.controller.serializers import role
from app.api.service.roleService import creata_role, update_role, delete_role

log = logging.getLogger(__name__)
ns_role = Namespace(name='roles', description='角色相关操作')

@ns_role.route('/getRoleList')
class GetRoleList(Resource):
    @ns_role.marshal_list_with(role)
    def get(self):
        """
        返回角色列表
        """
        roles = Role.query.all()
        return roles

@ns_role.route('/createRole')
class CreateRole(Resource):
    @ns_role.response(201, '创建角色成功')
    @ns_role.expect(role)
    def post(self):
        """
        创建角色
        """
        data = request.json
        creata_role(data)
        return None, 201


@ns_role.route('/updateRole/<string:id>')
class UpdateRole(Resource):
    @ns_role.response(204, '修改用户成功')
    @ns_role.expect(role)
    def put(self, id):
        """
        修改角色
        """
        data = request.json
        update_role(id, data)
        return None, 204

@ns_role.route('/deleteRole/<string:id>')
class DeleteRole(Resource):
    def delete(self, id):
        """
        删除角色
        """
        delete_role(id)
        return None, 204