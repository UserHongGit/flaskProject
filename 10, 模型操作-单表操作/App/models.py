from .exts import db


#类 --> 表
# 类属性 --> 表字段
# 对象 --> 表里的一条数据

class User(db.Model):
    __tablename__='tb_user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), unique=True,index=True)
    age = db.Column(db.Integer,default=1)

    #相当于toString()
    def __repr__(self):
        return self.name




