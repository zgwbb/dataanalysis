#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yunze
import pymongo
my_client = pymongo.MongoClient("mongodb://106.14.117.35:27017/")
# mydb = my_client["sports"]
mydb = my_client.dataanalysis
mydb.authenticate('dataAnalysis', '12345678', mechanism='SCRAM-SHA-1')


class OperationMongo(object):
    def __init__(self, ip, data_base, user, password):
        """
        :param ip:ip地址:
        :param data_base:指定数据库:
        :param user:指定用户:
        :param password:用户密码:
        """
        mongo_url = "mongodb://{}:27017/".format(ip)

        # 14352
        client = pymongo.MongoClient(mongo_url)
        self.data_base = client[data_base]
        self.data_base.authenticate(user, password, mechanism='SCRAM-SHA-1')

    def get_mongo_client(self):
        return self.data_base

    # 增加单条数据
    def add_single_data(self, gather, value):
        my_gather = self.data_base[gather]
        my_data_id = my_gather.insert_one(value)
        return my_data_id.inserted_id
    # 增加多条数据

    # 删除单条数据

    # 删除多条数据

    # 改动一条数据

    # 改动多条数据

    # 查询单条数据

    # 查询多条数据
