from flask import Flask
from flask_sock import Sock

app=Flask(__name__)
sock=Sock(app)

@sock.route('/echo')
def echo(ws):
    while True:
        message=ws.receive()
        if message:
            print("Received: ", message)
            ws.send(message)
        else:
            break

if __name__=="__main__":
    app.run(host="localhost", port=5000)