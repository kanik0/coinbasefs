# Coinbase Failsafe
A simple Coinbase wallet manager written in Python.
The script periodically checks the value of Bitcoin (in USD/EUR/..) and sells all your BTCs in case of a dramatic drop of their value. The sell order is triggered when the value of Bitcoin goes below a certain margin_value, that is defined as percentage of the maximum value Bitcoin has ever reached since you launched the script.

# Install
- Create new Coinbase API keys at https://www.coinbase.com/settings/api . You need both the public and the private key. When asked for permissions, please choose at least: 
```
wallet:sells:create
wallet:accounts:create
wallet:accounts:read
wallet:transactions:send
wallet:transactions:read
wallet:addresses:create
```

- Clone/download the repository. On Linux/MacOS you can clone it with
```bash
git clone https://github.com/massimobedini/coinbasefs.git
```
  or download the zip file: https://github.com/massimobedini/coinbasefs/archive/master.zip

- Install the dependencies for python:
```
pip install coinbase

# or

easy_install coinbase
```

- Edit the script: complete the configuration by putting you api keys in `apy_key` and `api_secret` values inside the script.

- Now you are ready to go. Run the program with `python coinbasefs.py`:
```bash
$:~/coinbasefs$ python coinbasefs.py
###################################
 .(-._. ~Coinbase Failsafe~ ._.-). 
###################################

[*] Wait time is set to 10 seconds.
[*] Acceptable relative loss from maximum is set to 10 %.
[*] The currency code chosen is EUR.
[*] Connecting to Coinbase..
[*] Connected. You currently have BTC 0.00081941. Starting..

Current value of Bitcoin: 8738.73 EUR. The current maximum is 8738.73 EUR and the SELL value is currently set to 7864.86 EUR.
Current value of Bitcoin: 8738.73 EUR. The current maximum is 8738.73 EUR and the SELL value is currently set to 7864.86 EUR.
Current value of Bitcoin: 8738.73 EUR. The current maximum is 8738.73 EUR and the SELL value is currently set to 7864.86 EUR.
Current value of Bitcoin: 8753.40 EUR. The current maximum is 8753.4 EUR and the SELL value is currently set to 7878.06 EUR.
[...]
```
