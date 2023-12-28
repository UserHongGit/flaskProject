#views.py: 存放 路由+视图函数
import random

from flask import Blueprint,request,render_template,\
    jsonify,make_response,Response,redirect,url_for

#一定要导入model, 不然model.py不会执行
from . models import *
#创建蓝图
blue = Blueprint('book_blue',__name__)

@blue.route('/')
@blue.route('/book_index/')
def book_index():
    return render_template('template.html')

@blue.route('/book_list/')
def book_list():
    books = Book.query.all();
    return render_template('book_list.html',books = books)

@blue.route('/book_detail/<book_id>/')
def book_detail(book_id):
    book = Book.query.get(book_id)
    return render_template('book_detail.html',book = book)

@blue.route('/author_detail/<author_id>/')
def author_detail(author_id):
    author = Author.query.get(author_id)
    return render_template('author_detail.html',author = author)

@blue.route('/pub_detail/<pub_id>/')
def pub_detail(pub_id):
    pub = Publisher.query.get(pub_id)
    return render_template('publisher_detail.html',pub = pub)

