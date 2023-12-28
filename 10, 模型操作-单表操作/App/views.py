#views.py: 存放 路由+视图函数

from flask import Blueprint,request,render_template,\
    jsonify,make_response,Response,redirect,url_for

#一定要导入model, 不然model.py不会执行
from . models import *
#创建蓝图
blue = Blueprint('user',__name__)

@blue.route('/')
def index():
    return 'index'

#表操作
#数据的操作在这里, 表结构的更改, 在models.py里, 然后进行数据迁移

#增: 添加数据
@blue.route('/useradd/')
def user_add():
    #添加单条数据
    u = User()
    u.name = 'ikun'
    u.age = 24
    # db.session.add(u);  #将u对象添加到session中
    # db.session.commit(); #同步到数据库中



    #添加多条数据
    users = [];
    for i in range(10,30):
        u = User();
        u.name = '蔡徐坤' + str(i)
        u.age = i;
        users.append(u)

    try:
        db.session.add_all(users)
        db.session.commit(); #事务提交
    except Exception as e:
        db.session.rollback()  #回滚
        db.session.flush()  #清空缓存
        return "批量添加数据失败" + str(e);
    return "批量添加数据成功";

@blue.route('/userdel/')
def user_del():
    u = User.query.first();#查询第一条数据
    db.session.delete(u)
    db.session.commit();

    return '删除成功'

@blue.route('/userupdate/')
def user_update():
    u = User.query.first();#查询第一条数据
    u.name = '蔡徐坤-修改'
    u.age = 1000
    #直接修改, 提交就行了
    db.session.commit();

    return '修改成功'

#查询
@blue.route('/userget/')
def user_get():
    #all()  返回所有的数据, 列表形式
    users = User.query.all()
    print(users)
    print(list(users)) #转换成列表形式
    #User.query是一条sql语句, 类型是<class 'flask_sqlalchemy.query.Query'>一个查询对象
    print(User.query,type(User.query))

    print('----------------------')
    #filter(): 过滤, 得到查询集, 类似SQL中的where, 与get()不一样, get()得到的是数据, filter()得到的是数据集
    users = User.query.filter()
    print(users,type(users))
    # users.filter(); #可以继续filter查询

    print('----------------------')
    #get()  查询对应主键的数据对象
    user = User.query.get(12);
    # user = User.query.get_or_404(12);
    print(user,type(user)) #返回User对象 <class 'App.models.User'>

    '''
    filter()   类似SQL中的where
    filter_by()  用于等值操作的过滤
    '''
    print('----------------------')
    users = User.query.filter(User.age==20)
    print(users)
    print(list(users))
    #使用filter_by
    users = User.query.filter_by(age=20)
    # users = User.query.filter_by(age>20)  #不能使用范围的, 只能使用等值的, 非等值的使用filter()
    print(list(users))

    print('----------------------')
    #first()   第一条数据
    #last()  最后一条数据
    user = User.query.first()
    # user = User.query.filter_by(age = 8888).first_or_404()  #第一条数据不存在, 抛出404错误

    print('----------------------')
    users = User.query.filter();
    print(users.count())

    print('----------------------')
    #limit(): 前几条
    #offset(): 跳过前几条
    users = User.query.offset(3).limit(4); #跳过前三条, 取之后的第四条数据
    print(list(users))

    print('----------------------')
    users = User.query.order_by('age') #升序
    print(list(users))
    #降序 需要导包
    from sqlalchemy import desc
    users = User.query.order_by(desc('age'))
    print(list(users))

    print('----------------------')
    #逻辑运算, and_, or_, not_(取反)
    users = User.query.filter(User.age>20, User.age<25) #年龄20 - 25
    #使用前 导包
    from sqlalchemy import and_,or_,not_
    users = User.query.filter(and_(User.age>20,User.age<25))
    users = User.query.filter(or_(User.age>25,User.age<20))
    users = User.query.filter(not_(or_(User.age>25,User.age<20)))
    users = User.query.filter(not_(User.age>25))
    print(list(users))

    print('----------------------')
    #查询属性
    #contain('')  模糊查找sql的like
    users = User.query.filter(User.name.contains('蔡'))
    print(list(users))
    #in_
    users = User.query.filter(User.age.in_( [10,20,30,40,50,60] ))
    print(list(users))

    print('----------------------')
    #startswith()
    users = User.query.filter(User.name.startswith( ['蔡'] ))
    print(list(users))
    users = User.query.filter(User.name.endswith( ['坤']))
    print(list(users))

    print('----------------------')
    #__gt__: 大于
    #__ge__: 大于等于
    users = User.query.filter(User.age.__gt__(20))
    print('大于20的:',list(users))

    return 'success'
'''
普通分页
1, 手动翻页
    offset().limit()
    数据, 1,2,3,4,5....
    页码: page = 1
    每页数量: per_page=5
    1-5   offset().limit(5)
    6-10   offset(5).limit(5)
    11-15   offset(10).limit(5)
    16-20   offset(15).limit(5)
    ...
    page=n   offset( (page-1) * per_page).limit(per_page)
    
2, paginate对象

'''
# @blue.route('/paginate/<page>/<per_page>') #这样也可以传递参数
@blue.route('/paginate/')
def get_paginate():
    #页码, 默认显示第一页
    page = request.args.get('page',1)
    #per_page, 每页显示的数据
    per_page = request.args.get('per_page',5);
    print(page,type(page))
    print(per_page,type(per_page))# 5 <class 'int'>

    page = int(page)
    per_page = int(per_page)

    #paginate()
    p = User.query.paginate(page=page, per_page=per_page,error_out=False)
    '''
    返回的paginate对象属性
        paginate对象的属性:
        items:返回当前页的内容列表
        has_next:是否还有下一页
        has_prev: 是否还有上一页
        next(error_out=False): 返回下一页的Pagination对象
        prev(error_out=False): 返回上一页的Pagination对象
        page: 当前页的页码(从1开始)
        pages: 总页数
        per_page: 每页显示的数量
        prev_num: 上一页页码数
        next_num: 下一页页码数
        query: 返回创建该Pagination对象的查询对象   没有这个属性了
        total: 查询返回的记录总数
    '''
    print(p.items)
    print(p.has_next)
    print(p.has_prev)
    print(p.next(error_out=False).items);
    print(p.prev(error_out=False).items);

    print(p.page)#返回当前的页码
    print(p.pages)
    print(p.per_page)
    print(p.prev_num)
    print(p.next_num)

    print('-------------------')
    # print(p.query)  #没有这个属性了
    print(p.total)
    return render_template('template.html',p=p)
















