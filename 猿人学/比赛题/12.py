# -*- coding: utf-8 -*-
# @Time : 2021/2/20 17:52
# @Author : loyalist
# @Email : lzl0118@foxmail.com
# @File : 12.py
# @Desc :

import requests
import base64
from urllib.parse import quote


def get_page(page):
    m = quote(base64.b64encode(('yuanrenxue' + str(page)).encode()).decode())
    url = f"http://match.yuanrenxue.com/api/match/12?page={page}&m={m}"
    headers = {
        'Cookie': 'sessionid=5n9bzmyk2co3zg4tuwmtkbscxo8gapvc;',
        'User-Agent': 'yuanrenxue.project'
    }
    response = requests.get(url, headers=headers)
    result = response.json().get('data')
    print(result)
    return result


if __name__ == '__main__':
    ans = 0
    for page in range(1, 6):
        data = get_page(page)
        ans += sum([datum['value'] for datum in data])
    print(ans)
