# encoding: utf-8

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from exts import db


class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

    # 字段映射
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def password(self):
        return self._password

    # 前端传入的密码进行加密
    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    # 密码校验
    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result
