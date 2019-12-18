import os
import src.Functions
from flask import Flask, render_template, request
from werkzeug import secure_filename
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
model = "Input/Model/model.json"
weights = "Input/Model/weights-improvement-26-0.93.hdf5"
app.config['UPLOAD_FOLDER'] = './Output'


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files["file"]
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        pred = src.Functions.predict(img, model, weights)
        return render_template("prediction.html", pred=pred)


if __name__ == "__main__":
    app.run()
