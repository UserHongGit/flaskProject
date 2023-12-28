from flask import Flask
from werkzeug.utils import cached_property

# __name__ 表示当前目录层级就是, 整个项目的基础目录
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

#前边的/必须加, 后边的可以不加, 但是建议后边的也加上
@app.route('/index/')
def index():
    return 'Index 首页'

if __name__ == '__main__':
    #启动服务器
    app.run()
