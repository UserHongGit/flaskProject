from App import create_app

app = create_app()

if __name__ == '__main__':
    #启动服务器
    app.run(debug=True,port=6666)

