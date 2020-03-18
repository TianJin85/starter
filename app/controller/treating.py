# -*- encoding: utf-8 -*-
"""
@File    : treating.py
@Time    :  2020/3/18 19:44
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from app.models.message import Message
from app.models.selection import Selection


def enroll_data(result, imgpath, cardidinfo):
    mess_data = {
        "uid": result["userid"],
        "username": result["username"],
        "census": result["census"],
        "cardid": result["cardid"],
        "stature": result["stature"],
        "weight": result["weight"],
        "wechat": result["wechat"],
        "qq": result["qq"],
        "school": result["school"],
        "education": result["education"],
        "workunit": result["workunit"],
        "occupation": result["occupation"],
        "profession": result["profession"],
        "monthly": result["monthly"],
        "member": result["member"],
        "housing": result["housing"],
        "rest": result["rest"],
        "vehicle": result["vehicle"],
        "marriage": result["marriage"],
        "phone": result["phone"],
        "images": imgpath,
        "sex": cardidinfo["sex"],
        "age": cardidinfo["age"]
    }

    Message.add_message(**mess_data)
    mess_id = Message.get_messid(uid=result["userid"])
    select_data = {"mid": mess_id,
                   "marriage": result["marriage"],
                   "age": result["age"],
                   "stature": result["ze_stature"],
                   "weight": result["ze_weight"],
                   "monthly": result["ze_monthly"],
                   "housing": result["ze_housing"],
                   "vehicle": result["ze_vehicle"],
                   "children": result["ze_housing"],
                   "census": result["ze_census"],
                   "pests": result["ze_pests"]}
    Selection.add_selection(**select_data)