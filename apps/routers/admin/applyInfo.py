"""
报名信息接口
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from apps.models import mydb
from utils import Pager
from json import dumps
applyinfo = Blueprint('apply_bp', __name__, url_prefix='/api/v1')


# 获取用户数据的接口
@applyinfo.route('/applyInfo', methods=['GET'])
@jwt_required
def get_user_apply():
    # 获取管理员信息
    my_col = mydb['admin']
    # 获取用户信息
    my_col_uesr = mydb['users']
    user_number =[]
    user_data = []
    for user_idNumber in my_col_uesr.find():
        user_number.append(user_idNumber['idNumber'])
    for user_message in my_col_uesr.find():
        user_data.append({"wxId":user_message['wxId'],"name":user_message['name'],"phone":user_message['phone'],"school":user_message['school'],"identityCard":user_message['idNumber']})
    # 获取用户要页码
    try:
        new_page = request.args["page"]
        pager = Pager(int(new_page))
        if int(new_page) == 0:
            return jsonify({'success': False, 'message': 'The page number you requested does not exist'}), 401
        # 判断当前用户在数据库中是否存在
        if my_col.find_one({'Admin_email': get_jwt_identity()}):
            if pager.start <= len(user_number):
                if pager.end <= len(user_number):
                    user_data_f = user_data[pager.start:pager.end]
                    return dumps(user_data_f), 200
                else:
                    user_data_f = user_data[pager.start: pager.end]
                    return dumps(user_data_f), 200
            else:
                return jsonify({'success': False, 'message': 'The page number you requested does not exist'}), 401
        else:
            return jsonify({'success': False, 'message': 'Insufficient permissions of current account'}), 401
    except ValueError:
        return jsonify({'success': False, 'message': 'Wrong value entered'}), 401







