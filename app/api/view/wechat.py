# -*- encoding: utf-8 -*-
"""
@File    : wechat.py
@Time    :  2020/3/2 17:27
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import base64
import json
import os
from datetime import datetime

import requests
from lin.exception import Success, Failed, UnknownException
from lin.redprint import Redprint

from flask import render_template, redirect, request, jsonify, url_for, Response

from app.api.front.serve import codes
from app.config.pya_setting import get_jsapi_params, get_openid
from app.config.secure import WxAppidSecretSecure
from app.controller.save import Save
from app.controller.treating import enroll_data
from app.models.commodity import Commodity
from app.models.ctivity import Ctivity
from app.models.message import Message
from app.models.search_message import Serch_message
from app.models.selection import Selection
from app.models.user import User
from app.validators.love_forms import MessageForm

wechat = Redprint("wechat")

wechat_secure = WxAppidSecretSecure()


@wechat.route("/", methods=['GET'])
def test():
    APPID = "wxb10a1f7d311d8f9b"
    REDIRECT_URI = "http://www.anshun520.com/view/wechat/personal"
    SCOPE = "snsapi_userinfo "
    source_url = 'https://open.weixin.qq.com/connect/oauth2/authorize' \
                 + '?appid={APPID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={SCOPE}' \
                 + '#wechat_redirect'
    # REDIRECT_URI = quote(REDIRECT_URI, 'utf-8')
    # url = source_url.format(APPID=APPID, REDIRECT_URI=REDIRECT_URI, SCOPE=SCOPE)
    url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxb10a1f7d311d8f9b&redirect_uri=http://www.anshun520.com/view/wechat/index&response_type=code&scope=snsapi_userinfo&state=123&connect_redirect=1#wechat_redirect"

    return redirect(url)


@wechat.route("/index/<userid>", methods=[ "GET"])
@wechat.route("/index", methods=["GET"])
def index(userid=None):
    userinfo = {"userid": userid, "messid": None}
    code = request.args.get('code')
    if code:
        source_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?'\
            +'appid={APPID}&secret={APPSECRET}&code={CODE}&grant_type=authorization_code'
        access_token_url = source_url.format(APPID=wechat_secure.appdi, APPSECRET=wechat_secure.secret, CODE=code)
        resp = requests.get(access_token_url)
        if resp.ok:
            data = eval(resp.text) # 将字符串转为字典
            openid = data['openid']
            access_token = data["access_token"]
            info_url = " https://api.weixin.qq.com/sns/userinfo?access_token={ACCESS_TOKEN}&openid={OPENID}&lang=zh_CN"
            resp_user = requests.get(info_url.format(ACCESS_TOKEN=access_token, OPENID=openid))
            if resp_user.ok:
                result = eval(resp_user.text)

                user = User.add_openid(openid=openid, headimgurl=result["headimgurl"])    # 查询数据数据不存在就储存数据
                if user:
                    userid = User.get_user_id(openid=openid)
                    messid = Message.get_messid(uid=userid)
                    userinfo["messid"] = messid
                    userinfo["userid"] = userid
        else:
            return "登录失败"
    result = []
    data = Message.get_mess_all()

    for mess in data:
        mess_dict = mess.__dict__
        setattr(mess, "images", eval(mess_dict["images"])[0])
        setattr(mess, "userinfo", userinfo)
        mess._fields.append("userinfo")
        result.append(mess.__dict__)

    return render_template("index.html", result=result)


@wechat.route("/integral/", methods=[ "GET"])
def integral():
    userid = request.args["userid"]

    if userid:
        mess = Message.get_messid(uid=userid)


    return render_template("integral.html", userid=userid)


@wechat.route("/activity/", methods=["POST", "GET"])
def activity():
    userid = request.args["userid"]

    return render_template("activity.html", userid=userid)


@wechat.route("/activity_details/", methods=["POST", "GET"])
def activity_details():

    activity_id = request.args["activity_id"]

    return render_template("activity_details.html", activity_id=activity_id)


@wechat.route("/consumption/", methods=["POST", "GET"])
def consumption():
    userid = request.args["userid"]

    return render_template("consumption.html", userid=userid)


@wechat.route("/enroll/", methods=["POST", "GET"])
def enroll():
    userid = request.args["userid"]
    form = MessageForm(request.form)

    if request.method == "POST":
        print(request.form.to_dict())
        if form.validate():
            try:
                result = request.form.to_dict()
                uid = result["userid"]
                code = str(result["code"])

                if code == codes[uid]["code"]["code"]:
                    minute = (datetime.now() - codes[uid]["code"]["date"]).seconds / 60
                    codes.pop(uid, "")      # 删除验证码
                    if minute > 5:

                        imgpath = Save(result=result).get_data()        # 保存图片获取地址
                        try:
                            cardidinfo = Message.set_cardid(result["cardid"])
                            enroll_data(result, imgpath, cardidinfo)
                            return Success(msg="报名成功")
                        except:
                            return UnknownException(msg="请检查身份证是否输入正确")
                    else:
                        Success(msg="验证码已过期")
                return Success(msg="验证码不正确")
            except os.error as e:
                return jsonify({"errors": e, "status": 500})
        else:
            error_data = ""
            for items in form.errors.values():
                for item in items:
                    error_data+=item+"\n"

            return jsonify({"errors": error_data, "status": 300})

    return render_template("enroll.html", userid=userid)


@wechat.route("/vip_hyfw/", methods=["GET"])
def vip_hyfw():
    userid = request.args['userid']
    return render_template("vip_hyfw.html", userid=userid)


@wechat.route("/my_balance/", methods=["GET"])
def my_balance():
    userid = request.args["userid"]

    return render_template("my_balance.html", userid=userid)


@wechat.route("/upenroll/", methods=["GET"])
def upenroll():
    userid = request.args["userid"]
    return render_template("upenroll.html", userid=userid)


@wechat.route("/message/", methods=["GET"])
def message():
    userid = request.args["userid"]

    return render_template("message.html", userid=userid)


@wechat.route("/message_details/", methods=["GET"])
def message_details():
    userid = request.args["userid"]

    return render_template("message_details.html",  userid=userid)


@wechat.route("/order/", methods=["GET"])
def order():
    userid = request.args["userid"]
    return render_template("order.html", userid=userid)


@wechat.route("/order_details/", methods=["GET"])
def order_details():
    userid = request.args["userid"]
    return render_template("order_details.html", userid=userid)


@wechat.route("/personal/", methods=["GET"])
def personal():
    userid = request.args["userid"]
    if userid:
        mess_data =Message.get_message(userid)
        mess_data["userid"] = userid
        return render_template("personal.html", mess_data=mess_data)

@wechat.route("/personal_details/", methods=["GET"])
def personal_details():
    uid = request.args["uid"]
    if uid:

        return render_template("personal_details.html", uid=uid)


@wechat.route("/recharge/", methods=["GET"])
def recharge():
    userid = request.args["userid"]
    if request.method == "POST":
        if userid:
            openid = User.get_openid(userid)
            result = get_jsapi_params(openid)
            result["userid"] = userid
        return render_template("recharge.html", **result)
    return render_template("recharge.html", userid=userid)


@wechat.route("/recharge_vip/", methods=["GET"])
def recharge_vip():
    return render_template("Recharge_vip.html")


@wechat.route("/search_criteria/", methods=["GET"])
def search_criteria():

    return render_template("search_criteria.html")


@wechat.route("/search_result/", methods=["GET"])
def search_result():
    sex = request.args["sex"]
    return render_template("search_result.html", sex=sex)


@wechat.route("/see_qq/", methods=["POST", "GET"])
def see_qq():
    result = None
    id = request.args["userid"]
    if id is not None:
        result = Serch_message.qq_list(id=id)

    return render_template("see_qq.html", result=result)


@wechat.route("/see_wx/", methods=["POST", "GET"])
def see_wx():

    return render_template('see_wx.html')

@wechat.route("/messinfo/", methods=["POST", "GET"])
def messinfo(userid=None):
    if request.method == "POST":
        userid = request.form["userid"]
        data = Message.get_unenroll(userid)
        return jsonify(data)
    data = Message.get_unenroll(userid)
    return jsonify(data)


@wechat.route("/indexinfo/", methods=["POST", "GET"])
def indexinfo():

    data = Message.get_index()

    for mess, select in data:

        mess_dic = mess.__dict__
        # select_dic = select.__dict__

        # result = Message.set_cardid(mess.cardid)
        #
        # setattr(mess, "sex", result["sex"])
        # setattr(mess, "age", result["age"])
        delattr(mess, "cardid")
        # mess._fields.append("sex")
        # mess._fields.append("age")
        setattr(mess, "images", eval(mess_dic["images"])[0])

    return jsonify(data)


@wechat.route("/payment", methods=["GET"])
def paryment():

    return render_template("wx_js_pay.html", context={'params': get_jsapi_params("oB2YTuAUMHUAGZLPRPI_kfMbV5sg")})




@wechat.route("/add_commodity", methods=['GET'])
def add_commodity():
    comm = Commodity()
    comm.add_commdity()
    return Success(msg="添加成功")