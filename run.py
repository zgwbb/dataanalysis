#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yunze
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from apps import create_app
app = create_app()

if __name__ == '__main__':
    CORS(app)
    jwt = JWTManager(app)
    app.run()

