#views.py: 存放 路由+视图函数

from flask import Blueprint,request,render_template,\
    jsonify,make_response,Response,redirect,url_for
from . import models
#创建蓝图
blue = Blueprint('user',__name__)

@blue.route('/')
def home():
    return 'Flask Home!'

@blue.route('/request/',methods=['GET','POST'])
def get_request():
    pass
    print(request.method) # 获取Flask框架中的request对象, 注意需要先import
    '''
    这个request是ImmutableMultiDict类字典对象, 特点是允许有多个重复的key
    '''
    print(request.args)
    print(request.args['name'],request.args['age'])# 如果没有这个key, 会报错!
    print(request.args.get('name')) #即使没有这个key也不会报错
    #localhost:5000/request/?name=list1&name=list2&age=12
    print(request.args.getlist('name'))#如果有多个name的key, 应该用 getlist, 不然只会返回一个值

    #获取post参数
    print(request.form)
    return 'hello'


#查看Response对象信息
@blue.route('/response/',methods=['POST'])
def get_response():
    pass

    return 'response ok'  #返回字符串
    return render_template('login.html',name="张三",age="历史") #模版渲染并传参给模版引擎
    data = {'name':'张三','age':'李四'}
    return data  #返回json数据
    return jsonify(data)  #返回序列化json数据

    #返回自定义的response对象
    html = render_template('login.html',name="张三",age="历史")
    print(html,type(html))
    res = make_response(html,200)
    return res

    #不使用make_response方法, 自定义response对象
    res = Response(html)



#重定向Response
@blue.route("/redirect/")
def make_redirect():
    pass
    #重定向的几种方式
    return redirect("www.baidu.com") #跳转外部url
    return redirect('/request') #跳转到本服务器的路径

    #使用url_for跳转
    #user为蓝图的名称, 根据蓝图的名称和函数的名称找到对应跳转的路由
    ret = url_for('user.get_request')
    print('ret:',ret)
    return redirect(ret)

    # url_for传参跳转
    ret = url_for('user.get_request',name='王五',age="呵呵")
    print('ret:', ret)
    return redirect()


