import os
from flask import Flask, render_template, request
from werkzeug.utils import html, secure_filename
app = Flask(__name__)

app.secret_key = "12345"
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/upload')
def upload_():
   return render_template('upload.html')
right_image = {'jpg','png'}
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      file = request.files['file']
      filename = secure_filename(file.filename)
      if not filename =='' and filename.split('.')[-1] in right_image:
         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
         fullfilename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
         return render_template("results.html",uploaded_image=fullfilename,value='HEALTH',Accuracy=98)
      elif filename.split('.')[-1] not in right_image and not filename =='':
         message = 'Imvalid file format, PLZ Select the right image'
         return render_template('upload.html',message = message)

      else:
         message = 'No File Selected, Please Select the Image'
         return render_template('upload.html',message = message)
if __name__ == '__main__':
   app.run(debug = True)