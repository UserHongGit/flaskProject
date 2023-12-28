#urls.py  路由文件

from .exts import api
from .apis import *

api.add_resource(HelloResource,'/hello_resource/')
api.add_resource(UserResource,'/user_resource/')
api.add_resource(ModelResource,'/model_resource/')
api.add_resource(UrlResource,'/url_resource/',endpoint='id')
api.add_resource(ModelListResource,'/models_resource/')


#参数解析
api.add_resource(ParamResource,'/param/')

