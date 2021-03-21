from flask import Flask, render_template, request, redirect, send_file, flash, send_from_directory, abort
import os
from werkzeug.utils import secure_filename
import predict
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')  # This is nothing but to define the parameters in the URL
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')  # **Refer comment below
def main_page(page_name):
    return render_template(page_name)

# I've only done changes to form of index.html. Have to do it to the rest as well.


# This is nothing but to define the parameters in the URL
@app.route('/details', methods=["GET", "POST"])
def details():

    if request.method == "POST":
        details = request.form
        global patientname, patientid, patientgender, patientage, patientemail, patientnumber, staffname, staffid, staffemail, staffnumber, staffrole, staffmessage
        patientname = details["patientname"]
        patientid = details["patientid"]
        patientage = details["patientage"]
        patientgender = details["patientgender"]
        patientemail = details["patientemail"]
        patientnumber = details["patientnumber"]
        staffname = details["staffname"]
        staffid = details["staffid"]
        staffemail = details["staffemail"]
        staffnumber = details["staffnumber"]
        staffrole = details["staffrole"]
        staffmessage = details["staffmessage"]

        return render_template("upload.html", patientname=patientname)
    return render_template('details.html')


app.config["CSV_UPLOADS"] = "C:\\Users\\ARFAH\\Desktop\\Bugsqaush\\the-bug-sqaushers\\static\\pdf\\uploads"
app.config["ALLOWED_CSV_EXTENSIONS"] = ["CSV"]
app.config["MAX_CSV_FILESIZE"] = 50 * 1024 * 1024
app.config["CSV_FILEPATH"] = "C:\\Users\\ARFAH\\Desktop\\Bugsqaush\\the-bug-sqaushers\\static\\csv-json-txt"


def allowed_csv(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_CSV_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_CSV_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_csv_filesize(filesize):

    if int(filesize) <= app.config["MAX_CSV_FILESIZE"]:
        return True
    else:
        return False


@app.route("/upload", methods=["GET", "POST"])
def upload_csv():

    if request.method == "POST":

        if request.files:

            if "filesize" in request.cookies:

                if not allowed_csv_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    flash('File size exceeds maximum limit', 'danger')
                    return redirect(request.url)

                csv = request.files["csv"]

                if csv.filename == "":
                    print("No filename")
                    flash('No file uploaded or invalid file name', 'danger')
                    return redirect(request.url)

                if allowed_csv(csv.filename):
                    global filename
                    filename = secure_filename(csv.filename)

                    csv.save(os.path.join(
                        app.config["CSV_UPLOADS"], filename))

                    print("CSV saved")

                    file_path = os.path.join(
                        app.config["CSV_UPLOADS"], filename)
                    print(file_path)
                    print(filename)
                    global probablity
                    probablity = []
                    array = predict.algorithm(filename)
                    for i in array:
                        probablity.append(i*100)
                    # main.run_main(file_path, filename)

                    return render_template('/results.html', data=json.dumps(probablity),  array=probablity, patientname=patientname, patientid=patientid, patientage=patientage, patientgender=patientgender, patientemail=patientemail, patientnumber=patientnumber, staffname=staffname, staffid=staffid, staffemail=staffemail, staffnumber=staffnumber, staffrole=staffrole, staffmessage=staffmessage)

                else:
                    print("That file extension is not allowed")
                    flash('Please upload a CSV file.', 'danger')
                    return redirect(request.url)

    return render_template("/upload.html", patientname=patientname)


# @app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
#     return send_from_directory(directory=uploads, filename=filename)

# @app.route('/thisone_student_data.csv')
# def download_file():
#     print(filename)
#     try:
#         return send_file("static/csv-json-txt/"+filename[:-4]+'_' + "student_data.csv", as_attachment=False)
#         # return send_from_directory(app.config["CSV_FILEPATH"], filename=filename, as_attachment=True)
#     except FileNotFoundError:
#         abort(404)


# @app.route("/download", methods=["GET", "POST"])
# def download_file():
#     if "file_name" in request.cookies:
#         print(request.cookies["file_name"])
#         p = "static/csv-json-txt/" + \
#             request.cookies["file_name"].replace(
#                 '.CSV', '').replace(' ', '_') + "_" + "student_data.csv"

#         return send_file(p, as_attachment=True)

    # @app.route('/<filename>')
    # def download_file():
    #     p = filename[:-4]+'_' + "student_data.csv"
    #     print(p)
    #     return send_file(p, as_attachment=True)
