from novadax import RequestClient as NovaClient

# Funções de acesso a a api da NovaDax. de uma forma simplificada. 
# É só chamar pelo comando import

nova_client = NovaClient('access_key', 'secret_key')

#Configurando a key de acesso API
def Key(access_key = '', secret_key = ''):
    nova_client = NovaClient(access_key, secret_key)

# Dados de um símbolo (par) específico
def Simbolo(simbolo):
    return nova_client.get_symbol(simbolo)

# Todos os símbolos (pares)
def Simbolos():
    return nova_client.list_symbols()

# Hora atual do sistema
def HoraAtual():
    return nova_client.get_timestamp()

# Obter dados de ticker de todos os pares de negociação
def Tickers():
    return nova_client.list_tickers()

# Obter dados de ticker de um par de negociação específico (Ex: 'BTC_BRL')
def TickerSimbolo(simbolo):
    return nova_client.get_ticker(simbolo)

# Retorna informações de livro de ofertas para um par específico.
def Livro(simbolo, limite = 10):
     return nova_client.get_depth(simbolo, limite)

# Retorna informações das negociações realizadas recentemente.
def Traders(simbolo, limite = 10):
    return nova_client.list_trades(simbolo, limite)

# Obter dados de candlestick
# TIMEFRAME = (ONE_MIN, FIVE_MIN, FIFTEEN_MIN, HALF_HOU, ONE_HOU, ONE_DAY, ONE_WEE, ONE_MON)
def Candle(simbolo, inicio, fim, timeframe = 'ONE_MIN'):
    return nova_client.get_kline(simbolo, timeframe, inicio, fim)

# Abre uma ordem limitada de compra e a envia para livro de ofertas para sua execução.
def BuyLimit(simbolo, preco, montante):
    return nova_client.create_order(simbolo, 'LIMIT', 'BUY', price = str(preco), amount = str(montante))

# Abre uma ordem limitada de venda e a envia para livro de ofertas para sua execução.
def SellLimit(simbolo, preco, montante):
    return nova_client.create_order(simbolo, 'LIMIT', 'SELL', price = str(preco), amount = str(montante))

# Abre uma ordem a mercado de compra e a envia para livro de ofertas para sua execução.
# Valor é da moeda de destino. Ex: '10' reais em BTC_BRL
def Buy(simbolo, valor):
    return nova_client.create_order(simbolo, 'MARKET', 'BUY', value = str(valor))

# Abre uma ordem a mercado de venda e a envia para livro de ofertas para sua execução.
def Sell(simbolo, montante):
    return nova_client.create_order(simbolo, 'MARKET', 'SELL', amount = str(montante))

# Solicita o cancelamento de uma ordem.
def Cancelar(ordem):
    return nova_client.cancle_order(str(ordem))

# Retorna os detalhes atualizados de uma ordem. 
def Ordem(ordem):
    return nova_client.get_order(str(ordem))

# Retorna o histório de ordens de acordo com o filtro informado
# Status da ordem: (FINISHED, SUBMITTED, PROCESSING, PARTIAL_FILLED, CANCELING, FILLED, CANCELED e REJECTED)
def Ordens(simbolo, inicio, fim, tipo = 'FINISHED', quant = 100):
    return nova_client.list_orders(simbolo, tipo, str(inicio), str(fim), str(quant))

# Retorna o resultado da execução de uma ordem.
def OrderResult(ordem):
    return nova_client.list_order_fills(str(ordem))

# Retorna os saldos das moedas da sua conta.
def Saldos():
    return nova_client.get_account_balance()

# Sacar criptomoedas
# EX: moeda = 'BTC', valor = 1, endereço da carteira = '0sdfsdfsdfsd'
def Sacar(moeda, valor, endereco):
    return nova_client.withdraw_coin(moeda,valor,endereco)

# Listar sub-contas
def SubContas():
    return self.api.subs()

# Saldo da sub-conta
def SaldoSub(subId):
    return self.api.subs_balance(subId)

# Histórico de transferência da sub-conta
def HistoricoSub(subId):
    return self.api.subs_transfer_record(subId)

# Transferência da sub-conta
def TranferSub(subId, assetCode, transferAmount, transferType):
    return self.api.subs_transfer(subId, assetCode, transferAmount, transferType)


# Registros de depósito e saque de carteira
def Registros():
    return nova_client.wallet_deposit_withdraw_record()

