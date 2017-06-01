#!/usr/bin/env python
#coding:utf-8

#创建一个空字典
#setdefault 设置默认值，和get类似,temp是搜索的key,0是返回的值

logfile_dict = {}
file=open('www_access_20140823.log','r')
for line in file.readlines():
#       print line
        if line == '\n':
                continue
        temp = (line.split()[0],line.split()[8])
        logfile_dict[temp]=logfile_dict.setdefault(temp,0)+1
        file.close
#print logfile_dict
#排序
#[(('220.181.51.108', '404'), 2), (('60.222.231.46', '200'), 608)]
#将字典转换成列表
res_list = logfile_dict.items()
#print res_list
#print res_list
#列表个数 1,2.3,4...
for i in range(len(res_list)):
        for j in range(i+1,len(res_list)):
                if res_list[i][1]<res_list[j][1]:
                        res_list[i],res_list[j]=res_list[j],res_list[i]
#print res_list
#写入到log.html里面
count = 0
w = open('log.html','w')
w.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>访问日志排名前十IP及Status</title>
</head>
<body>
<table border='1'>
<tr>
<td>IP</td>
<td>STATUS</td>
<td>NUM</td>
</tr>
</body>
</html>
''')
for k in res_list:
    if count >= 10:
      break
    temp = '''<tr>
    <td> %s </td>
    <td> %s </td>
    <td> %s </td>
    </tr>'''% (k[0][0], k[0][1], k[1])
#print temp
    count += 1
    w.write(temp)
#w.write('''</table></body></html>\n''')

w.close()
