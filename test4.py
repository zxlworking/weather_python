#!/usb/bin/env python
#coding=utf-8
import cgi
import json
import sys

from com_zxl_common.HttpUtil import *
from com_zxl_common.XPathParserUtil import *
from com_zxl_listener.TaoBaoAnchorLoadListener import TaoBaoAnchorLoadListener

reload(sys)
sys.setdefaultencoding("utf-8")

driver = None
result = {}

if __name__ == "__main__":

    form = cgi.FieldStorage()
    page = form.getvalue("page").decode("utf-8")

    # page = 1
    print "page============test4--->%s" % page

    mHttpUtil = HttpUtil()
    mXPathParserUtil = XPathParserUtil()

    #test
    # l = 20
    # i = 0
    # for ll in range(l):
    #     taobao_anchor_element = {}
    #
    #     i = i + 1
    #     print "=======================taobao_anchor_element======================="
    #     print i
    #
    #     x = "[%d]" % i
    #     print x

    if page is None:
        result["code"] = -1
        result["desc"] = "参数错误"
    else:
        try:
            driver = mHttpUtil.get_taobao_anchor(page, TaoBaoAnchorLoadListener(result))
            mXPathParserUtil.parse_taobao_anchor(driver, result)

            result["current_page"] = page

            driver.close()
            driver.quit()
        except BaseException,e:
            print e
            result["code"] = -2
            result["desc"] = "获取信息失败"
            if driver is not None:
                driver.close()
                driver.quit()
    print "Content-type:text/html;charset=UTF-8"
    print "Accept:application/json"
    print "Accept-Charset:UTF-8"
    print ""

    print json.dumps(result, encoding="utf-8", ensure_ascii=False)