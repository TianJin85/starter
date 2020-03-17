# -*- encoding: utf-8 -*-
"""
@File    : ctivity.py
@Time    :  2020/3/14 16:16
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.exception import ParameterException

from app.models.love import Love_ctivity


class Ctivity(Love_ctivity):

    @classmethod
    def add_ctivity(cls, name, address, testarea, date, images, rule, message, initiator, money):
        user = Love_ctivity.query.filter_by(name=name).first()
        if user is not None:
            raise ParameterException(msg='活动名称以存在')
        Love_ctivity.create(
            name=name,
            address=address,
            testarea=testarea,
            date=str(date),
            images=images,
            rule=rule,
            message=message,
            initiator=initiator,
            money=float(money),
            num=0,
            commit=True
        )
        return True

