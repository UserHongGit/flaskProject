from flask import Flask,render_template,jsonify
from werkzeug.utils import cached_property




from App import create_app

#因为Flask的应用已经放在了App包下, 这里拿不到了, 所以需要导包, 导入之后直接拿到app对象
app = create_app()

if __name__ == '__main__':
    #启动服务器
    app.run(debug=True,port=6666)

