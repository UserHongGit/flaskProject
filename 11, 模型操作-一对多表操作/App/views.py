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

#一对多
#增加数据
@blue.route('/addgrade/')
def add_grade():
    #添加班级
    grades = []
    for i in range(10):
        grade = Grade()
        grade.name = f'Jay{i} - {str(random.randint(10,99))}'
        grades.append(grade)
    try:
        db.session.add_all(grades)
        db.session.commit()
    except Exception as e:
        print('e:',e)
        db.session.rollback()
        db.session.flush()
    return "ok";

@blue.route('/addstu/')
def add_student():
    #添加班级
    students = []
    for i in range(10,20):
        stu = Student()
        stu.name = f'Jolin{i}'
        stu.age = 1
        stu.gradeid = random.randint(1,10)
        students.append(stu)
    try:
        db.session.add_all(students)
        db.session.commit()
    except Exception as e:
        print('e:',e)
        db.session.rollback()
        db.session.flush()
    return "ok";

#修改
@blue.route('/updatestu/')
def update_stu():
    stu = Student.query.first();
    stu.age = 100;
    db.session.commit();
    return 'ok'


#删除
@blue.route('/delstu/')
def del_stu():
    stu = Student.query.first()
    db.session.delete(stu)
    db.session.commit();
    return 'ok'

#删除班级, 班级关联学生
# 学生外键关联班级的id主键, 如果直接删除班级主键id = 2 的数据, 同步的会将从表的id=2的外键数据都置为null, 从表的数据不会删除
@blue.route('/del_grade/')
def del_grade():
    grade = Grade.query.filter_by(id=2).first()
    print(grade)
    db.session.delete(grade)
    db.session.commit();
    return 'ok'

@blue.route('/getstu/')
def get_stu():
    #查询某学生所在的班级
    stu = Student.query.get(8)
    print(stu.name,stu.age)
    print(stu.grade)  #使用Grade类里配置的反向链接
    print(stu.grade.name,str(stu.grade.id))

    #查找某班级下的所有学生
    print('---------------')
    grade = Grade.query.get(6)
    print(grade.name)
    print(grade.students) #反向查找该班级下的所有学生

    return "ok"













