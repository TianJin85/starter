"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

# 安全性配置
from app.config.setting import BaseConfig


class DevelopmentSecure(BaseConfig):
    """
    开发环境安全性配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://tianjin:TJ307440205@211.149.250.67:3306/marriage'

    SQLALCHEMY_ECHO = False

    SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'


class ProductionSecure(BaseConfig):
    """
    生产环境安全性配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://tianjin:TJ307440205@211.149.250.67:3306/marriage'

    SQLALCHEMY_ECHO = False

    SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'


class WxAppidSecretSecure(BaseConfig):
    """
        生产环境appid  secret配置
    """
    appdi = "wxb10a1f7d311d8f9b"
    secret = "2e15b2278054f1aa2eaec2967fb1c578"
    url = "https://api.weixin.qq.com/cgi-bin/{0}"
    token = None
    detection_url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}"


class RedisSecure:
    """
    Redis开发环境配置
    """
    name = "tianjin"
    host = "11.149.250.67"
    port = 6379
    db = 0


class NodeAccessKey:
    """
    Node Server AccessKeyId and AccessKeySecret
    """
    AccessKeyId = "LTAI4FcXR2ChjYjD57x9Cyn6"
    AccessKeySecret = "hHL9Xn263xnNZ3uQFrV6Xsvi9Xe40x"
