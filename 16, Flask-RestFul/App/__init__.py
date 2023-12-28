
from flask import Flask
from .exts import init_exts
from .urls import *

def create_app():
    app = Flask(__name__)

    #配置数据库
    db_uri = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
        'root', 'jia', '192.168.255.128', '3306', 'py-flaskdb'
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #初始化插件
    init_exts(app=app)

    return app;



