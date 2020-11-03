from flask import Flask,render_template,request,redirect,session

app=Flask(__name__)

app.config["DEBUG"]=True
app.config['SECRET_KEY']='rajatronakshubham123'

@app.route('/signup',methods=['POST','GET'])
def signup():
    msg=''
    if request.method=='POST' and 'firstname' in request.form and 'lastname' in request.form and 'email' in request.form and 'mobileno' in request.form and 'exampleInputPassword1' in request.form and 'exampleInputPassword2' in request.form:
        firstname = request.form['firstname']
        lastname = request.form['firstname']
        email = request.form['firstname']
        mobileno = request.form['firstname']
        password = request.form['firstname']
        confirm_password = request.form['firstname']

        if 
    return render_template('homepage.html',msg=msg)



