from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index1.html")
@app.route('/login',methods=["POST"])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        mobile = request.form['ph']
        mail = request.form['em']
        return render_template("index1.html",y = user,x=mail,z=mobile)

if (__name__)=='__main__':
    app.run(debug = True)