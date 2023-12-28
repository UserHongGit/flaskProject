#views.py: 存放 路由+视图函数
import random
import time

from flask import Blueprint,request,render_template,\
    jsonify,make_response,Response,redirect,url_for \
    ,session,g,current_app
from .exts import cache #导入缓存

#一定要导入model, 不然model.py不会执行
from . models import *
#创建蓝图
blue = Blueprint('book_blue',__name__)

@blue.route('/')
@cache.cached(timeout=20) #缓存失效时间20s
def index():
    print('index')
    time.sleep(5) #模拟查询数据库 ,耗时5s
    return 'index'

@blue.route('/template/')
def template():
    return render_template('template.html')









