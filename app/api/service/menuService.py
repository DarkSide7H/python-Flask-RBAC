#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : Guohao 
# @Time : 2019-07-21 21:32 

from app import db
from app.models.models import Menu, MenuElement, MenuOperation
import uuid, time

def creata_menu(data):
    menu = Menu()

    menu.id = str(uuid.uuid1())
    menu.menu_code = data.get('menu_code')
    menu.menu_name = data.get('menu_name')
    menu.menu_icon = data.get('menu_icon')
    menu.menu_path = data.get('menu_path')
    menu.parent_id = data.get('parent_id')
    menu.sort = data.get('sort')
    menu.is_hidden = data.get('is_hidden')
    menu.status = data.get('status')
    menu.foundtime = time.strftime('%Y-%m-%d %H:%M:%S')
    elements = data.get('elements')
    operations = data.get('operations')
    for element in elements:
        menuElement = MenuElement()
        menuElement.id = str(uuid.uuid1())
        menuElement.menu_id = menu.id
        menuElement.element_code = element.get('element_code')
        menuElement.element_name = element.get('element_name')
        menuElement.foundtime = time.strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(menuElement)
        db.session.flush()
    for operation in operations:
        menuOperation = MenuOperation()
        menuOperation.id = str(uuid.uuid1())
        menuOperation.menu_id = menu.id
        menuOperation.operation_code = operation.get('operation_code')
        menuOperation.operation_name = operation.get('operation_name')
        menuOperation.foundtime = time.strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(menuOperation)
        db.session.flush()
    db.session.add(menu)
    db.session.commit()

def update_menu(id, data):
    menu = Menu.query.filter(Menu.id == id).one()
    menu.menu_code = data.get('menu_code')
    menu.menu_name = data.get('menu_name')
    menu.menu_icon = data.get('menu_icon')
    menu.menu_path = data.get('menu_path')
    menu.parent_id = data.get('parent_id')
    menu.sort = data.get('sort')
    menu.is_hidden = data.get('is_hidden')
    menu.status = data.get('status')
    menu.updatetime = time.strftime('%Y-%m-%d %H:%M:%S')
    elements = data.get('elements')
    operations = data.get('operations')
    for element in elements:
        menuElement = MenuElement()
        menuElement.id = element.get('id')
        menuElement.menu_id = menu.id
        menuElement.element_code = element.get('element_code')
        menuElement.element_name = element.get('element_name')
        menuElement.foundtime = time.strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(menuElement)
        db.session.flush()
    for operation in operations:
        menuOperation = MenuOperation()
        menuOperation.id = element.get('id')
        menuOperation.menu_id = menu.id
        menuOperation.operation_code = operation.get('operation_code')
        menuOperation.operation_name = operation.get('operation_name')
        menuOperation.foundtime = time.strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(menuOperation)
        db.session.flush()

    db.session.add(menu)
    db.session.commit()

def delete_menu(id):
    menu = Menu.query.filter(Menu.id == id).one()
    menuElements = MenuElement.query.filter(MenuElement.menu_id == id).all()
    for menuElement in menuElements:
        db.session.delete(menuElement)
        db.session.flush()
    menuOperations = MenuOperation.query.filter(MenuOperation.menu_id == id).all()
    for menuOperation in menuOperations:
        db.session.delete(menuOperation)
        db.session.flush()
    db.session.delete(menu)
    db.session.commit()

def getMenuElementOperation():
    query = db.session().query(Menu)
    # outerjoin 左连接
    query = query.outerjoin(MenuElement, MenuElement.menu_id == Menu.id).outerjoin(MenuOperation, MenuOperation.menu_id == Menu.id)
    data = query.all()
    return data
