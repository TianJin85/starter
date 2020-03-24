# -*- encoding: utf-8 -*-
"""
@File    : ctivity.py
@Time    :  2020/3/14 16:16
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.exception import ParameterException

from app.models.love import Love_ctivity, Love_user


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

    @classmethod
    def get_ctivity(cls):
        ctivity = Love_ctivity.query.all()

        return ctivity

    @classmethod
    def apply(cls, id, ctivity_id):
        ctivity = Love_ctivity.query.filter_by(id=ctivity_id).first()
        id_list = []
        if ctivity:
            if ctivity.uid:
                uid_list = eval(ctivity.uid)
                if id not in uid_list:
                    uid_list.append(id)
                    ctivity.update(
                        uid=str(uid_list),
                        commit=True
                    )
                    num = int(ctivity.num)+1
                    ctivity.update(
                        num=num,
                        commit=True
                    )
            else:
                id_list.append(id)
                ctivity.update(
                    uid=str(id_list),
                    commit=True
                )

                num = int(ctivity.num) + 1
                ctivity.update(
                    num=num,
                    commit=True
                )
        return True

