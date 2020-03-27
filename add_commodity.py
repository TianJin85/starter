# -*- encoding: utf-8 -*-
"""
@File    : add_commodity.py
@Time    :  2020/3/27 14:35
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""

from lin.core import User
from lin.db import db

from app.app import create_app
from app.models.love import Love_commodity


def main():
    app = create_app()
    with app.app_context():
        with db.auto_commit():
            # 创建一个超级管理员
            commodity1 = Love_commodity()
            commodity1.name = "VIP周收费"
            commodity1.monthly = 99
            commodity1.type = "VIP"
            commodity1.comment = "充值99有一周的会员权益"

            commodity2 = Love_commodity()
            commodity2.name = "VIP一个月"
            commodity2.monthly = 199
            commodity2.type = "VIP"
            commodity2.comment = "充值199有一个月的会员权益"

            commodity3 = Love_commodity()
            commodity3.name = "VIP三个月"
            commodity3.monthly = 499
            commodity3.type = "VIP"
            commodity3.comment = "充值499有三个月的会员权益"

            commodity4 = Love_commodity()
            commodity4.name = "VIP半年"
            commodity4.monthly = 899
            commodity4.type = "VIP"
            commodity4.comment = "充值899有半年的会员权益"

            commodity5 = Love_commodity()
            commodity5.name = "VIP一年收费"
            commodity5.monthly = 1499
            commodity5.type = "VIP"
            commodity5.comment = "充值1499有一年的会员权益"

            commodity11 = Love_commodity()
            commodity11.name = "VIP一年服务"
            commodity11.monthly = 2999
            commodity11.type = "VIP"
            commodity11.comment = "1、看相片 2、看联系方式 3、交换联系方式 4、了解交流情况 5、推见面 6、见面回访 7、推动恋爱回访 8、推动相亲2次/月 9、相亲免费赠送咖啡"

            # 普通收费项目

            commodity6 = Love_commodity()
            commodity6.name = "查看电话微信"
            commodity6.monthly = 39
            commodity6.type = "common"
            commodity6.comment = "看电话、微信一次"

            commodity7 = Love_commodity()
            commodity7.name = "查看相片"
            commodity7.monthly = 9.9
            commodity7.type = "common"
            commodity7.comment = "查看相片（3-5张生活照）"

            commodity8 = Love_commodity()
            commodity8.name = "初识"
            commodity8.monthly = 99
            commodity8.type = "common"
            commodity8.comment = "一次婚姻（工作单位性格，朋友眼中的TA）"

            commodity9 = Love_commodity()
            commodity9.name = "微信群"
            commodity9.monthly = 499
            commodity9.type = "common"
            commodity9.comment = "小罗哥创建的相亲微信群聊（一年）"

            commodity10 = Love_commodity()
            commodity10.name = "头条"
            commodity10.monthly = 59
            commodity10.type = "common"
            commodity10.comment = "公众号头条推送（一次）"


if __name__ == '__main__':
    try:
        main()
        print("新增超级管理员成功")
    except Exception as e:
        raise e