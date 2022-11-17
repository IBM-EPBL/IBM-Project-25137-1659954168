from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("resume.html")
@app.route('/login',methods=["POST"])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        agee = request.form['age1']
        qualification = request.form['quali']
        clgname = request.form['clg']
        paddress = request.form['adres']
        techskill = request.form['skill']
        soskill = request.form['sskill']
        mail = request.form['mail']
        return render_template("resume.html",a = user,b=agee,c=qualification,d=clgname,e=paddress,f=techskill,g=soskill,h=mail)
@app.route('/upload',methods=['GET','POST'])
def flask_upload():
    if request.method =='POST':
        f=request.files['file']
        f.save(secure_filename(f.filename))
        return 'Upload successsful'
if (__name__)=='__main__':
    app.run(debug = True)