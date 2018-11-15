#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import Cookie
import cgi
import json
import os
import sys


reload(sys)
sys.setdefaultencoding("utf-8")

result = {}

if __name__ == "__main__":
    form = cgi.FieldStorage()

    print form

    for key in form.keys():
        print key

    # 获取文件名
    fileitems = form['file']

    if not os.path.exists('crash/'):
        os.mkdir('crash')

    print "fileitems--->"
    print isinstance(fileitems, list)


    # 检测文件是否上传
    if fileitems is not None:
        if isinstance(fileitems, list):
            print len(fileitems)
            for file_item in fileitems:
                if file_item.filename:
                    # 设置文件路径
                    fn = os.path.basename(file_item.filename)
                    open('crash/' + fn, 'wb').write(file_item.file.read())
                    message = 'file---> "' + fn + '" --->upload success'
                else:
                    message = 'file no upload'

                print "test8.py===>message===>%s" % message

        else:
            if fileitems.filename:
                # 设置文件路径
                fn = os.path.basename(fileitems.filename)
                open('crash/' + fn, 'wb').write(fileitems.file.read())
                message = 'file---> "' + fn + '"--->upload success'
            else:
                message = 'file no upload'

            print "test8.py===>message===>%s" % message

    else:
        print "test8.py===>message===>not fileitems"



    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)