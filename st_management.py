import os, time

now = time.time()

def manageFiles(path):
    for filename in os.listdir(path):
        if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:
            if os.path.isfile(os.path.join(path, filename)):
                print(filename)
                os.remove(os.path.join(path, filename))