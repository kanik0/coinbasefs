from __future__ import print_function
import datetime
from time import sleep
from coinbase.wallet.client import Client

# Configuration
api_key = 'null'        # Your API key
api_secret = 'null'     # Your API secret key
version = '2017-10-31'  # API version, don't change this
currency_code = 'EUR'   # Currency code, default is EUR
margin = 15             # Acceptable relative loss from maximum,
                        # expressed as percentage %, default is 15%
time_delay = 15         # Delay in seconds, default is 15 seconds

# Config check
if api_key == 'null' or api_secret == 'null':
    print('Please specify your API key and secret key inside the script.')
    quit()

# Connect to Coinbase
print('###################################')
print(' .(-._. ~Coinbase Failsafe~ ._.-). ')
print('###################################')
print('')
sleep(1)
print('[*] Wait time is set to %s seconds.' % (time_delay))
print('[*] Acceptable relative loss from maximum is set to %s %%.' % (margin))
print('[*] The currency code chosen is %s.' % (currency_code))
print('[*] Connecting to Coinbase..')

# Connects to Coinbase
client = Client(api_key, api_secret, api_version=version)
# Gets primary account
account = client.get_primary_account()
price = client.get_spot_price(currency=currency_code)
# DA GUARDARE MEGLIO
payment_method = client.get_payment_methods()[2]
print('[*] Connected. You currently have %s. Starting..' % (account.balance))
print('')

# Defines starting maximum value
max_price = float(price.amount)
# Defines starting acceptable loss
margin_value = (1 - float(margin) / 100) * max_price
sleep(5)


# Main code
while True:

    try:
        account = client.get_primary_account()
        # Updates data
        balance = account.balance
        price = client.get_spot_price(currency=currency_code)

        if float(price.amount) < margin_value:
            sell = account.sell(total=account.balance,
                                currency='BTC',
                                payment_method=payment_method.id)

            print('The price is %s %s, SELLING everything!' %
                  (price.amount, currency_code))
            print('%s - Transaction ID: %s.' %
                  str(datetime.datetime.now()).split('.')[0], sell.id)
            print('Quitting..')
            quit()

        if float(price.amount) > max:
            max_price = float(price.amount)

        margin_value = (1 - float(margin) / 100) * max_price

        print('Current value of Bitcoin: %s %s.'
              'The current maximum is %s %s and the SELL value is '
              'currently set to %.2f %s.'
              % (price.amount, currency_code, max_price, currency_code,
                  margin_value, currency_code))

        sleep(time_delay)

    except Exception as error:
        print('An error occured, Coinbase might be down (ERR: %s).'
              'Trying again in 10 seconds..' % error)

        sleep(10)
