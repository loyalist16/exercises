import requests
from lxml import etree


def get_page(page):
    url = f"http://www.glidedsky.com/level/web/crawler-basic-2?page={page}"
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': '_ga=GA1.2.500370608.1610345306; _gid=GA1.2.2026030606.1610345306; __gads=ID=dfd5daf8f7c4d660-22dde8e2a8c500aa:T=1610345306:RT=1610345306:S=ALNI_MYWz_NX1g3Z3hTYLJUIZF-M3rwuNw; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1610345306,1610413927; footprints=eyJpdiI6IllqN3F4TUcxVXo5bnplZnJvU0YxZEE9PSIsInZhbHVlIjoiNHZcL0FzUG5LTEcxVHlGSFdFWlVVeTkyTGhBNU9lMlE0eElVU2QzUWRyQ1JmYnlMUVVXUHhNNXp5c09zXC9HYTZPIiwibWFjIjoiMWFjMWJjMjljMGYwMTYwYjkyNmU2NmVjNmE1ZTYwMTAxNzlmN2RhZWEyODIwN2FkMWNlODAyN2EzMTljZGI5ZSJ9; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IklmajRWazZmZ0p1RFwvSzczNXM0UUN3PT0iLCJ2YWx1ZSI6IjRcL05CUEU3TUkwWlh5NlwvTG5WMWZKb1RYeHdyQ2FCelFzNFo4WCsybmF5SHFXa2EyTjl2dXlzQ05OaXR2cnJ4VitLemNJRkNUQWg0Y1MwMEliM1VlZTVGbFFRcWNmOWlucGJrem5uTmdJbFdJS292XC9kS0tDR0o5WHFHMjBObXF1dWpHQmxaZENUZjl4REp0YjFmUFpuYjZVSk9xOUQyVHRZZktaVVd6SkRnTT0iLCJtYWMiOiJhNDhmNzgxMjM2ZGQ3OGJmNGI1NWI0NmE2OGNhYWU1ZjNiOGRjM2NlOTFkZWJkMzAwYzQyZmJmOWIwNTIzZmQwIn0%3D; XSRF-TOKEN=eyJpdiI6ImFHTEJ4VXNCNVRqTGdkR1lBdHlaVWc9PSIsInZhbHVlIjoiVjRBbjFXelR6Sno3RnV5RlJSb3cwZEU1Wm8zckFyZlZ2OWdmbFE1Q2tGcnd3UHl4ajNtMzZEakx6UUcyS2NwWCIsIm1hYyI6ImVhM2Q4N2IyZTBmYzY0ZGUzZWI1MzUxMzAyN2Y2OTMyZjNhMTgzMGQ3NmQwMDMwNzljNmY2NjQ3YzAyM2E5NTIifQ%3D%3D; glidedsky_session=eyJpdiI6Ill2SytMWGlQN25PWk1ueVlvVnJnUlE9PSIsInZhbHVlIjoiemg4R0ZmRmdaM2lHZjNoQjE1aUhjVEtzM3NaN2R3ZXlhVFhNUmxVODdNSUVxbUxPRFBiUVorRmppOU4xdVVodiIsIm1hYyI6ImRkOTMyNjYyYWRkNzZlZjYzNjQ1OWVjZTY4MTA3YTUzNzlmOGYzODBhNmJmMTI4OGVjZWUxYjVmZjU3MTY2OTMifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1610413972'
    }

    response = requests.request("GET", url, headers=headers)
    html = etree.HTML(response.text)
    numbers = html.xpath('//div[@class="col-md-1"]/text()')

    return [int(num) for num in numbers]


if __name__ == '__main__':
    ans = 0
    for i in range(1, 1001):
        num_list = get_page(i)
        print(num_list)
        ans += sum(num_list)
    print('答案: ', ans)
