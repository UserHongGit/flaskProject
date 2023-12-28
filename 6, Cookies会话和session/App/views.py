#views.py: 存放 路由+视图函数
import datetime

from flask import Blueprint,request,render_template,\
    jsonify,make_response,Response,redirect,url_for\
    ,session
from . import models
blue = Blueprint('user',__name__)

@blue.route('/')
@blue.route('/home/')
def home():
    #4, 获取cookies
    username = request.cookies.get('user');
    username = session.get('user')
    return render_template("template.html",username = username)

@blue.route('/login/',methods=['GET','POST'])
def login():
    #GEt请求就访问登录页面
    if request.method == 'GET':
        return render_template('login.html')
    #POST请求, 实现登录逻辑
    elif request.method == 'POST':
        pass
        #1, 获取前端提交的数据
        username = request.form.get('username')
        password = request.form.get('password')

        #2, 模拟登录, 用户名和密码验证
        if username == 'zs' and password == '1':
            #登录成功
            response = redirect('/home/')

            #3, 设置cookie
            #cookies中不能用中文, 浏览器关闭, cookies失效
            #max_age设置过期时间的两种方式
            response.set_cookie('user',username,max_age=3600*24*7)
            # response.set_cookie('user',username,expires=datetime.datetime(2023,12,12))

            #3, 也可以使用session
            session['user'] = username
            session.permanent = True  #设置session的过期时间, 时间为一个月
            return response
        else:
            return '用户名密码错误'

@blue.route("/logout")
def logout():
    #5, 删除cookies
    response = redirect('/home/')
    response.delete_cookie('user')
    session.pop('user')
    # session.clear()
    return response

