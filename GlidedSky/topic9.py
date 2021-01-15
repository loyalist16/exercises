import hashlib
import re
import requests


def encrypt(text):
    s = hashlib.sha1(('Xr0Z-javascript-obfuscation-1' + str(text)).encode()).hexdigest()
    return s


def get_page(page):
    r_url = f"http://www.glidedsky.com/level/web/crawler-javascript-obfuscation-1?page={page}"
    headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://www.glidedsky.com/level/web/crawler-javascript-obfuscation-1',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': '_ga=GA1.2.500370608.1610345306; __gads=ID=dfd5daf8f7c4d660-22dde8e2a8c500aa:T=1610345306:RT=1610345306:S=ALNI_MYWz_NX1g3Z3hTYLJUIZF-M3rwuNw; footprints=eyJpdiI6IllqN3F4TUcxVXo5bnplZnJvU0YxZEE9PSIsInZhbHVlIjoiNHZcL0FzUG5LTEcxVHlGSFdFWlVVeTkyTGhBNU9lMlE0eElVU2QzUWRyQ1JmYnlMUVVXUHhNNXp5c09zXC9HYTZPIiwibWFjIjoiMWFjMWJjMjljMGYwMTYwYjkyNmU2NmVjNmE1ZTYwMTAxNzlmN2RhZWEyODIwN2FkMWNlODAyN2EzMTljZGI5ZSJ9; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IklmajRWazZmZ0p1RFwvSzczNXM0UUN3PT0iLCJ2YWx1ZSI6IjRcL05CUEU3TUkwWlh5NlwvTG5WMWZKb1RYeHdyQ2FCelFzNFo4WCsybmF5SHFXa2EyTjl2dXlzQ05OaXR2cnJ4VitLemNJRkNUQWg0Y1MwMEliM1VlZTVGbFFRcWNmOWlucGJrem5uTmdJbFdJS292XC9kS0tDR0o5WHFHMjBObXF1dWpHQmxaZENUZjl4REp0YjFmUFpuYjZVSk9xOUQyVHRZZktaVVd6SkRnTT0iLCJtYWMiOiJhNDhmNzgxMjM2ZGQ3OGJmNGI1NWI0NmE2OGNhYWU1ZjNiOGRjM2NlOTFkZWJkMzAwYzQyZmJmOWIwNTIzZmQwIn0%3D; _gid=GA1.2.196044008.1610593115; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1610345306,1610413927,1610593114,1610674931; XSRF-TOKEN=eyJpdiI6Im02NlVHanE0UU1hb3h0V0VkeWhTcVE9PSIsInZhbHVlIjoiQzRuTEh0XC9tVExsc3JMcEZqZjFZUGlkTWV6WSs5bFJkdk5JcXVKUGNoN0FsQ2srYmw4VXNKSXVKK2tQbjlFSmIiLCJtYWMiOiJiOGUwZDUyM2MwOTQ0ZWQxODc2NWI0ZDMwMzhhOTZhZjc4ZTY5M2IxYWUxMzE3N2M0MzVkN2MwMTQ3ZmUyYzFlIn0%3D; glidedsky_session=eyJpdiI6IlpDNnhVZXlcL0pwUCtvSzh0OFwvRVU2QT09IiwidmFsdWUiOiJoUlYzUFFvTkFuTXYxMGJoVnlrcVdSN2UwRTRvTG9pendcL3VEWkU1NlVzMXRnZm5ZZmMweTRjbmFIcitGWk9tUiIsIm1hYyI6ImY0MDA5ZjhlMTEyOTc1YTZmM2RhYTA3NmUyMTFhZGU2ZWQ3MTg4N2Y1ZTg3ZGNmYzU5M2E2MDZkYWI2N2Y0YmIifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1610700673'
    }

    response = session.get(r_url, headers=headers)
    ot = re.search('t="(\d+)', response.text).group(1)
    t = int((int(ot) - 99) / 99)
    sign = encrypt(t)
    # print(t, sign)
    url = f"http://www.glidedsky.com/api/level/web/crawler-javascript-obfuscation-1/items?page={page}&t={t}&sign={sign}"
    headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': r_url,
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': '_ga=GA1.2.500370608.1610345306; __gads=ID=dfd5daf8f7c4d660-22dde8e2a8c500aa:T=1610345306:RT=1610345306:S=ALNI_MYWz_NX1g3Z3hTYLJUIZF-M3rwuNw; footprints=eyJpdiI6IllqN3F4TUcxVXo5bnplZnJvU0YxZEE9PSIsInZhbHVlIjoiNHZcL0FzUG5LTEcxVHlGSFdFWlVVeTkyTGhBNU9lMlE0eElVU2QzUWRyQ1JmYnlMUVVXUHhNNXp5c09zXC9HYTZPIiwibWFjIjoiMWFjMWJjMjljMGYwMTYwYjkyNmU2NmVjNmE1ZTYwMTAxNzlmN2RhZWEyODIwN2FkMWNlODAyN2EzMTljZGI5ZSJ9; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IklmajRWazZmZ0p1RFwvSzczNXM0UUN3PT0iLCJ2YWx1ZSI6IjRcL05CUEU3TUkwWlh5NlwvTG5WMWZKb1RYeHdyQ2FCelFzNFo4WCsybmF5SHFXa2EyTjl2dXlzQ05OaXR2cnJ4VitLemNJRkNUQWg0Y1MwMEliM1VlZTVGbFFRcWNmOWlucGJrem5uTmdJbFdJS292XC9kS0tDR0o5WHFHMjBObXF1dWpHQmxaZENUZjl4REp0YjFmUFpuYjZVSk9xOUQyVHRZZktaVVd6SkRnTT0iLCJtYWMiOiJhNDhmNzgxMjM2ZGQ3OGJmNGI1NWI0NmE2OGNhYWU1ZjNiOGRjM2NlOTFkZWJkMzAwYzQyZmJmOWIwNTIzZmQwIn0%3D; _gid=GA1.2.196044008.1610593115; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1610345306,1610413927,1610593114,1610674931; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1610700612; XSRF-TOKEN=eyJpdiI6IjlMK2doR095R3FDRDhoUm9TbVdNQ0E9PSIsInZhbHVlIjoidVNpYlwvbHRYeE1MZVdua3NIUTRhQ1ZtZEo3b0l0SkpURmprZ2hQaHFyK0FvTVZONG5uYU1tM1NLRHAreU90WDkiLCJtYWMiOiIwZTNiNDE3MDdjNWMyOTQ1Zjg0ZGNmNjk4ZmM3MTE3ZTkwYzg1Y2RjYzk0MzEzYTZiNGJiNDg3YzczNTYxM2Q5In0%3D; glidedsky_session=eyJpdiI6Im9sNzZWdENSNVZNZFA1K0NoekRJc3c9PSIsInZhbHVlIjoiM1lMYzhrS080QXFsdVk3WEl5S1F6cmE4elVhRGtRMWFwWExhdnBabHJwV2pQRDBvRDU4WU0wTjRzTE9zUWp1ZyIsIm1hYyI6ImJkYzk4ZGY2ZjRjYzA0NjRhNmJkZjU4MjhhMDQyYTlkODcxMTNjM2JiMTE2Y2NmZWViNGQ0M2E1NDdmMjYxOWIifQ%3D%3D'
    }

    response = session.get(url, headers=headers)
    resp = response.json()
    print(f'{page} >>> ', resp['items'])
    return resp['items']


if __name__ == '__main__':
    session = requests.Session()
    ans = 0
    for i in range(1, 1001):
        num_list = get_page(i)
        ans += sum(num_list)
    print('答案: ', ans)