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
            Ctivity.add_ctivity(**result)
    if request.method == "DELETE":
        return jsonify(request.data)

    if request.method == "PUT":
        return jsonify(request.data)

    return {"methods": ["POST", "DELETE", "PUT", "GET"]}