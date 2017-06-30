#/bin/bash
git add .
git commit -m "`date -s`"
git push origin master
#error: command 'gcc' failed with exit status 1
#解决报错 
yum install gcc python-devel

pip2.7 install MySQL-python

