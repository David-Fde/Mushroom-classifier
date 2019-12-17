import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '../../Input/Test-photos'

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def uploader():
 if request.method == 'POST':
  # obtenemos el archivo del input "archivo"
  f = request.files['archivo']
  filename = secure_filename(f.filename)
  # Guardamos el archivo en el directorio "Archivos PDF"
  f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  # Retornamos una respuesta satisfactoria
  return "<h1>Archivo subido exitosamente</h1>"


if __name__ == "__main__":
    app.run()


