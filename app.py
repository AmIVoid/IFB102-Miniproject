from flask import Flask, render_template, request, flash, redirect, url_for, make_response
from flask.helpers import send_file
from youtubedl import ytDownload
from multidl import Download
from waifu2x import upscale
from config import changeWebhook, changeDays
import os

url = ''
quality = ''
username = ''
UPLOAD_FOLDER = './uploaded_images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Homepage

@app.route('/')
def homepage():
    return render_template("index.html")

# YouTubeDL Webpages

@app.route('/youtubedl')
def youtubedl():
    return render_template("youtubedl.html")

@app.route('/youtubedl', methods=['POST'])
def ytGetURL():
    global url
    url = request.form['url']
    return render_template("youtubedl.html", text=url)

@app.route('/youtubedl/quality', methods=['POST'])
def getQuality():
    global quality
    quality = request.form['quality']
    return render_template("youtubedl.html")

@app.route('/youtubedl/download', methods=['GET', 'POST'])
def sendDownload():
    return render_template("youtubedl/download.html")

@app.route('/youtubedl/download', methods=['GET', 'POST'])
def renderPage():
    return render_template("youtubedl.html")

@app.route('/youtubedl/file', methods=['GET', 'POST'])
def sendFile():
    returnFile = ytDownload(url, quality)
    return send_file(f'{returnFile}', mimetype="video/H264", as_attachment=True)

# TwitterDL Pages

@app.route('/twitterdl')
def twitterdl():
    return render_template("twitterdl.html")

@app.route('/twitterdl', methods=['POST'])
def twGetURL():
    global url
    url = request.form['url']
    return render_template("twitterdl.html", text=url)

@app.route('/twitterdl/download', methods=['GET', 'POST'])
def twSendDownload():
    return render_template("twitterdl/download.html")

@app.route('/twitterdl/download', methods=['GET', 'POST'])
def twRenderPage():
    return render_template("twitterdl.html")

@app.route('/twitterdl/file', methods=['GET', 'POST'])
def twSendFile():
    returnFile = Download(url)
    return send_file(f'{returnFile}', mimetype="video/H264", as_attachment=True)

# Waifu2x Pages

@app.route('/waifu2x')
def waifu2x():
    return render_template("waifu2x.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/waifu2x', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            print('No File')
            return render_template("waifu2x.html", outcome="No file")

        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        outfile = upscale(path)
        return send_file(f'{outfile}', mimetype="img/jpg", as_attachment=True)
    
# Admin Pages

@app.route('/admin')
def showLogin():
    return render_template("admin-login.html")

@app.route('/admin', methods=['POST'])
def adminLogin():
    global pin
    pin = request.form['pin']
    if pin == '6969':
        with open("./logs/video_log.txt", "r", encoding="UTF-8") as v_log:
            video_info = v_log.read().split('\n')
        with open("./logs/image_log.txt", "r", encoding="UTF-8") as i_log:
            image_info = i_log.read().split('\n')
        return render_template("admin.html", v_log_file=video_info, i_log_file=image_info)
    else:
        return render_template("admin-login.html", state='Incorrect pin')

@app.route('/admin-config', methods=['POST'])
def changeDaysConfig():
    days = request.form['days']
    changeDays(days)
    with open("./logs/video_log.txt", "r", encoding="UTF-8") as v_log:
        video_info = v_log.read().split('\n')
    with open("./logs/image_log.txt", "r", encoding="UTF-8") as i_log:
        image_info = i_log.read().split('\n')
    return render_template("admin.html", v_log_file=video_info, i_log_file=image_info)

@app.route('/admin-config', methods=['POST'])
def changeHookConfig():
    url = request.form['hook']
    changeWebhook(url)
    with open("./logs/video_log.txt", "r", encoding="UTF-8") as v_log:
        video_info = v_log.read().split('\n')
    with open("./logs/image_log.txt", "r", encoding="UTF-8") as i_log:
        image_info = i_log.read().split('\n')
    return render_template("admin.html", v_log_file=video_info, i_log_file=image_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0")