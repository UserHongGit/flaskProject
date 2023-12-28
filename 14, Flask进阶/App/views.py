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
    print('使用内置g对象: ',g.star)
    time.sleep(5) #模拟查询数据库 ,耗时5s
    return 'index'

'''
钩子函数, 也叫中间件, 
    @blue.before_request: 每一次请求之前访问
'''
@blue.before_request
def before():
    print('before request')

    #
    print(request.path)
    print(request.method)
    print(request.remote_addr)  #客户端ip信息

    #简单的反扒
    print(request.user_agent)
    if 'python' in request.user_agent.string:
        return '使用python发的请求, 拒绝连接!'
    ip = request.remote_addr
    if cache.get(ip):
        return '调用太快'
    cache.set(ip,'value',timeout=1)  #1s内只允许一个ip访问一次

    print('------------------')
    g.star = '使用全局的应用对象赋值!'
    print(g.star)
    print(current_app)
    print(current_app.config)

'''
Flask 内置对象
    request:
    session:
    g: 全局对象
    current_app: Flask应用对象
'''










