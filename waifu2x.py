from PIL import Image
import os
from datetime import datetime
from st_management import manageFiles
from webhook import sendMessage

def upscale(image_path):
    image = Image.open(image_path)
    image = image.resize((2*image.size[0], 2*image.size[1]), resample=Image.BILINEAR)
    output_path = f'./output_images/{os.path.basename(image_path)}'
    outfile = f'{os.path.splitext(output_path)[0]}_@2x.jpg'
    sendMessage(f'**{os.path.basename(image_path)}** was just upscaled.')
    if os.path.isfile('logs/image_log.txt'):
        log = open('logs/image_log.txt', 'a')
        log.write(f'\n{datetime.now()} \'{outfile}\'')
        log.close()
    else:
        log = open('logs/image_log.txt', 'w+')
        log.write(f'{datetime.now()} \'{outfile}\'')
        log.close()
    image.save(outfile)
    manageFiles(r'./uploaded_images')
    manageFiles(r'./output_images')
    return(outfile)