# -*- coding: utf-8 -*-
# @Time : 2021/2/22 12:15
# @Author : loyalist
# @Email : lzl0118@foxmail.com
# @File : 6.py
# @Desc :


import requests
import execjs



def get_m():
    with open("6.js", 'r', encoding='utf-8') as f:
        jscode = f.read()
    t, m = execjs.compile(jscode).call('get_m_q_value')
    q = f"1-{t}|"
    return q, m


def get_page(page):
    q, m = get_m()
    url = f"http://match.yuanrenxue.com/api/match/6"
    params = {
        'page': page,
        'm': m,
        'q': q
    }
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'yuanrenxue.project',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://match.yuanrenxue.com/match/6',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': 'sessionid=cckky7hhiqqr9mygxpx4eugap72h1t2k;'
    }

    response = requests.request("GET", url, headers=headers, params=params)
    result = response.json().get('data')
    print(result)
    return result


if __name__ == '__main__':
    ans = 0
    for page in range(1, 6):
        data = get_page(page)
        ans += sum([datum['value'] for datum in data])
    print(ans*24)
