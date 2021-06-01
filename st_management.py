import os, time
import json

now = time.time()

def manageFiles(path):
    if os.path.isfile('config.json'):
        with open('config.json') as config:
            data = json.load(config)
            days = data['days']
        print(days)
    else:
        days = 7

    for filename in os.listdir(path):
        if os.path.getmtime(os.path.join(path, filename)) < now - days * 86400:
            if os.path.isfile(os.path.join(path, filename)):
                print(filename)
                os.remove(os.path.join(path, filename))