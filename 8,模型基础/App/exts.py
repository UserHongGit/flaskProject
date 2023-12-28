# exts.py  插件管理, 专门存放插件的地方
#拓展的第三方插件都在这里

#1, 导入第三方插件
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#2, 初始化
db = SQLAlchemy()  #ORM
migrate = Migrate()  #数据迁移

#3, 和app对象绑定 相当于上边的db, migrate插件对象和__init__.py里的app对象进行绑定
#可以直接在__init__.py里直接importdb和migrate对象, 但是这样不太好, 这里直接定义一个函数, 到时候直接引入这个函数, 保证初始化只初始化一次
def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)



