# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author         : micah
# @Author_email   : 844830117@qq.com
# @FILE           : baidu_translate.py
# @Time           : 2022/7/26 19:43
# @work           : 百度翻译

# post请求（携带了参数）
# 响应数据是一组json数据
import json

import requests

if __name__ == '__main__':
    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    # 3.post请求参数处理（同get请求一致）
    word = input('enter a word:')
    data ={
        'kw':word
    }
    # 4.请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.获取响应数据:json()方法返回的是obj（如果确认响应数据是json类型额，才可以使用json()
    dic_obj = response.json()

    # 持久化存储
    fileName = word +'.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp,ensure_ascii=False)

    print('over!!!')



