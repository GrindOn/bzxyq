# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author         : micah
# @Author_email   : 844830117@qq.com
# @FILE           : baidu_translate.py
# @Time           : 2022/7/26 19:43
# @work           : 搜狗搜索

# UA: User-Agent(请求载体的身份标识)

# UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器
# 说明该请求是一个正常的请求。但是，如果检测到请求的载体身份标识不是基于某一浏览器的，则表示该请求
#为不正常的请求（爬虫），则服务器端就很有可能拒绝该请求。

# UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器

import requests

if __name__ == '__main__':
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！！')

