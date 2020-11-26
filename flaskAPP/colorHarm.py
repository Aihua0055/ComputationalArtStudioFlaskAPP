from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    send_from_directory
)

import requests
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


bp = Blueprint('colorHarm',__name__,url_prefix='/colorHarm')

@bp.route('/upload',methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static/images/')

    # create image directory if not found
    if not os.path.isdir(target):
        os.mkdir(target)

    # retrieve file from html file-picker
    upload = request.files.getlist("file")[0]
    print("File name: {}".format(upload.filename))
    filename = upload.filename

    # file support verification
    ext = os.path.splitext(filename)[1]
    if (ext == ".jpg") or (ext == ".png") or (ext == ".bmp"):
        print("File accepted")
    else:
        return render_template("error.html", message="The selected file is not supported"), 400

    # save file
    destination = "/".join([target, filename])
    print("File saved to to:", destination)
    upload.save(destination)

    kwargs={
        'input_image':'IMG_8135.jpg',
        'image_name':url_for('static',filename = "/".join(['/images',filename])),
        'output_image':'temp.png',
        'jumbotron':{
            "header":"Color Harmonization",
            "bg_image":url_for('static',filename ='/images/colorHarJ.png'),
            "text": "Add text"
        }

    }

    # forward to processing page
    return render_template("/nav/colorharm.html", **kwargs)

@bp.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory("/static/images",filename)