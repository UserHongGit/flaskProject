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

# @app.route('/')   将app换成blue使用蓝图, 但是伴随一个问题, blue怎么和app关联绑定  ->>  在init文件通过注册蓝图, 进行绑定
@blue.route('/')
def home():  # put application's code here
    return 'Flask Home!'


#也可以继续再创建新的蓝图, 让不同的蓝图各自管理
blue2 = Blueprint('product',__name__)
@blue2.route("/goods")
def goods():
    return 'index'


