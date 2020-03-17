# -*- encoding: utf-8 -*-
"""
@File    : wechat.py
@Time    :  2020/3/13 10:08
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import request, jsonify
from lin import admin_required
from lin.exception import Success, UnknownException
from lin.redprint import Redprint
from werkzeug.datastructures import ImmutableMultiDict

from app.models import ctivity
from app.models.ctivity import Ctivity
from app.models.love import Love_ctivity
from app.validators.love_forms import Ctivity_Form

back = Redprint("wechat")


@back.route("/manage", methods=["POST", "DELETE", "PUT", "GET"])
@admin_required
def activity():
    if request.method == "POST":
        form = Ctivity_Form(ImmutableMultiDict(eval(str(request.data, encoding='utf-8'))))
        if form.validate():
            result = eval(str(request.data, encoding='utf-8'))
            result.pop("num")
            if Ctivity.add_ctivity(**result):
                return Success(msg="发布活动成功")
            return UnknownException(msg="发布活动失败、活动名是否重复？")
    if request.method == "DELETE":
        return jsonify(request.data)

    if request.method == "PUT":
        return jsonify(request.data)

    return {"methods": ["POST", "DELETE", "PUT", "GET"]}