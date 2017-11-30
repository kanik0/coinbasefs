# Coinbase Failsafe
A simple Coinbase wallet manager written in Python.
The script periodically checks the value of Bitcoin (in USD/EUR/..) and sells all your BTCs in case of a dramatic drop of their value. The sell order is triggered when the value of Bitcoin goes below a certain margin_value, that is defined as percentage of the maximum value Bitcoin has ever reached since you launched the script.

# Install
- Clone/download the repository. On Linux/MacOS you can clone it with
```bash
git clone https://github.com/massimobedini/coinbasefs.git
```
or download the zip file: https://github.com/massimobedini/coinbasefs/archive/master.zip

