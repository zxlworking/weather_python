#!/usr/bin/env python
# coding=utf-8
from com_zxl_common.HttpBaseUtil import HttpBaseUtil


class QsbkUtil(HttpBaseUtil):

    def get_qsbk_detail(self, author_id, result):
        # https://www.qiushibaike.com/article/120535436
        url = "http://www.qiushibaike.com/article/%s" % author_id

        driver = self.get_web_content(url)
        try:
            qsbk_detail_content = driver.find_element_by_xpath('//div[@class="content"]').text
            # print qsbk_detail_content

            user_comment_list = []
            comment_elements = driver.find_elements_by_xpath('//div[@class="comment-block clearfix floor-8"]')
            for comment_element in comment_elements:
                # print comment_element

                element_id = comment_element.get_attribute('id');
                print element_id

                parent_xpath = '//div[@id="%s"]/div[@class="replay"]' % element_id

                user_comment_element = {}
                user_comment_element["user_id"] = "user_id"
                user_comment_element["user_head_img"] = "user_head_img"

                user_comment_element["user_name"] = comment_element.find_element_by_xpath(parent_xpath + '/a[@class="userlogin"]').get_attribute('title')

                # if "manIcon" in parse_qsbk_detail_comment_element[3]:
                #     user_comment_element["user_sex"] = SEX_MAN
                # else:
                #     user_comment_element["user_sex"] = SEX_FEMALE
                # user_comment_element["user_age"] = int(parse_qsbk_detail_comment_element[4])
                user_comment_element["comment_content"] = comment_element.find_element_by_xpath(parent_xpath + '//span[@class="body"]').text
                # user_comment_element["comment_report"] = int(parse_qsbk_detail_comment_element[6])

                user_comment_list.append(user_comment_element)

            result["code"] = 0
            result["desc"] = "success"
            result["qsbk_detail_content"] = qsbk_detail_content
            result["user_comment_list"] = user_comment_list

            driver.close()
            driver.quit()
        except BaseException, e:
            print e
            result["code"] = -2
            result["desc"] = "数据解析异常"
            driver.close()
            driver.quit()
