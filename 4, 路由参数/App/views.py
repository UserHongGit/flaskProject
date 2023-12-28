#views.py: 存放 路由+试图函数

'''
蓝图: 一种规划, 主要是用来规划urls(路由route)
蓝图的基本使用:
    在views.py初始化蓝图
        blue = Blueprint('user',__name__)
    在init文件中调用蓝图并进行路由注册
        app.register_blueprint(blueprint=blue)

'''
from flask import Blueprint
from . import models
#创建蓝图
blue = Blueprint('user',__name__)

@blue.route('/')
def home():
    return 'Flask Home!'

@blue.route('/string/<string:name>/')
def get_string(name):
    print(name,type(name))
    return 'hello'+name

#必须是any里设置的范围内的值才能访问, 否则无法访问提示404
@blue.route('/get_any/<any(apple,orange,banana):fruit>/')
def get_any(fruit):
    print(fruit,type(fruit))
    return 'hello'+fruit


@blue.route('/string/',methods=['POST'])
def req_post():
    return 'hello'

