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


