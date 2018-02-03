from flask import Flask
from flask import request

#WA[
from whatsapp import Client
#expected_token = 'SOME SECRET TOKEN OF YOUR CHOICE'
expected_token = 'jmdmatadi'
#]WA

app = Flask(__name__)



@app.route('/')
def hello_world():

    return 'Hello World!'

@app.route('/msg', methods = ['POST'])
def msg():
    to = request.form['to']
    return str(to)

@app.route('/sendmsg')
def sendmsg():
    #to = request.args.get('to')
    to = '8376966864'
#    msg = request.args.get('msg')
    msg = 'Hellow world!!!'
  #  token = request.args.get('token')
    token = 'jmdmatadi'
    if(str(token) == expected_token):
        client = Client(login='8076284641', password='fTHUL2A4y0zfOfCDjWy8v6p8U1I=')
        res = client.send_message(to, msg)  
    
    else:
        res = 'Unauthorized'
    
    return str(res)

if __name__ == '__main__':
    app.run()
