#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-20 09:17

import logging
from flask import request
from flask_restplus import Namespace, Resource
from app.models.models import Menu
from app.api.controller.serializers import menu, menuElementOperation
from app.api.service.menuService import creata_menu, update_menu, delete_menu, getMenuElementOperation

log = logging.getLogger(__name__)
ns_menu = Namespace(name='menus', description='菜单相关操作')

@ns_menu.route('/getMenuElementOperationList')
class GetMenuList(Resource):
    @ns_menu.marshal_list_with(menuElementOperation)
    def get(self):
        """
        返回菜单及菜单元素和菜单操作列表
        """
        menuElementOperation = getMenuElementOperation()
        return menuElementOperation


@ns_menu.route('/getMenuList')
class GetMenuList(Resource):
    @ns_menu.marshal_list_with(menu)
    def get(self):
        """
        返回菜单列表
        """
        menus = Menu.query.all()
        return menus

@ns_menu.route('/createMenu')
class CreateMenu(Resource):
    @ns_menu.response(201, '创建菜单成功')
    @ns_menu.expect(menuElementOperation)
    def post(self):
        """
        创建菜单
        """
        data = request.json
        creata_menu(data)
        return None, 201


@ns_menu.route('/updateMenu/<string:id>')
class UpdateMenu(Resource):
    @ns_menu.response(204, '修改菜单成功')
    @ns_menu.expect(menuElementOperation)
    def put(self, id):
        """
        修改菜单
        """
        data = request.json
        update_menu(id, data)
        return None, 204

@ns_menu.route('/deleteMenu/<string:id>')
class DeleteMenu(Resource):
    def delete(self, id):
        """
        删除菜单
        """
        delete_menu(id)
        return None, 204