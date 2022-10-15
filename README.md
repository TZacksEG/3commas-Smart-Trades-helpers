# 3commas-Smart-Trades-helpers
Scripts for using 3commas Smart Trade with Risk Management

Most of us fail in Crypto Day Trading Due to Bad risk management. 
therefore, these Scripts were created 
******************
# How it works?
I have designed these scripts to risk a certain amount per trade with self adjusting position Size/value with 
Risk-Reward Ratio or Multi Take profit levels system , **controlled via Telegram** 


Works for spot and futures **USDT Market ONLY**  ( LONG and SHORT ) with Break-even Feature.


# Explanation of The Money management Strategy

Assuming your **capital** is $20K  

if you enter a BTC long position with **5% stoploss** without any risk management you lose $1,000 . too big ?! if yes then here comes the Risk management part

Your **risk per trade** = 1% of capital  = $200

**Your Position value** will be calculated and adjusted to match your stoploss USD value so your Position value will be  = **$4,000**

BTC would need to drop 5% in price value in order to lose the **Risk Per trade value** which is in our case is **1% of the capital = $200**

**so your risk USD value per trade stays the same , no matter how small/big your stoploss is**

and SO ON . 

*****************************

# Take profit

**We have 2 Scripts with different Take profit strategies**
* **Fixed Tps** which is [Smart_Trade_fixed_TPs.py](https://github.com/TZacksEG/3commas-Smart-Trades-helpers/wiki/Smart-Trade-with-Fixed-TP's-level) Fixed % of Tps (adjustable) .

  you can set whatever % of tps you want: 2% and 5% and 10% Up to 5 TP's levels. 


* **Risk-Reward Ratio** which is [Smart_Trade_with_RR.py](https://github.com/TZacksEG/3commas-Smart-Trades-helpers/blob/main/Smart_Trade_with_RR.py) RR Strategy. 

  it calculates your profit automatically using the value of the stoploss used in the trade.

  **Default RR is 1 to 2.4 RR, so you lose 1 dollar to earn $2.4**

**BOTH OF the scripts have a Break-even feature which will automatically MOVE your Stoploss level to entry when first TP is Reached**


**********************

# How to use?
* if you want to run the whole operation automatically 
  - BY automatically Open trades Via sending alerts from Tradingview 
  to your Telegram Channel and then Telegram to **3commas**
  - then you need to have your own webhook server to manage the whole automation 
  - [Install Webhook Server](https://github.com/TZacksEG/3commas-Smart-Trades-helpers/wiki/Personal-Webhook-Setup) 


* if you want to run the smart Trades manually by sending yourself the Trades to Telegram
  - Just Send Trades manually to the Telegram Channel , where it will send your Trades to 3commas Automaticlly 
    

* Scripts
  - [Smart_Trade_fixed_TPs](https://github.com/TZacksEG/3commas-Smart-Trades-helpers/wiki/Smart-Trade-with-Fixed-TP's-level)
  - [Smart_Trade_with_RR ( RISK and REWARD )](https://github.com/TZacksEG/3commas-Smart-Trades-helpers/wiki/Smart-Trades-with-RR-(-RISK-and-REWARD-))
  

# 

**********************
# 

# Installation

* Get a VPS i recommend  [Contabo.com](https://contabo.com/en/)
* need python3.7 or higher
* git clone https://github.com/TZacksEG/3commas-Smart-Trades-helpers.git
* pip install -r requirements.txt
* **python3 Smart_Trade_fixed_TPs.py** 
* OR
* **python3 Smart_Trade_with_RR.py**
* **if Webhook is Needed then python3 webhook.py**
