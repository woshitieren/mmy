#!/usr/bin/env python
#coding:utf8
user_dict={}
def get_data():
	with open('user.txt') as f:
		for l in f:
			if l =='\n':
				continue
			(user,pwd)=l.replace('\n','').split(':')
			user_dict[user]=pwd
get_data()
#更新文件
def render_file():
	user_txt_list=[]
	for item in user_dict.items():
		user_txt_list.append('%s:%s'%item)
	with open('user.txt','w') as f:
		f.write('\n'.join(user_txt_list))
def add_user(user,pwd):
	if user and pwd:
		if user in user_dict:
			return 'user already exist'
		else:
			user_dict[user]=pwd
			render_file()
			return 'ok'
	else:
		return 'need a user and password'
add_user('zabbix','123')
def del_user(user):
	if not user:
		return 'need a username'
	if user in user_dict:
		del user_dict[user]
		return 'ok'
	else:
		return 'user not exists'
def updateuser(user,pwd):
	user_dict[user]=pwd
	render_file()
