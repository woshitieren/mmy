#!/usr/bin/env python
from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
import util
#user random
app.secret_key='fdsaffgdafafdssdfsadfs'
@app.route('/')
def index():
	if 'user' in session:
		return render_template('index.html',user=session['user'],users=util.user_dict.items())
	else:
		return redirect('/login')
@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	elif request.method=='POST':
		user=request.form.get('user')
		pwd=request.form.get('pwd')
		if user in util.user_dict and util.user_dict[user]==pwd:
			session['user']=user
			return redirect('/')
		else:
			return 'wrong user or password'
@app.route('/delete')
def removeuser():
	user=request.args.get('user')
	res=util.del_user(user)
	if res=='ok':
		return redirect('/')
	else:
		return res 
@app.route('/logout')
def logout():
	del session['user']
	return redirect('/login')
@app.route('/updatepwd',methods=['GET','POST'])
def updatepwd():
	if request.method=='GET':
		user = request.args.get('user')
		return render_template('update.html',user=user)
	elif request.method=='POST':
		user=request.form.get('user')
		oldpwd = request.form.get('oldpwd')
		newpwd=request.form.get('newpwd')
		confirmpwd=request.form.get('confirmpwd')
		if util.user_dict[user]!=oldpwd:
			return 'wrong old password'
		if newpwd!=confirmpwd:
			return 'new pwd not equal to confirmpwd'
		util.updateuser(user,newpwd)
		return redirect('/')
if __name__=="__main__":
	app.run(host='0.0.0.0',port=9092,debug=True)
