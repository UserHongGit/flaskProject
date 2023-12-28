from .exts import db
'''
图书馆项目
    作者:数据 -> 1:n  一本书只由一个作者完成, 一个作者可以创作多本书
    出版社: 书籍 -> n:n   一个出版社可以出版多本书, 一本书也可以由多个出版社出版

要求:
    1.在书籍的book_index.htm1中有一个"查看所有书籍”的超链接按钮，点击进入书籍列表book_list.html页面
    2.在书箱的book_list,htm1中显示所有书名，点击书名可以进入书箱详情book_detail.html
    3.在书箱book_detai1.html中可以点击该书的作者和出版社，进入作者详情的author_detal.html和出版社详情的publisher_detail.html页掌

'''
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer,default=1)
    sex = db.Column(db.Boolean,default=True)
    email = db.Column(db.String(50))

    #建立关系
    books = db.relationship('Book',backref='author',lazy='dynamic')

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),unique=True)
    date = db.Column(db.DateTime)

    #1对多, 外键
    author_id = db.Column(db.Integer,db.ForeignKey(Author.id))

#中间表(书籍 - 出版社)
book_publisher = db.Table(
    'book_publisher',
    db.Column('book_id',db.Integer,db.ForeignKey('book.id'),primary_key=True),
    db.Column('publisher_id',db.Integer,db.ForeignKey('publisher.id'),primary_key=True)
)

class Publisher(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True)
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    website = db.Column(db.String(100))

    #多对多, 关联book表
    books = db.relationship('Book',backref='publishers',lazy='dynamic',secondary=book_publisher)




















