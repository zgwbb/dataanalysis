"""
赛事接口
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from apps.models import mydb
from utils import Pager
from json import dumps
import re
matchevent = Blueprint('match_bp', __name__, url_prefix='/api/v1')

# 赛事发布接口
@matchevent.route('/public', methods=['POST'])
@jwt_required
def release_match():
    my_col = mydb['match']
    my_admin = mydb['admin']
    try:
        # data包含了要添加的赛事名称，地点，内容，时间
        data = [{"name": request.json['name'], "time": request.json['time'],
                 "site": request.json['site'],
                 "content": request.json['content']}]
        # 判断请求数据的长度
        data1 = list(request.json.values())
        event_data = []
        for match_data in my_col.find():
            event_data.append(
                {"name": match_data['event_name'], "time": match_data['event_time'],
                 "site": match_data['site'],
                 "content": match_data['content']})
        # 判断当前用户是否是管理员
        if my_admin.find_one({'Admin_email': get_jwt_identity()}):
            if len(data1) != 4:
                return jsonify({'success': False,
                                'message': 'Please enter the event information to be created correctly'}), 401
            else:
                if '' in data1:
                    return jsonify({'success': False,
                                    'message': 'Please enter the event information to be created correctly'}), 401
                if data[0] not in event_data:
                    my_col.insert(
                        {
                            "event_name": data1[0],
                            "event_time": data1[1],
                            "site": data1[2],
                            "content": data1[3]
                        })
                    return jsonify({'status': 'Event released successfully'}), 200
                else:
                    return jsonify({'success': False,
                                    'message': 'The event already exists'}), 401
        else:
            return jsonify({'success': False,
                            'message': 'The current user does not exist and cannot perform the operation'}), 401
    except KeyError:
        return jsonify({'success': False,
                        'message': 'Wrong number of values entered'}), 401

# 赛事删除
@matchevent.route('/public', methods=['DELETE'])
@jwt_required
def delete_match():
    my_col = mydb['match']
    my_admin = mydb['admin']
    # data包含了要添加的赛事名称，地点,时间
    data = []
    try:
        data.append({"name": request.json['name'], "time": request.json['time'],
                     "site": request.json['site']})
        # 判断请求数据的长度
        data1 = list(request.json.values())
        event_data = []
        for match_data in my_col.find():
            event_data.append(
                {"name": match_data['event_name'], "time": match_data['event_time'],
                 "site": match_data['site']})
        # 判断当前用户是否是管理员
        if my_admin.find_one({'Admin_email': get_jwt_identity()}):
            if len(data1) != 3:
                return jsonify({'success': False,
                                'message': 'Wrong number of values entered'}), 401
            else:
                if '' in data1:
                    return jsonify({'success': False,
                                    'message': 'Wrong number of values entered'}), 401
                if data[0] in event_data:
                    my_col.delete_one(
                        {'event_name': data1[0], "event_time": data1[1], "site": data1[2]})

                    return jsonify({'status': 'Event delete successfully'}), 200
                else:
                    return jsonify({'success': False,
                                    'message': 'The event already not exists'}), 401
        else:
            return jsonify(
                {'success': False, 'message': 'The current user does not exist and cannot perform the operation'}), 401
    except KeyError:
        return jsonify({'success': False,
                        'message': 'Wrong number of values entered'}), 401


# 赛事查询
@matchevent.route('/sportsQuery', methods=['POST'])
@jwt_required
def get_match_apply():
    # 获取管理员信息
    my_col = mydb['admin']
    # 获取赛事信息
    my_col_match = mydb['match']
    match_data = []
    for match_message in my_col_match.find():
        match_data.append({"name": match_message['event_name'], "time": match_message['event_time'],
                           "site": match_message['site'], "content": match_message['content']})
    # 获取用户要页码
    try:
        new_page = request.args["page"]
        pager = Pager(int(new_page))
        if int(new_page) == 0:
            return jsonify({'success': False, 'message': 'The page number you requested does not exist'}), 401
        # 判断当前用户在数据库中是否存在
        if my_col.find_one({'Admin_email': get_jwt_identity()}):
            if pager.start <= len(match_data):
                if pager.end <= len(match_data):
                    user_data_f = match_data[pager.start:pager.end]
                    return dumps(user_data_f), 200
                else:
                    user_data_f = match_data[pager.start: pager.end]
                    return dumps(user_data_f), 200
            else:
                return jsonify({'success': False, 'message': 'The page number you requested does not exist'}), 401
        else:
            return jsonify({'success': False, 'message': 'Insufficient permissions of current account'}), 401
    except KeyError:
        return jsonify({'success': False, 'message': 'Wrong number of values entered'}), 401
    except ValueError:
        return jsonify({'success': False, 'message': 'Wrong number of values entered'}), 401

# 赛事修改
@matchevent.route('/public', methods=['PUT'])
@jwt_required
def alter_match_apply():
    my_col = mydb['match']
    my_admin = mydb['admin']
    # data包含了要添加的赛事名称，地点，内容，时间
    data = []
    try:
        name = request.json['name']
        data.append({"name":name , "time": request.json['time'],
                     "site": request.json['site']})
        # 获取请求数据的值
        data1 = list(request.json.values())
        del data1[0:3]
        # 获取请求数据的键
        data2 = list(request.json.keys())
        # 要删除的key
        delete_key = ['name', 'time', 'site']
        # 获取要修改的键值
        data2 = [x for x in data2 if x not in delete_key]
        # data_k也是获取请求参数的键值
        data_k = []
        for x in data2:
            data_k.append(re.sub(r'new_', '', x))
        print(data_k)
        event_data = []
        for match_data in my_col.find():
            event_data.append(
                {"name": match_data['event_name'], "time": match_data['event_time'],
                 "site": match_data['site']})
        # 判断当前用户是否是管理员
        if my_admin.find_one({'Admin_email': get_jwt_identity()}):
            if data[0] not in event_data:
                return jsonify({'success': False,
                                'message': 'The event already not exists'}), 401
            else:
                if len(data_k) == 1:
                    my_col.update_one(
                        {'event_name': request.json['name'], "event_time": request.json['time'],
                         "site": request.json['site']}, {"$set": {data_k[0]: data1[0]}})
                    return jsonify({'status': 'Event modify successfully'}), 200
                elif len(data_k) == 2:
                    my_col.update_one(
                        {'event_name': request.json['name'], "event_time": request.json['time'],
                         "site": request.json['site']}, {"$set": {data_k[0]: data1[0], data_k[1]: data1[1]}})
                    return jsonify({'status': 'Event modify successfully'}), 200
                elif len(data_k) == 3:
                    my_col.update_one(
                        {'event_name': request.json['name'], "event_time": request.json['time'],
                         "site": request.json['site']},
                        {"$set": {data_k[0]: data1[0], data_k[1]: data1[1], data_k[2]: data1[2]}})
                    return jsonify({'status': 'Event modify successfully'}), 200
                elif len(data_k) == 4:
                    my_col.update_one(
                        {'event_name': request.json['name'], "event_time": request.json['time'],
                         "site": request.json['site']}, {
                            "$set": {data_k[0]: data1[0], data_k[1]: data1[1], data_k[2]: data1[2],
                                     data_k[3]: data1[3]}})
                    return jsonify({'status': 'Event modify successfully'}), 200
                else:
                    return jsonify(
                        {'success': False,
                         'message': 'Wrong value entered'}), 401
        else:
            return jsonify(
                {'success': False, 'message': 'The current user does not exist and cannot perform the operation'}), 401
    except ValueError:
        return jsonify(
            {'success': False, 'message': 'Wrong value entered'}), 401
    except KeyError:
        return jsonify(
            {'success': False, 'message': 'Wrong value entered'}), 401

