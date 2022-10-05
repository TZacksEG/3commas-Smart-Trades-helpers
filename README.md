# 3commas-Smart-Trades-helpers
Scripts for using 3commas Smart Trade with Risk Management

Most of us fail in Crypto Day Trading Due to Bad risk management. 
therefore, these Scripts were created 

# How it works?
I have designed these scripts to risk a certain amount per trade depend on your capital and also adjust the position value depend on your stoploss 
works for spot and futures **ONLY USDT Market**

# Explaination 

**capital** = $20K

**risk per trade** = 1 % = $200 ( adjustable in the script ) risk whatever you want 

assuming you entering a BTC long position with 5% stoploss 

**Your Position value** will be calculated in that way ( risk per trade / Stoploss % ) so its 200/5% = **$4,000**

BTC would have to drop 5% in price to lose the **Risk Per trade value** which in our case is **1% of the capital or $200**

******************
but if you LONG BTC with stoploss of 2% 

**Your Position value** will be calculated in that way ( risk per trade / Stoploss % ) so its 200/2% = **$10,000**
BTC would have to drop 2% in price to lose the **Risk Per trade value** which in our case is **1% of the capital or $200**

**so your risk amount per trade stays the same , no matter how small/big stoploss you use .
**



there are 2 different scripts 
* Smart_Trade_fixed_TPs.py
* Smart_Trade_with_RR.py
