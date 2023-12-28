#views.py: 存放 路由+视图函数

from flask import Blueprint,request,render_template,\
    jsonify,make_response,Response,redirect,url_for

#一定要导入model, 不然model.py不会执行
from . import models
#创建蓝图
blue = Blueprint('user',__name__)

@blue.route('/')
def index():
    return 'index'



