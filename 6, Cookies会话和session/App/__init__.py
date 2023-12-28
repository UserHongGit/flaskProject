from flask import Flask
from .views import blue
import datetime

def create_app():
    app = Flask(__name__)

    #注册蓝图
    app.register_blueprint(blueprint=blue)

    #session配置信息

    print(app.config)  #输出Flask的配置
    app.config['SECRET_KEY'] = 'abc123'#设置session的secret_key
    #设置session的过期时间为8天
    app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=8)
    return app;




