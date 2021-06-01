import json
from dhooks import Webhook

with open('config.json') as config:
    data = json.load(config)
    hookurl = data['webhook']
    hook = Webhook(hookurl)

def sendMessage(message):
    hook.send(message)
