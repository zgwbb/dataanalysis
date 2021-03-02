#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yunze
from flask import Flask
from setting import DevelopmentConfig
from apps.routers import adminLogin,applyinfo,matchevent



def create_app():
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(DevelopmentConfig)
    # 注册蓝图
    app.register_blueprint(adminLogin)
    app.register_blueprint(applyinfo)
    app.register_blueprint(matchevent)
    return app


