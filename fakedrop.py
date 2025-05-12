from flask import Flask, request, send_file, redirect
from random import random
from PIL import Image

from io import BytesIO

app = Flask(__name__)

@app.route('/')
def get_file():
    return redirect('/upload')
    
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        ext = f.filename.split('.')[1]
        if ext != "py":
            f.save('/storage/emulated/0/Fakedrop/image'+str(random())[2:]+'.'+ext)
            return '<p>File sent!</p><br><a href="/upload">Send more</a>'
        else:
            return '<h1>An error occurred</h1>'
    return '''
    <!doctype html>
    <title>Fakedrop</title>
    <h1>Upload a file with fakedrop</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == ("__main__"):
    
    app.run(host="0.0.0.0", debug=True)