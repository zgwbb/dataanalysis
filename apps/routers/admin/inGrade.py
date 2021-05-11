#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yunze
"""
导入比赛成绩
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
inGrade = Blueprint('grade_bp', __name__, url_prefix='/api/v1')




