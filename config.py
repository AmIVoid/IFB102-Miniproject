import json, os

def createConfig():
    if os.path.isfile('config.json'):
        return('Config exists')
    else:
        hook = input('Enter webhook URL: ')
        output = {
            'days' : 7,
            'webhook' : hook
        }
        with open('config.json', 'w') as config:
            json.dump(output, config)
            config.close()

def changeDays(time):
    if os.path.isfile('config.json'):
        with open('config.json', 'r') as config:
            config_file = json.load(config)
            config.close()
            config_file['days'] = time
            config = open('config.json', 'w')
            json.dump(config_file, config)
            config.close()
    else:
        createConfig()

def changeWebhook(url):
    if os.path.isfile('config.json'):
        with open('config.json', 'r') as config:
            config_file = json.load(config)
            config.close()
            config_file['webhook'] = url
            config = open('config.json', 'w')
            json.dump(config_file, config)
            config.close()
    else:
        createConfig()

createConfig()