# -*- coding: utf-8 -*-
# @Time : 2021/2/20 18:08
# @Author : loyalist
# @Email : lzl0118@foxmail.com
# @File : 13.py
# @Desc :

import requests
import re


def get_page(page):
    url = f"http://match.yuanrenxue.com/api/match/13?page={page}"
    headers = {
        'Host': 'match.yuanrenxue.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'yuanrenxue.project',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://match.yuanrenxue.com/match/13',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': f'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1613783480,1613799401,1613804404,1613956176; '
                  f'Hm_lpvt_0362c7a08a9a04ccf3a8463c590e1e2f=1613956176; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1613783482,1613799402,1613804405,1613956179; '
                  f'qpfccr=true; no-alert=true; tk=-3884792864035405662; sessionid=cckky7hhiqqr9mygxpx4eugap72h1t2k; '
                  f'Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1613783500,1613799406,1613804416,1613956195; '
                  f'Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1613956195; '
                  f'{cookie}; '
                  f'Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1613956899'
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    result = response.json().get('data')
    print(result)
    return result


if __name__ == '__main__':
    url1 = "http://match.yuanrenxue.com/match/13"
    # session = requests.Session()
    headers1 = {
        'Host': 'match.yuanrenxue.com',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://match.yuanrenxue.com/match/13',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': 'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1613783480,1613799401,1613804404,1613956176; Hm_lpvt_0362c7a08a9a04ccf3a8463c590e1e2f=1613956176; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1613783482,1613799402,1613804405,1613956179; qpfccr=true; no-alert=true; tk=-3884792864035405662; sessionid=cckky7hhiqqr9mygxpx4eugap72h1t2k; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1613783500,1613799406,1613804416,1613956195; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1613956195; yuanrenxue_cookie=1613956205|AuhMNmsOMor0fliIkUWxAmZFSRylaDzVpIox68NF; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1613956207'
    }
    response = requests.get(url1, headers=headers1)
    cookie_list = re.findall("\('(.*?)'\)", response.text)
    cookie = ''.join(cookie_list)
    print(cookie)
    headers = {
        'Host': 'match.yuanrenxue.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://match.yuanrenxue.com/match/13',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': f'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1613783480,1613799401,1613804404,1613956176; '
                  f'Hm_lpvt_0362c7a08a9a04ccf3a8463c590e1e2f=1613956176; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1613783482,1613799402,1613804405,1613956179; '
                  f'qpfccr=true; no-alert=true; tk=-3884792864035405662; '
                  f'sessionid=cckky7hhiqqr9mygxpx4eugap72h1t2k; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1613783500,1613799406,1613804416,1613956195; '
                  f'Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1613956195; '
                  f'Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1613956207; {cookie}'
    }
    response = requests.get(url1, headers=headers)
    ans = 0
    for page in range(1, 6):
        data = get_page(page)
        ans += sum([datum['value'] for datum in data])
    print(ans)
