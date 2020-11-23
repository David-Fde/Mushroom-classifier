import os
import Functions
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)
model = "Input/Model/model.json"  # trained neural network
weights = "Input/Model/weights-improvement-26-0.93.hdf5"  # weights
app.config['UPLOAD_FOLDER'] = './Output'
edible = ("Boletus-edulis", "Niscalo", "Amanita-cesarea")
toxic = ("Amanita-muscaria", "Amanita-phalloides")

# landing page
@app.route("/")
def landing_page():
    return render_template('index.html')

# function to save and upload an image
@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files["file"]
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(img)
        if img != "":
            pred, mushroom = Functions.predict(img, model, weights)
            if mushroom in edible:
                return render_template("edible.html", pred=pred)
            else:
                return render_template("toxic.html", pred=pred)
        else:
            return render_template("index.html")

# load map
@app.route("/map")
def openMap():
    return render_template("map.html")


def main():
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    run(host=host, port=port, debug=True)


if __name__ == "__main__":
    app.run()
