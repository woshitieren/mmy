#!/usr/bin/env python
#coding:utf8
#print [line]有\n空行continue掉
res={}
f = open('www_access_20140823.log','r')
for line in f:
	if line=='\n':
		continue
	tmp = line.split()
	log_keys=(tmp[0],tmp[6],tmp[8])
	res[log_keys]=res.get(log_keys,0)+1	
f.close()
#排序以log_keys三个维度排序
#先转换成列表
res_list=res.items()
for j in range(15):
	for i in range(len(res_list)-1):
		if res_list[i][1]>res_list[i+1][1]:
			res_list[i],res_list[i+1]=res_list[i+1],res_list[i]
#print res_list
#降序
for item in res_list[:-15:-1]:
	print item
#正序
#for item in res_list[-15:]:
#	print item
