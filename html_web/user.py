#!/usr/bin/env python
#coding:utf-8

from flask import Flask,render_template
#render_template渲染html模块
app = Flask(__name__)
@app.route('/')
def index():
    return 'hello flask'
@app.route('/userlist')
def userlist():
    userlist = []
    with open('user.txt') as f:
        for l in f:
            userlist.append(l.split(':'))
        return render_template('userlist.html',userxxx=userlist)
@app.route('/user')
def user():
    html_str = '<table border="1">'
    with open('user.txt') as f:
        for line in f:
            html_str += '<tr><td>%s</td><td>%s</td></tr>'%tuple(line.split(':'))
    return html_str
#   return 'hello user <input type="text">'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
