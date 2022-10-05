# 3commas-Smart-Trades-helpers
Scripts for using 3commas Smart Trade with Risk Management

Most of us fail in Crypto Day Trading Due to Bad risk management. 
therefore, these Scripts were created 
******************
# How it works?
I have designed these scripts to risk a certain amount per trade depend on the Trading capital and also adjust the position value depend on your stoploss 
works for spot and futures **ONLY USDT Market**  ( LONG and SHORT ) also has multi Tps or Risk-Reward Ratio and Breakeven when first Tp is Reached to secure your Profit .

# Explaination 

**capital** = $20K

**risk per trade** = 1 % = $200 ( adjustable in the script ) risk whatever you want 

assuming you entering a BTC long position with 5% stoploss 

**Your Position value** will be calculated in that way ( risk per trade / Stoploss % ) so its 200/5% = **$4,000**

BTC would have to drop 5% in price to lose the **Risk Per trade value** which is in our case is **1% of the capital or $200**

but if you LONG BTC with stoploss of 2% 

**Your Position value** will be calculated in that way ( risk per trade / Stoploss % ) so its 200/2% = **$10,000**

BTC would have to drop 2% in price to lose the **Risk Per trade value** which is in our case is **1% of the capital or $200**

**so your risk amount per trade stays the same , no matter how small/big stoploss you use**

The Take profit matter has 2 options 
* **Fixed Tps** ( adjustable in the script ) you can set whatever % of tps you want exmple : 2% and 5% and 10% etc up to 5 Tp's
* **Risk-Reward Ratio** , it calculate your profit automaticlly using the value of the stoploss used in the trade .. 

**Default RR is 1 to 2.4 RR so you lose 1 dollar to earn $2.4**


there are 2 different scripts 
* **Smart_Trade_fixed_TPs.py** buys or sell at **MARKET PRICE **
* **Smart_Trade_with_RR.py** Buys or sell at **limit PRICE**
**********************
# Smart_Trade_fixed_TPs
 when you run it , it will ask fo data as shown below 
 ![image](https://user-images.githubusercontent.com/106902748/194078254-f2db452d-9c09-49bf-8cb2-e92f399d61f0.png)
 
**Configuration**
The configuration file for Smart_Trade_fixed_TPs has the following settings:

* **timezone** - timezone. (default is 'Africa/Cairo')
* **debug** - set to true to enable debug logging to file. (default is False)
* **logrotate** - number of days to keep logs. (default = 7)
* **3c-apikey** - your 3Commas API key value. [How to Create a 3commas API ?](https://help.3commas.io/en/articles/5599671-3commas-api-creating-an-api-key-for-development)

* **3c-apisecret** - your 3Commas API key secret value.
* **accounts** = your account/accounts number [how to get the account number?](https://github.com/TZEG/3commas-Smart-Trades-helpers/wiki/How-to-get-exchange-account-number-from-3commas)
* **risk-of-trade** - the % of your account balance that you will risk for each trade - default is 1%
* **Tp1** - % of your 1st TP
* **Tp2** - % of your 2nd TP
* **Tp3** - % of your 3rd TP
* **Tp4** - % of your 4th TP
* **Tp5** - % of your 5th TP
* **leverage** - are you going to use leverage Trading ? then what is your lev maybe 5 or 10 or 100? default is 1 for SPOT Trading
* **tgram-phone-number** - your Telegram phone number, needed for first time authorisation code. (session will be cached in watchlist.session)
* **tgram-api-id** - your telegram API id. [how to get Telegram App/HASH?]([https://github.com/TZEG/3commas-Smart-Trades-helpers/wiki/How-to-get-exchange-account-number-from-3commas](https://github.com/TZEG/3commas-Smart-Trades-helpers/wiki/Get-Telegram-APP-ID-and-HASH))
* **tgram-api-hash** - your telegram API hash.
* **tgram-channel** - name of the chat channel to monitor and send trades to
* **notifications** - set to true to enable notifications. (default = False) [How to setup telegram Notifications](https://github.com/TZEG/3commas-Smart-Trades-helpers/wiki/How-to-setup-telegram-Notifications)
* **notify-urls** - one or a list of apprise notify urls, each in " " seperated with commas. See [Apprise website](https://github.com/caronc/apprise) for more information.

**********************
# Smart_Trade_fixed_TPs Format

`LONG/SHORT

COIN

stoploss`

![image](https://user-images.githubusercontent.com/106902748/194093614-9ef1983f-752e-4128-b039-0d8733bc7bb8.png)

You can use CLOSE to close/Panic Sell  all your SMART trades


