# -*- encoding: utf-8 -*-
"""
@File    : wechat.py
@Time    :  2020/3/13 10:09
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import time
from datetime import datetime

from flask import request, jsonify
from lin.exception import Success, UnknownException
from lin.redprint import Redprint

from app.models.ctivity import Ctivity
from app.models.message import Message

front = Redprint("wechat")


@front.route("/search_sex", methods=["GET"])
def search_sex():
    sex = request.args["sex"]
    if sex:
        mess = Message.get_sex(sex=sex)
    return jsonify(mess)


@front.route("/search_id", methods=["GET"])
def search_id():

    uid = request.args["uid"]
    if uid:
        result = Message.get_unenroll(uid=uid)

        delattr(result[0], "cardid")  # 删除属性

        return jsonify(result)


@front.route("/search_criteria", methods=["GET"])
def search_search_criteria():

    return request.args.to_dict()


@front.route("/activity", methods=["GET"])
def activity():
    id = request.args["id"]
    ctivity = Ctivity.get_ctivity()
    for item in ctivity:
        date_list = []
        data = item.__dict__
        date = data["date"]

        start = eval(date)[0].replace("T", " ")[:-5]

        end = eval(date)[0].replace("T", " ")[:-5]

        expire = (datetime.strptime(start, "%Y-%m-%d %H:%M:%S")-datetime.now()).days
        apply = False
        if data["uid"]:
            uid_list = eval(data["uid"])
            if id in uid_list:
                apply = True

        start = time.strptime(start, "%Y-%m-%d %H:%M:%S")
        end = time.strptime(end, "%Y-%m-%d %H:%M:%S")
        start = time.strftime("%Y/%m/%d %H:%M:%S", start)
        end = time.strftime("%Y/%m/%d %H:%M:%S", end)
        date_list.append(start)
        date_list.append(end)
        setattr(item, "expire", expire)
        setattr(item, "apply", apply)
        item._fields.append("expire")
        item._fields.append("apply")
        setattr(item, "date", date_list)

    return jsonify(ctivity)


@front.route("/apply", methods=["GET"])
def apply():
    id = request.args["id"]
    ctivity_id = request.args["ctivity_id"]

    try:
        Ctivity.apply(id=id, ctivity_id=ctivity_id)
    except:
        return UnknownException("报名失败")
    return Success(msg="报名成功")


@front.route("/activity_details/", methods=["GET"])
def activity_details():

    ctivity_id = request.args["ctivity_id"]
    ctivity_data =  Ctivity.activity_details(ctivity_id=ctivity_id)
    if ctivity_data:

        date = eval(ctivity_data.__dict__["date"])
        stop_date = date[0]
        start_date = date[1]
        setattr(ctivity_data, "stop_date", stop_date)
        setattr(ctivity_data, "start_date", start_date)
        ctivity_data._fields.append("stop_date")
        ctivity_data._fields.append("start_date")

    return jsonify(ctivity_data)
