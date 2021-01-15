# CONSULTA COTAÇÃO ATUAL DO BITCOIN NAS EXCHANGES
import requests, json

"""
Padrão Json
"market":"BTC-BRL",
"last":99448,
"high":100280.18,
"low":97854,
"vol":21.76542692,
"avg":99240.3,
"var":2.48,
"buy":99306.9,
"sell":99398.88,
"timestamp":"2020-12-06 00:46:02"
"""

#Imprimindo o último preço Bitcoin
req_btc = requests.get('https://api-simulator.bitpreco.com/btc-brl/ticker')
Bitcoin = json.loads(req_btc.text)
print('Último preço Bitcoin:', Bitcoin['last'])

#Imprimindo o último preço Ethereum
req_eth = requests.get('https://api-simulator.bitpreco.com/eth-brl/ticker')
Ethereum = json.loads(req_eth.text)
print('Último preço Ethereum:', Ethereum['last'])

#Imprimindo o último preço de Dólares
req_usdt = requests.get('https://api-simulator.bitpreco.com/usdt-brl/ticker')
Dolar = json.loads(req_usdt.text)
print('Último preço Dólar:', Dolar['last'])