# -*- encoding: utf-8 -*-
"""
@File    : serve.py
@Time    :  2020/3/16 17:40
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import jsonify
from lin.redprint import Redprint

server_api = Redprint("server")


@server_api.route("note", methods=["GET"])
def server_note():

    return jsonify()

