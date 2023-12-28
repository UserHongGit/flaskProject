from flask import Flask,render_template,jsonify
from werkzeug.utils import cached_property

# __name__ 表示当前目录层级就是, 整个项目的基础目录
app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return 'Flask Home!'

#前边的/必须加, 后边的可以不加, 但是建议后边的也加上
@app.route('/index/')
def index():
    return '<b>Index 首页<b>' #可以直接返回标签, 前端直接渲染页面

@app.route('/index/render')
def index_render():
    return render_template('login.html',name='传参测试数据')

@app.route('/index/json')
def index_json():
    #可以直接返回json对象, 但是一般会使用jsonify将对象转成字符串, 返回给前端
    return jsonify({'name':'张三','age':20})


if __name__ == '__main__':
    #启动服务器
    # app.run()
    app.run(debug=True,port=666,host='0.0.0.0')
    '''
    run() 启动的时候, 可以添加参数:
        debug  是否开启调试模式, 开启后修改过的python代码会自动重启
        port 指定启动端口, 默认5000
        host 默认127.0.0.1, 指定0.0.0.0代表本机所有IP
    '''

