import os.path

from flask import Flask
from .views import blue
from .exts import init_exts


#项目目录
#__file__ 当前文件下的abspath绝对路径的dirname所在目录,
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('BASE_DIR:',BASE_DIR)

def create_app():
    #可以这么用, 但是不建议
    # static_folder = '../static'
    # template_folder = '../templates'

    #这样使用,
    static_folder = os.path.join(BASE_DIR,'static')
    template_folder = os.path.join(BASE_DIR,'templates')
    app = Flask(__name__,static_folder=static_folder,template_folder=template_folder)

    #注册蓝图
    app.register_blueprint(blueprint=blue)

    #配置数据库
    db_uri = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
        'root', 'jia', '192.168.255.128', '3306', 'py-flaskdb'
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #初始化插件
    init_exts(app=app)

    return app;



