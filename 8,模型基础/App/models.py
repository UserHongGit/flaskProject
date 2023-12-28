#models.py: 模型, 处理数据, 和数据库相关的东西
from .exts import db

#模型Model: 就是一个类
#必须继承db.Model, 才是一个模型类, 不然就是一个普通的类
class User(db.Model):
    #表名
    __tablename__='tb_user'
    #定义表字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), unique=True,index=True)
    age = db.Column(db.Integer,default=1)
    sex = db.Column(db.Boolean,default=True)
    salary = db.Column(db.Float,default=10000,nullable=False)

'''
db.Column: 字段
db.Integer: 整数
primary_key=True 主键
autoincrement=True 自动递增
db.String(30)  varchar(30) 可变字符串
unique=True 唯一约束
index=True  普通索引
'''




