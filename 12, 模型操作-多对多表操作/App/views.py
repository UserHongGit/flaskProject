#views.py: 存放 路由+视图函数
import random

from flask import Blueprint,request,render_template,\
    jsonify,make_response,Response,redirect,url_for

#一定要导入model, 不然model.py不会执行
from . models import *
#创建蓝图
blue = Blueprint('user',__name__)

@blue.route('/')
def index():
    return 'index'

#多表操作

#多对多
#增加数据
@blue.route('/adduser/')
def add_user():
    #添加用户
    users = []
    for i in range(10,14):
        user = UserModel()
        user.name = f'Lucy{i}'
        user.age = i
        users.append(user)
    try:
        db.session.add_all(users)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.flush()
    return 'ok'

#增加数据
@blue.route('/addmovie/')
def add_movie():
    #添加电影
    movies = []
    for i in range(10,14):
        movie = MovieModel()
        movie.name = f'阿凡达-{i}'
        movies.append(movie)
    try:
        db.session.add_all(movies)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.flush()
    return 'ok'

#增加中间表数据
@blue.route('/add_collect/')
def add_collect():
    #用户收藏电影
    user = UserModel.query.get(1)
    movie = MovieModel.query.get(1)

    user.moviemodels.append(movie)
    db.session.commit()

    return 'ok';

'''
需要的数据
INSERT INTO `collects` VALUES (1, 1);
INSERT INTO `collects` VALUES (1, 2);
INSERT INTO `collects` VALUES (1, 3);
INSERT INTO `collects` VALUES (1, 4);
INSERT INTO `collects` VALUES (2, 4);
INSERT INTO `collects` VALUES (3, 4);
INSERT INTO `collects` VALUES (4, 4);
'''
#查询
@blue.route('/get_collect/')
def get_collect():
    #查询某位用户收藏的电影
    user = UserModel.query.get(1)
    print(user.moviemodels)

    #查找收藏了某电影的所有用户
    movies = MovieModel.query.get(4)
    print(movies.users)
    print(list(movies.users))
    return 'ok';

#修改: 和单标操作一样
#删除
@blue.route('/del_user')
def del_user():
    #删除用户时, 将对应的关系表collect表里的1用户数据都会删除掉
    #movie电影并不影响
    user = UserModel.query.get(1)
    db.session.delete(user)
    db.session.commit()

    return 'ok'

