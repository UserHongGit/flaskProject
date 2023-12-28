# __init__.py 初始化文件,创建Flask应用
# 添加了__init__.py会将本文件夹编程python的一个包

from flask import Flask

#不能这样直接创建Flask应用, 否则其他地方引用本模块的包的时候, 会创建好几次应用
#最好就是处理成一个函数, 到时候只会调用一次, 比如: create_app()
# app = Flask(__name__)


'''
导入包的工作, 都由init来做, 后续即使views.py需要用models.py, 也都由init来做, 防止循环引用, 统一使用蓝图来做
'''
from .views import blue


def create_app():
    app = Flask(__name__)

    #注册蓝图
    app.register_blueprint(blueprint=blue)
    return app;



