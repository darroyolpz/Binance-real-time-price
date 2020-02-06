import json, requests, time, os

# https://www.binance.com/en/trade/WRX_USDT

'''
Go to https://www.binance.com/en/trade/COIN_USDT and wait until at least 1m chart is available
Otherwise you could be easily buying the top or losing a clear downside rejection
'''

# Data
coin = 'WRX'
fees = 1-0.1/100
url = 'https://api.binance.com/api/v3/ticker/price?symbol=' + coin + 'USDT'

# Trades executed. Limit price and Amount
trades = [[0.06, 3000]]

while True:

	# Get the coin price
	response = requests.get(url).text
	value = json.loads(response)
	actual_price = float(value['price'])

	# Get figures
	asset_size = sum([trade[1]/trade[0] for trade in trades])*fees
	position_size = sum([trade[1] for trade in trades])
	be_price = (position_size / asset_size) / fees
	net_balance = position_size * (actual_price - be_price) / be_price

	print('Asset size:', asset_size)
	print('Position size:', position_size)
	print('Break-even price:', be_price)
	print('-----------------------------')
	print('Actual', coin, 'price:', actual_price)
	print('Net balance:', net_balance)
	print('\n')

	# Go to sleep
	time.sleep(2)
	#os.system('clear')