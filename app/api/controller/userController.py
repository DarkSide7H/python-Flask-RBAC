#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-19 13:51

import logging
from flask import request, abort, Response, jsonify, g
from flask_restplus import Namespace, Resource, fields
from app.api import api

from app.models.models import User
from app.api.controller.serializers import user, userBindRole, page_of_users
from app.api.controller.parsers import pagination_arguments
from app.api.service.userService import creata_user, update_user, delete_user, bind_role
from utils.token_auth import auth, verify_token
from utils.response_code import Ret

log = logging.getLogger(__name__)
# 定义命名空间
ns_user = Namespace(name='users', description='用户相关操作')

@ns_user.route('/checkToken')
class checkToken(Resource):
    def get(self):
        """
        校验token是否有效
        :return:
        """
        data = request.headers.get('Token')
        bToken = verify_token(data)
        if bToken:
            return jsonify(code=Ret.SUCCESS, msg='token 有效')
        else:
            return jsonify(code=Ret.FAILURE, msg='token 无效')


@ns_user.route('/login')
class login(Resource):
    # 请求参数
    login = api.model('Login', {
        'username': fields.String(required=True, description='用户名'),
        'password': fields.String(required=True, description='密码')
    })
    @ns_user.expect(login)
    def post(self):
        """
        登录，获取用户信息以及生成token
        :return:
        """
        data = request.json
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter(User.username == username).first()
        if User.verify_password(user, password):
            # 生成token
            token = user.generate_auth_token()
            return jsonify(code=Ret.SUCCESS, msg="登录成功", data={'token': token.decode('utf-8'), 'name': user.username})
        else:
            return jsonify(code=Ret.FAILURE, msg="密码错误")

@ns_user.route('/logout')
class logout(Resource):
    @auth.login_required
    def logout(self):
        return jsonify(Ret.SUCCESS, msg="退出成功")


@ns_user.route('/getUserList')
class GetUserList(Resource):
    # RESTFul 扩展集成 decorators，注入视图装饰器
    # decorators = [auth.login_required]
    # @ns_user.marshal_list_with(user)
    @auth.login_required
    def get(self):
        """
        返回用户列表.
        """
        users = User.query.all()
        user_list = []
        for user in users:
            user_list.append(user.to_dict())

        data = user_list
        return jsonify(code=Ret.SUCCESS, msg="查询成功", data=data)

@ns_user.route('/getUserListForPage')
class GetUserListForPage(Resource):
    @ns_user.expect(pagination_arguments)
    # @ns_user.marshal_with(page_of_users)
    def get(self):
        """
        分页返回用户列表.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 2)
        print(per_page, 'per_page')

        users_query = User.query
        users_page = users_query.filter(User.founder == g.user.id).paginate(page, per_page, error_out=False)
        user_list = []
        for user in users_page.items:
            user_list.append(user.to_dict())

        data = {
            'users': user_list,
            'total': users_page.total,
            'pages': users_page.pages,
            'page': users_page.page
        }
        return jsonify(code=Ret.SUCCESS, msg="查询成功", data=data)

@ns_user.route('/createUser')
class CretaUser(Resource):
    # @ns_user.response(201, '创建用户成功')
    # @ns_user.expect(user)
    user = api.model('Model User', {
        'username': fields.String(required=True, description='用户名'),
        'nickname': fields.String(required=False, description='昵称'),
        'password': fields.String(required=True, description='密码'),
        'phone': fields.String(required=False, description='手机号码'),
        'email': fields.String(required=False, description=''),
        'is_children': fields.Integer(required=False, description=''),
        'parent_id': fields.String(required=False, description='')
    })

    @ns_user.expect(user)
    @auth.login_required
    def post(self):
        """
        创建用户
        """
        data = request.json
        if data.get('password') == '' or data.get('password') is None:
            # abort() 立即停止视图函数的执行，并且把相对应的信息返回到前端中
            # abort(Response("密码不能为空"))
            return jsonify(code=Ret.FAILURE, msg="密码不能为空")
        creata_user(data)

        # return None, 201
        return jsonify(code=Ret.SUCCESS, msg="创建成功")

@ns_user.route('/updateUser/<string:id>')
class UpdateUser(Resource):
    @ns_user.response(204, '修改用户成功')
    @ns_user.expect(user)
    def put(self, id):
        """
        修改用户
        """
        data = request.json
        update_user(id, data)
        return None, 204

@ns_user.route('/deleteUser/<string:id>')
class DeleteUser(Resource):
    def delete(self, id):
        """
        删除用户
        """
        delete_user(id)
        return None, 204

@ns_user.route('/bindRole')
class BindRole(Resource):
    @ns_user.response(204, '绑定用户角色')
    @ns_user.expect(userBindRole)
    def post(self):
        """
        用户绑定角色
        :return:
        """
        data = request.json
        bind_role(data)
        return None, 204