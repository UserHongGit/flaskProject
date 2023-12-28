from flask import jsonify
from flask_restful import Resource,fields,marshal_with,reqparse

#类视图:
#视图函数
#简单使用
class HelloResource(Resource):
    def get(self):
        return jsonify({'msg':'get请求'})

    def post(self):
        return jsonify({'msg':'post请求'})



#Flask-RESTful
#字段格式化: 定义返回给前端的数据格式
#定义返回格式
response_fields = {
    'status':fields.Integer
    ,'msg':fields.String
    ,'data':fields.String
    ,'like':fields.String(default='ball') #如果返回的数据没有, 就会赋一个默认值
    ,'like2':fields.String()  #如果返回的数据没有, 会自动带着, 但是value是null
    ,'data2':fields.String(attribute='data') #返回给前端的是data2, 但是实际程序里是data,做一个伪装
}

class UserResource(Resource):
    @marshal_with(response_fields)  #必须加这个, 上边的response规则才起作用
    def get(self):
        return {
            "status":200,
            "msg":"ok"
            ,'data':'UserResource的response!'
        }




# --------------------------------------------
#定义返回的是嵌套对象
from .models import *

author_fields = {
    'name':fields.String
    ,'age':fields.Integer
    ,'sex':fields.Boolean
}
response_fields2 = {
    'status':fields.Integer
    ,'msg':fields.String
    ,'data':fields.Nested(author_fields)
}
class ModelResource(Resource):
    @marshal_with(response_fields2)
    def get(self):
        author = Author.query.first();
        print(author.name)
        return {
            'status':200
            ,'msg':'成功'
            ,'data':author
        }





# -----------------------------------------
# 定义返回的数据携带url信息
response_fields3 = {
    'status':fields.Integer
    ,'msg':fields.String
    ,'url':fields.Url(endpoint='id') #fields.Url就是将当前数据的API暴露出来, 提供url
    ,'url2':fields.Url(endpoint='id',absolute=True) #absolute返回绝对路径
}

class UrlResource(Resource):
    @marshal_with(response_fields3)
    def get(self):
        return {
            "status":200,
            "msg":"ok"
            ,'data':'UserResource的response!'
        }




#------------------------
# 定义response里, 是List嵌套对象
author_fields2 = {
    'name':fields.String
    ,'age':fields.Integer
    ,'sex':fields.Boolean
}
response_fields4 = {
    'status':fields.Integer
    ,'msg':fields.String
    ,'data':fields.List(fields.Nested(author_fields2))
}
class ModelListResource(Resource):
    @marshal_with(response_fields2)
    def get(self):
        authors = Author.query.all()
        return {
            'status':200
            ,'msg':'成功'
            ,'data':authors
        }

#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#--------------------------参数解析----------------------------------

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='name是必填参数!')
parser.add_argument('name', type=int, action='append', help='age是必填参数!') #可以有多少age参数
parser.add_argument('cookies_key',type=str,location='cookies')   #获取cookies中的数据

class ParamResource(Resource):
    def get(self):
        args = parser.parse_args()  #必须加了这句, 上边定义的规范才起作用
        name = args.get('name')
        age = args.get('age');

        cookies_key = args.get('cookies_key')
        return jsonify({'name':name})












