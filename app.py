import sys
sys.path.insert(0,"/db")
from db.dbhelper import *
from flask import Flask,render_template,redirect,url_for,request

upload_folder="static/images"
app = Flask(__name__)
app.config['UPLOAD_FOLDER']= upload_folder

@app.route("/save",methods=['POST','GET'])
def save()->None:
    file = request.files['webcam']
    idno:str = request.args.get('idno')
    lastname:str = request.args.get('lastname')
    firstname:str = request.args.get('firstname')
    course:str = request.args.get('course')
    level:str = request.args.get('level')
    
    
    filename=(upload_folder+"/"+lastname+".png")
    file.save(filename)
    ok:bool = addrecord('students',idno=idno,lastname=lastname,firstname=firstname,course=course,level=level,image=filename)
    return redirect(url_for("index"))
    
    message:str ="Student Added" if ok else" Error Saving student"
    print(message)

@app.route("/")
def index()-> None:
    return render_template("register.html")
    
if __name__ == "__main__":
    app.run(debug=True)