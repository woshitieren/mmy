#!/usr/bin/env python
#coding:utf-8


#1、打开文件  统计数据

def read_file(file_name):
    res = {}
    with open(file_name) as f:
        for line in f:
            if line == '\n':
                continue
            tmp=line.split()
            ip,url,status = (tmp[0],tmp[6],tmp[8])
            file_tuple = (ip,url,status)
            res[file_tuple]=res.get(file_tuple,0)+1
    return res
#2、统计数据获取前十
def getTop10(res_dict):
    return sorted(res_dict.items(),key=lambda x:x[1],reverse=True)[:10]
#3、写入html文件
def gen_html(arr):
    html_tmp1 = '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
    html_str='<table border="1">'
    html_str +=html_tmp1%('IP','URL','STATUS','COUNT')
    for (ip,url,status),count in arr:
        html_str += html_tmp1%(ip,url,status,count)
    html_str+='</table>'
    return html_str
def write_file(arr):
    html_str = gen_html(arr)
    with open('res.html','w') as f:
        f.write(html_str)
def start():
    res=read_file('www_access_20140823.log')
    top10 = getTop10(res)
    write_file(top10)
start()
