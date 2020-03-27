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


codes = {}


@server_api.route("/note/", methods=["GET"])
def server_note():
    id = request.args["id"]
    phone = request.args["phone"]

    if id and re.search(r'1[3,4,5,7,8]\d{9}', phone):

        for items in list(codes.keys()):
            for item in codes[items]:

                second = (datetime.now() - codes[items][item]["date"]).seconds/60  # 获取所有验证码存在的时间
                if second >= 5:     # 超过五分钟则删除
                    codes.pop(items)    # 删除验证码

        if id not in codes:
            code = NoetServer.random_code()
            code["date"] = datetime.now()

            codes[id] = {"code": code}
            # resp = eval(NoetServer(phone=phone, code_dict={"code": code}).send_code())
            # if resp["Message"]=="OK":
            #     return Success(msg="短信发送成功")

        else:
            return Success(msg="短信以发送请5分钟后重试")

    else:
        return Success(msg="电话号码格式不正确请重新输入")



