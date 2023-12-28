#views.py: 存放 路由+视图函数

from flask import Blueprint,request,render_template,\
    jsonify,make_response,Response,redirect,url_for

#一定要导入model, 不然model.py不会执行
from . import models
#创建蓝图
blue = Blueprint('user',__name__)

@blue.route('/')
def home():
    pass

    data = {
        'name':'ikun'
        ,'age':26
        ,'likes':['ball','sing','dacne']
    }

    # return render_template('template.html',name='ikun',age=26)
    return render_template('base.html',**data)


@blue.route('/child')
def child():
    pass

    data = {
        'name':'ikun'
        ,'age':26
        ,'likes':['ball','sing','dacne']
    }
    return render_template('child.html',**data)

@blue.route('/child2')
def child2():
    pass

    data = {
        'name':'ikun'
        ,'age':26
        ,'likes':['ball','sing','dacne']
    }
    return render_template('child2.html',**data)


