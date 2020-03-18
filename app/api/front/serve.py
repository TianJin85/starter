# -*- encoding: utf-8 -*-
"""
@File    : serve.py
@Time    :  2020/3/16 17:40
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import re
from datetime import datetime

from flask import jsonify, request
from lin.exception import Success
from lin.redprint import Redprint

from app.note.server import NoetServer

server_api = Redprint("server")

globals()
codes = {}


@server_api.route("/note", methods=["GET"])
def server_note():
    id = request.args["id"]
    phone = request.args["phone"]
    if id and re.match(r'1[3,4,5,7,8]\d{9}', phone):

        code = NoetServer.random_code()
        code["date"] = datetime.now()

        codes[id] = {"code": code}
        resp = eval(NoetServer(phone=phone, code_dict=code).send_code())
        if resp["Message"]=="OK":
            return Success(msg="短信发送成功")
    else:
        return Success(msg="电话号码格式不正确请重新输入")