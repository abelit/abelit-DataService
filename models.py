# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2020/03/21 08:31:10
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


from db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


# 用户与角色多对多关系
users_roles = db.Table('users_roles',
                       db.Column('id', db.Integer, primary_key=True,
                                  autoincrement=True),
                       db.Column('userid',db.Integer, db.ForeignKey(
                           'users.id'), primary_key=True),
                       db.Column('roleid',db.Integer, db.ForeignKey(
                           'roles.id'), primary_key=True),
                       db.Column('created_timestamp', db.DateTime,
                                 nullable=False, default=datetime.now),
                       db.Column('updated_timestamp', db.DateTime,
                                 nullable=False,  onupdate=datetime.now, default=datetime.now)
                       )

# 用户与权限多对多关系
users_permissions = db.Table('users_permissions',
                             db.Column('id', db.Integer,
                                       primary_key=True,  autoincrement=True),
                             db.Column('userid', db.Integer, db.ForeignKey(
                                 'users.id'), primary_key=True),
                             db.Column('permissionid', db.Integer, db.ForeignKey(
                                 'permissions.id'), primary_key=True),
                             db.Column('created_timestamp', db.DateTime,
                                       nullable=False, default=datetime.now),
                             db.Column('updated_timestamp', db.DateTime,
                                       nullable=False,  onupdate=datetime.now, default=datetime.now)
                             )

# 用户组和角色多对多关系
groups_roles = db.Table('groups_roles',
                        db.Column('id',  db.Integer, primary_key=True,
                                   autoincrement=True),
                        db.Column('groupid', db.Integer, db.ForeignKey(
                            'groups.id'), primary_key=True),
                        db.Column('roleid', db.Integer, db.ForeignKey(
                            'roles.id'), primary_key=True),
                        db.Column('created_timestamp', db.DateTime,
                                  nullable=False, default=datetime.now),
                        db.Column('updated_timestamp', db.DateTime,
                                  nullable=False, onupdate=datetime.now, default=datetime.now)
                        )

# 用户组与权限多对多关系
groups_permissions = db.Table('groups_permissions',
                              db.Column('id',  db.Integer,
                                        primary_key=True,  autoincrement=True),
                              db.Column('groupid', db.Integer, db.ForeignKey(
                                  'groups.id'), primary_key=True),
                              db.Column('permissionid', db.Integer, db.ForeignKey(
                                  'permissions.id'), primary_key=True),
                              db.Column('created_timestamp', db.DateTime,
                                        nullable=False, default=datetime.now),
                              db.Column('updated_timestamp', db.DateTime,
                                        nullable=False,  onupdate=datetime.now, default=datetime.now)
                              )

# 角色与权限多对多关系
roles_permissions = db.Table('roles_permissions',
                             db.Column('id',  db.Integer,
                                       primary_key=True,  autoincrement=True),
                             db.Column('roleid', db.Integer, db.ForeignKey(
                                 'roles.id'), primary_key=True),
                             db.Column('permissionid', db.Integer, db.ForeignKey(
                                 'permissions.id'), primary_key=True),
                             db.Column('created_timestamp', db.DateTime,
                                       nullable=False, default=datetime.now),
                             db.Column('updated_timestamp', db.DateTime,
                                       nullable=False, onupdate=datetime.now, default=datetime.now)
                             )

# 数据包与权限多对多关系
menus_permissions = db.Table('menus_permissions',
                                db.Column('id', db.Integer,
                                          primary_key=True,  autoincrement=True),
                                db.Column('menusid', db.Integer, db.ForeignKey(
                                    'menus.id'), primary_key=True),
                                db.Column('permissionid', db.Integer, db.ForeignKey(
                                    'permissions.id'), primary_key=True),
                                db.Column('action', db.Integer,
                                          doc='1: view,2:create,3,edit,4.delete'),
                                db.Column('created_timestamp', db.DateTime,
                                          nullable=False, default=datetime.now),
                                db.Column('updated_timestamp', db.DateTime,
                                          nullable=False,  onupdate=datetime.now, default=datetime.now)
                                )


# 数据包与权限多对多关系
datapack_permissions = db.Table('datapack_permissions',
                                db.Column('id', db.Integer,
                                          primary_key=True,  autoincrement=True),
                                db.Column('datapackid', db.Integer, db.ForeignKey(
                                    'datapack.id'), primary_key=True),
                                db.Column('permissionid', db.Integer, db.ForeignKey(
                                    'permissions.id'), primary_key=True),
                                db.Column('action', db.Integer,
                                          doc='1: view,2:create,3,edit,4.delete'),
                                db.Column('created_timestamp', db.DateTime,
                                          nullable=False, default=datetime.now),
                                db.Column('updated_timestamp', db.DateTime,
                                          nullable=False,  onupdate=datetime.now, default=datetime.now)
                                )


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    alias = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100), unique=True,
                     nullable=False, doc="user account")
    surname = db.Column(db.String(100), nullable=False, doc="real username")
    email = db.Column(db.String(200), unique=True,
                      nullable=False, doc="user email, can login as email")
    passwd = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Integer, nullable=False, doc="1:male,0:female")
    groupid = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    positionid = db.Column(db.Integer, db.ForeignKey(
        'positions.id'), nullable=False)
    url = db.Column(db.String(1024), nullable=False,
                    doc="user's home page when logined", default='')
    autologin = db.Column(db.Integer, nullable=False,
                          default=0, doc="1:true,0:false")
    autologout = db.Column(db.Integer, nullable=False, default=600)
    lang = db.Column(db.String(10), nullable=False, default='zh_CN')
    refresh = db.Column(db.Integer, nullable=False, default=30)
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0:disable,1:enable")
    type = db.Column(db.Integer, nullable=False, default=2,
                     doc="0:Super Admin,1:Admin,2: Normal,3:Guest")
    theme = db.Column(db.String(128), nullable=False, default='default')
    attempt_clock = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    attempt_failed = db.Column(db.Integer, nullable=False, default=0)
    attempt_ip = db.Column(db.String(64), nullable=False, default='')
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, onupdate=datetime.now, default=datetime.now)

    groups = db.relationship(
        'Group', backref=db.backref('users', lazy='subquery'))
    positions = db.relationship(
        'Position', backref=db.backref('users', lazy=True))
    roles = db.relationship(
        'Role', secondary=users_roles, lazy='subquery', backref=db.backref('users', lazy=True))

    permissions = db.relationship(
        'Permission', secondary=users_permissions, lazy='subquery', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.name


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    alias = db.Column(db.String(80), unique=True)
    pid = db.Column(db.Integer, db.ForeignKey('groups.id'))
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0: disable, 1: enable")
    description = db.Column(db.Text)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False,  onupdate=datetime.now, default=datetime.now)

    roles = db.relationship(
        'Role', secondary=groups_roles, lazy='subquery', backref=db.backref('groups', lazy=True))

    permissions = db.relationship(
        'Permission', secondary=groups_permissions, lazy='subquery', backref=db.backref('groups', lazy=True))

    def __repr__(self):
        return '<Group %r>' % self.name


class Position(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    alias = db.Column(db.String(80), unique=True)
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0: disable, 1: enable")
    description = db.Column(db.Text)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False,  onupdate=datetime.now, default=datetime.now)

    def __repr__(self):
        return '<Position %r>' % self.name


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    alias = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0:disable,1:enable")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False,  onupdate=datetime.now, default=datetime.now)
    permissions = db.relationship('Permission', secondary=roles_permissions, lazy='subquery',
                                  backref=db.backref('roles', lazy=True))

    def __repr__(self):
        return '<Role %r>' % self.name


class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    type = db.Column(db.Integer, nullable=False, doc = "1: menu, 2: data package, 3: page element")
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0:disable,1:enable")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False,  onupdate=datetime.now, default=datetime.now)


class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0:failed,1:success")
    ip = db.Column(db.String(64), nullable=False)
    info = db.Column(db.Text)
    lastaccess = db.Column(db.DateTime, nullable=False, default=datetime.now)


class BlockIP(db.Model):
    __tablename__ = "block_ip"
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    ip = db.Column(db.String(64), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0:disable,1:enable")
    description = db.Column(db.Text)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False,  onupdate=datetime.now, default=datetime.now)


class Menu(db.Model):
    __tablename__ = "menus"
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    alias = db.Column(db.String(80), unique=True)
    module = db.Column(db.String(200))
    pid = db.Column(db.Integer,db.ForeignKey('menus.id'))
    url = db.Column(db.String(500), unique=True, nullable=False)
    icon = db.Column(db.String(50), unique=True)
    status = db.Column(db.Integer, nullable=False,default=1, doc="0:disable,1:enable")
    order = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False,  onupdate=datetime.now, default=datetime.now)

    permissions = db.relationship('Permission', secondary=menus_permissions, lazy='subquery',
                                  backref=db.backref('menus', lazy=True))

    def __repr__(self):
        return '<Menu %r>' % self.name


class DataPack(db.Model):
    __tablename__ = "datapack"
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    alias = db.Column(db.String(80), unique=True)
    status = db.Column(db.Integer, nullable=False, doc="0:disable,1:enable")
    filter = db.Column(db.Text)
    description = db.Column(db.Text)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False,  onupdate=datetime.now, default=datetime.now)

    permissions = db.relationship('Permission', secondary=datapack_permissions, lazy='subquery',
                                  backref=db.backref('datapack', lazy=True))

    def __repr__(self):
        return '<DataPack %r>' % self.name



