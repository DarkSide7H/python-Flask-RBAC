# coding: utf-8
# sqlacodegen 'mysql+pymysql://root:123456@localhost:3306/testDB?charset=utf8' > app/models/models.py
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
# 加密解密密码的库
from passlib.apps import custom_app_context
import config.settings
# URL安全序列化工具
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
# from sqlalchemy.ext.declarative import declarative_db.Model
# 
# Base = declarative_db.Model()
# metadata = Base.metadata
from app import db

class Group(db.Model):
    __tablename__ = 'group'

    id = Column(String(128), primary_key=True)
    groupname = Column(String(128))
    parent_id = Column(String(128))
    parent_name = Column(String(128))
    status = Column(String(32))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)

    def __init__(self):
        self


class GroupRole(db.Model):
    __tablename__ = 'group_role'

    id = Column(String(128), primary_key=True)
    group_id = Column(String(128))
    role_id = Column(String(128))
    status = Column(String(32))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)

    def __init__(self):
        self


class Menu(db.Model):
    __tablename__ = 'menu'

    id = Column(String(128), primary_key=True)
    menu_code = Column(String(64), unique=True)
    menu_name = Column(String(128))
    menu_icon = Column(String(128))
    menu_path = Column(String(128))
    parent_id = Column(String(128))
    sort = Column(INTEGER(11))
    is_hidden = Column(TINYINT(4), server_default=text("'0'"))
    status = Column(String(32))
    state = Column(TINYINT(4))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)
    elements = db.relationship('MenuElement', backref='', lazy='dynamic')
    operations = db.relationship('MenuOperation', backref='', lazy='dynamic')

    def __init__(self):
        self

class MenuElement(db.Model):
    __tablename__ = 'menu_element'

    id = Column(String(128), primary_key=True)
    element_code = Column(String(128))
    element_name = Column(String(128))
    menu_id = Column(String(128), db.ForeignKey(Menu.id))
    state = Column(TINYINT(4))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)

    def __init__(self):
        self


class MenuOperation(db.Model):
    __tablename__ = 'menu_operation'

    id = Column(String(128), primary_key=True)
    operation_code = Column(String(128))
    operation_name = Column(String(128))
    menu_id = Column(String(128), db.ForeignKey(Menu.id))
    state = Column(TINYINT(4))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)

    def __init__(self):
        self


class Permission(db.Model):
    __tablename__ = 'permission'

    id = Column(String(128), primary_key=True)
    type = Column(String(128))
    target_id = Column(String(128))
    status = Column(String(32))
    state = Column(TINYINT(4))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)

    def __init__(self):
        self


class Role(db.Model):
    __tablename__ = 'role'

    id = Column(String(128), primary_key=True)
    role_name = Column(String(128))
    role_desc = Column(String(500))
    status = Column(String(32))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)

    def __init__(self, role_name):
        self.role_name = role_name


class RolePermission(db.Model):
    __tablename__ = 'role_permission'

    id = Column(String(128), primary_key=True)
    role_id = Column(String(128))
    permission_id = Column(String(128))
    status = Column(String(32))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)

    def __init__(self):
        self


class User(db.Model):
    __tablename__ = 'user'

    id = Column(String(128), primary_key=True, unique=True)
    username = Column(String(128))
    nickname = Column(String(128))
    password = Column(String(128))
    phone = Column(String(32))
    email = Column(String(128))
    is_children = Column(INTEGER(1))
    parent_id = Column(String(128))
    status = Column(String(32))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)

    def __init__(self):
        self

    # 密码加密
    def hash_password(self, password):
        self.password = custom_app_context.encrypt(password)
        return self.password

    # 密码解析
    def verify_password(self, password):
        return custom_app_context.verify(password, self.password)

    # 获取token，有效时间
    def generate_auth_token(self, expiration=config.settings.TOKEN_EXPIRATION):
        s = Serializer(config.settings.SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id, 'username': self.username, 'nickname': self.nickname, 'phone': self.phone})

    # @staticmethod
    # def verify_auth_token(token):
    #     s = Serializer(config.settings.SECRET_KEY)
    #     try:
    #         data = s.loads(token)
    #         print(data)
    #     except SignatureExpired:
    #         print('token过期')
    #         return False  # token过期
    #     except BadSignature:
    #         print('token无效')
    #         return False  # token无效
    #     user = User.query.get(data['id'])
    #     print(user)
    #     return True
    def to_dict(self):
        user_info = {
            'id': self.id,
            'username': self.username,
            'phone': self.phone
        }
        return user_info

class UserAuth(db.Model):
    __tablename__ = 'user_auths'

    id = Column(String(128), primary_key=True)
    user_id = Column(String(128))
    third_type = Column(String(32))
    third_key = Column(String(128))
    status = Column(String(32))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)
    founder = Column(String(128))

    def __init__(self):
        self


class UserGroup(db.Model):
    __tablename__ = 'user_group'

    id = Column(String(128), primary_key=True)
    user_id = Column(String(128))
    group_id = Column(String(128))
    status = Column(String(32))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)

    def __init__(self):
        self


class UserRole(db.Model):
    __tablename__ = 'user_role'

    id = Column(String(128), primary_key=True)
    user_id = Column(String(128))
    role_id = Column(String(128))
    status = Column(String(32))
    founder = Column(String(128))
    founder_name = Column(String(128))
    foundtime = Column(DateTime)
    updater = Column(String(128))
    updater_name = Column(String(128))
    updatetime = Column(DateTime)

    def __init__(self):
        self
