import requests
import json
import discum
import os
import schedule
from dotenv import load_dotenv


load_dotenv()


def get_data(bot, NAME):
    data = {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "condenser_api.get_dynamic_global_properties",
        "params": []
    }

    res = requests.post("https://api.hive.blog/", data=json.dumps(data))

    content = res.json()['result']

    if NAME in content['current_witness']:

        print("Found & Sending... ")

        line_break = '\n'

        message = f"New Witness: {content['current_witness']}{line_break}Block Number: {content['head_block_number']}"

        bot.sendMessage(channelID=CHANNEL_ID, message=message)


if __name__ == "__main__":
    TOKEN = os.environ.get('TOKEN')
    GUILD_ID = os.environ.get('GUILD_ID')
    CHANNEL_ID = os.environ.get('CHANNEL_ID')
    NAME = os.environ.get('NAME')
    bot = discum.Client(token=TOKEN, log=False)
    print("Searching....")
    schedule.every().second.do(get_data, bot, NAME)

    while True:
        schedule.run_pending()
