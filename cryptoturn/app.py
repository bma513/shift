from flask import Flask
from flask import request
from totalvoice.cliente import Cliente
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def init():
    str = open('templates/index.html', 'r').read()
    return str

@app.route('/generatetoken', methods=['POST'])
def getToken():
    email = request.form['email']
    name = request.form['name']

    return '698dc19d489c4e4db73e28a713eab07b'

@app.route('/listtokens', methods=['GET', 'POST'])
def listToken():

    return {'source_tokens':['BTC'],'final_tokens': ['ETH','IOTA','XRP']}

@app.route('/sendsms', methods=['GET', 'POST'])
def sms():
    phone = request.form['email']
    message = request.form['name']
    client = Cliente('96d3610203e0fdc31009c2694afe135c', 'https://api2.totalvoice.com.br/sms')  # ex: api.totalvoice.com.br
    response = client.sms.enviar(phone, message)

    return response

@app.route('/convert')
def convert():
    source_coin = request.args.get('source_coin')
    source_amount = request.args.get('source_amount')
    final_coin = request.args.get('final_coin')

    r = requests.get('https://api.bitfinex.com/v1/trades/'+final_coin+source_coin+'?limit_trades=1')

    price=1/float(json.loads(r.text)[0]['price'])

    response = {'generated_wallet_address':'1BoatSLRHtKNngkdXEeobR76b53LFTtpyT', 'final_amount':int(source_amount)*price}

    return response

if __name__ == '__main__':
    app.run()
