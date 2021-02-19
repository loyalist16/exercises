# -*- coding: utf-8 -*-
# @Time : 2021/2/2 15:11
# @Author : loyalist
# @Email : lzl0118@foxmail.com
# @File : 3.py
# @Desc :

from collections import Counter
import re
import requests


def logo():
    # cookie_url = 'http://match.yuanrenxue.com/logo'
    # headers = {
    #     'Referer': "http://match.yuanrenxue.com/api/match/3",
    #     'User-Agent': 'yuanrenxue.project',
    #     'Connection': 'keep-alive'
    # }
    # resp = requests.post(cookie_url, headers=headers)
    # print(resp.headers)

    url = "http://match.yuanrenxue.com/logo"

    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Referer': 'http://match.yuanrenxue.com/match/3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.headers)
    print(response.raw.headers)
    print(response.cookies)


def run():
    url = "http://match.yuanrenxue.com/api/match/3"
    session = requests.Session()
    cookie_url = 'http://match.yuanrenxue.com/logo'
    HEADERS = {
        'Host': 'match.yuanrenxue.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'User-Agent': 'yuanrenxue.project',
        'Accept': '*/*',
        'Origin': 'http://match.yuanrenxue.com',
        'Referer': 'http://match.yuanrenxue.com/match/3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    ans = []
    for page in range(1, 6):
        session.headers=HEADERS
        resp = session.post(cookie_url)
        params = {
            'page': page
        }
        res = session.get(url, params=params)
        print(res.text)
        result = res.json()
        print(result)
        ans.extend([datum['value'] for datum in result.get('data')])
    print(ans)
    c = Counter(ans)
    return max(c, key=c.get)


if __name__ == '__main__':
    print(run())
    # 8717