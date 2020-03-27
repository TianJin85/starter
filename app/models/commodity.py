# -*- encoding: utf-8 -*-
"""
@File    : commodity.py
@Time    :  2020/3/18 17:02
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from app.models.love import Love_commodity


class Commodity(Love_commodity):

    def add_commdity(self):
        Love_commodity.create(
            name = '头条',
            monthly = float(59),
            _type = 'common',
            comment = '公众号头条推送（一次）',
            commit=True
        )



