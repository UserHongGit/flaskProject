from .exts import db


'''
多表关系
    一对多
        班级:学生  - 1:N
'''
class Grade(db.Model):
    __tablename__ = 'grade' #表名
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    #建立关联: 通过班级找学生
    #参数1: 关联的模型名称(表对应的类的名字)
    #参数2: 反向引用的名称, grade对象, 用班级去调用学生
            #让student去反过来得到grade对象的名称: student.grade
    #参数3: 懒加载, 用的时候才去加载这种反向关联, 节省资源
    #这里的students不是字段, 只是一个类的属性
    students = db.relationship('Student', backref='grade',lazy=True) #自己定义, 但并不是表里的字段

    def __repr__(self):
        return 'id:' + str(self.id) + ",name:" + self.name

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    #添加  外键: 跟grade表中的id进行关联
    gradeid = db.Column(db.Integer,db.ForeignKey(Grade.id))

class Student2(db.Model):
    __tablename__ = 'student2'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)









