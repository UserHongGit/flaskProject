from .exts import db


'''
多表关系
    对对多
        用户:电影  =  N:N
'''
#中间表 : 收藏表, 用户收藏电影, 电影被用户收藏
collect = db.Table(
    'collects'
    ,db.Column('user_id',db.Integer,db.ForeignKey('usermodel.id'),primary_key=True)
    ,db.Column('movie_id',db.Integer,db.ForeignKey('moviemodel.id'),primary_key=True)
)
#用户表
class UserModel(db.Model):
    __tablename__ = 'usermodel'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)

#电影表
class MovieModel(db.Model):
    __tablename__ = 'moviemodel'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))

    #关联
    #secondary = collect: 设置中间表
    users = db.relationship('UserModel',backref='moviemodels',lazy='dynamic',secondary=collect)
    '''
    Lazy属性:
            懒加载，可以延迟在使用关联属性的时候才建立关联
            Lazy='dynamic: 会返回一个query对象(查询集)，可以继续使用其他查询方法，如alL().
            Lazy='select': 首次访问到属性的时候，就会全部加载该属性的数据
            Lazy='joined':在对关联的两个表进行join操作，从而获取到所有相关的对象
            Lazy=True: 返回一个可用的列表对象，同select
    '''




















