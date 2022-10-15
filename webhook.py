import argparse
import configparser
import os
from pathlib import Path
import json
from telegram import Bot
import time
import sys
from flask import Flask, request


def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp


def load_config():
    """Create default or load existing config file."""

    cfg = configparser.ConfigParser()
    if cfg.read(f"{datadir}/{program}.ini"):
        return cfg

    cfg["settings"] = {
        "timezone": "Africa/Cairo",
        "debug": False,
        "logrotate": 7,
        "secret-key": 877876,
        "LONG-bot": "Telegram BOT Token for LONG alerts",
        "LONG-channel": "Telegram Channel ID for LONG alerts ",
        "SHORT-bot": "Telegram BOT Token for SHORT alerts",
        "SHORT-Channel": "Telegram Channel ID for SHORT alerts ",
    }
    with open(f"{datadir}/{program}.ini", "w") as cfgfile:
        cfg.write(cfgfile)

    return None


def send_alert(data):
    msg = data["msg"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    if "SHORT" in msg:
        tg_bot = Bot(token=str(config.get("settings", "SHORT-bot")))
        msg = msg.replace("--", "\n")
        try:
            tg_bot.sendMessage(
                data["telegram"],
                msg,
                # parse_mode="MARKDOWN",
            )
            print(get_timestamp(), f"Alert Received & Sent!")
        except KeyError:
            tg_bot.sendMessage(
                int(config.get("settings", "SHORT-Channel")),
                msg,
                # parse_mode="MARKDOWN",
            )
            print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
    elif "LONG" in msg:
        tg_bot = Bot(token=str(config.get("settings", "LONG-bot")))
        msg = msg.replace("--", "\n")
        try:
            tg_bot.sendMessage(
                data["telegram"],
                msg,
                # parse_mode="MARKDOWN",
            )
            print(get_timestamp(), f"Alert Received & Sent!")
        except KeyError:
            tg_bot.sendMessage(
                int(config.get("settings", "LONG-Channel")),
                msg,
                # parse_mode="MARKDOWN",
            )
            print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
        except Exception as e:
            print("[X] Telegram Error:\n>", e)

    else:
        return


# Start application
core = Flask(__name__)
program = Path(__file__).stem

# Parse and interpret options.
parser = argparse.ArgumentParser(description="ZCrypto helpers.")
parser.add_argument(
    "-d", "--datadir", help="directory to use for config and logs files", type=str
)
parser.add_argument(
    "-s", "--sharedir", help="directory to use for shared files", type=str
)
parser.add_argument(
    "-b", "--blacklist", help="local blacklist to use instead of 3Commas's", type=str
)

args = parser.parse_args()
if args.datadir:
    datadir = args.datadir
else:
    datadir = os.getcwd()

if args.sharedir:
    sharedir = args.sharedir
else:
    sharedir = None
if args.blacklist:
    blacklistfile = f"{datadir}/{args.blacklist}"
else:
    blacklistfile = None

# Create or load configuration file
config = load_config()
if not config:
    # Initialise temp logging
    print(
        f"Created example config file '{datadir}/{program}.ini', edit it and restart the program"
    )
    sys.exit(0)
else:
    # Handle timezone
    if hasattr(time, "tzset"):
        os.environ["TZ"] = config.get(
            "settings", "timezone", fallback="Africa/Cairo"
        )
        time.tzset()


@core.route("/webhook", methods=["POST"])
def webhook():
    try:
        if request.method == "POST":
            data = request.get_json()
            key = data["key"]
            if key == str(config.get("settings", "secret-key")):
                send_alert(data)
                return "Sent alert", 200
            else:

                return "Refused alert", 400

    except Exception as e:
        print(get_timestamp(), "Error:\n>", e)
        return "Error", 400


while True:
    config = load_config()
    print(f"Reloaded configuration from '{datadir}/{program}.ini'")
    if __name__ == "__main__":
        from waitress import serve

        print("Webhook Service Has been activated")
        serve(core, host="0.0.0.0", port=80)

# TO DO
