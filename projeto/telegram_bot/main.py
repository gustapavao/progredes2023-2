import requests
from utils import Utils
from models import Pavaobot

TOKEN = "6834703211:AAGQ_Ud2L-Epq5l1uklT7aIrddU5a1Y1ItI"
NAME = "peacocksbot"

URL = f'https://api.telegram.org/bot{TOKEN}'

requisition = requests.get(URL + '/getUpdates')

print(requisition.status_code)
read = (requisition.json())
user = read["result"][-1]["message"]["from"]["first_name"]
message = read["result"][-1]["message"]["text"]


if Utils.isacommand(message):
    id = int(read["result"][-1]["message"]["from"]["id"])
    answer = {'chat_id':id,'text':f'Hi, {user}'}
    send = requests.post(URL+'/sendMessage',data=answer)
else:
    id = int(read["result"][-1]["message"]["from"]["id"])
    answer = {'chat_id':id,'text':f'I am sorry, {user}. I could not undertand. Could you please use a command?'}
    send = requests.post(URL+'/sendMessage',data=answer)