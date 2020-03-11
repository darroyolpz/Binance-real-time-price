import json, requests, time, os

'''
Go to https://www.binance.com/en/trade/COIN_USDT and wait until at least 1m chart is available
Otherwise you could be easily buying the top or losing a clear downside rejection
'''
total_net = 0

def profit(coin, trades, total_net):
	# Exchange
	fees = 1-0.1/100
	url = 'https://api.binance.com/api/v3/ticker/price?symbol=' + coin + 'USDT'

	# Get the coin price
	response = requests.get(url).text
	value = json.loads(response)
	actual_price = float(value['price'])

	# Get figures
	asset_size = sum([trade[1]/trade[0] for trade in trades])*fees
	position_size = sum([trade[1] for trade in trades])
	be_price = (position_size / asset_size) / fees
	net_balance = position_size * (actual_price - be_price) / be_price
	total_net += net_balance

	print('Asset size:', asset_size)
	print('Position size:', position_size)
	print('Break-even price:', be_price)
	print('-----------------------------')
	print('Actual', coin, 'price:', actual_price)
	print('Net balance:', net_balance)
	print('\n')

	return total_net

# Data
coin = 'COCOS'
trades = [[0.000480, 999.99]]
total_net = profit(coin, trades, total_net)

coin = 'BTT'
trades = [[0.0003817, 244], [0.0003830, 2000.52]]
total_net = profit(coin, trades, total_net)

coin = 'FET'
trades = [[0.0344, 1575]]
total_net = profit(coin, trades, total_net)

print('----------------------')
print('Total net:', total_net)
print('----------------------')