# -*- encoding: utf-8 -*-
"""
@File    : commodity.py
@Time    :  2020/3/18 17:02
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from app.app import create_app
from app.models.love import Love_commodity
from lin.db import db

app = create_app()
with app.app_context():
    with db.auto_commit():
        commodity1 = Love_commodity()
        commodity1.name = "查看电话"
        commodity1.monthly = 39
        commodity1.comment = "若女方不同意，免费继续下一个"

        commodity2 = Love_commodity()
        commodity2.name = "查看微信"
        commodity2.monthly = 39
        commodity2.comment = "若女方不同意，免费继续下一个"

        commodity3 = Love_commodity()
        commodity2.name = "查看相片"
        commodity3.monthly = 9.9
        commodity3.comment = "一人一次"

        commodity4 = Love_commodity()
        commodity4.name = "初识"
        commodity4.monthly = 99
        commodity4.comment = "一次婚(婚姻工作单位、性格、朋友中的Ta)"

        commodity5 = Love_commodity()
        commodity5.name = "微信群"
        commodity5.monthly = 499
        commodity5.comment = "一年"

        commodity6 = Love_commodity()
        commodity6.name = "头条公众推送"
        commodity6.monthly = 59
        commodity6.comment = "公众号推送（非头条19元一次）"


