#!/usr/bin/env python
#coding:utf8
from flask import Flask,render_template,request,redirect,session
import MySQLdb as mysql
con = mysql.connect(host='192.168.2.122',user='deploy',passwd='123456',db='deploy')
#数据库自动生效插入数据
con.autocommit(True)
cur=con.cursor()
cur.execute('select * from user')
#print cur.fetchall()
app = Flask(__name__)
import util
#user random
app.secret_key='fdsaffgdafafdssdfsadfs'
@app.route('/pc',methods=['GET','POST'])
def pc():
	mem = request.args.get('mem')
	print mem
	sql='select * from pc'
	cur.execute(sql)
	res=cur.fetchall()
	mem_list=[]
	for item in res:
		m=item[1]
		if m not in mem_list:
			mem_list.append(m)
	pc_list=[]
	for item in res:
		a=item[1]
		print a
		if not mem or (item[1]==int(mem)):
			pc_list.append(item)
#	if request.method=='GET':
	return render_template('pc.html',pc=pc_list,mem_list=sorted(mem_list))
@app.route('/adduser',methods=['POST'])
def adduser():
	user=request.form.get('user')
	pwd=request.form.get('pwd')
	if (not user) or (not pwd):
		return 'need username and password'
	sql = 'insert into user values ("%s","%s")'%(user,pwd)
	cur.execute(sql)
	return redirect('/')
@app.route('/')
def index():
	if 'user' in session:
		cur.execute('select * from user')
		res = cur.fetchall()
		return render_template('index.html',user=session['user'],users=res)
	else:
		return redirect('/login')
@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	elif request.method=='POST':
		user=request.form.get('user')
		pwd=request.form.get('pwd')
		sql = 'select * from user where username="%s" and password="%s"'%(user,pwd)
		print sql
		cur.execute(sql)
	#	print cur.fetchall()
		if cur.fetchone():
			session['user']=user
			return redirect('/')
		else:
			return 'wrong user or password'
@app.route('/delete')
def removeuser():
	user=request.args.get('user')
	sql = 'delete from user where username="%s"'%(user)
	cur.execute(sql)
	return redirect('/')
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
