import requests
import base64
import re
from fontTools.ttLib import TTFont
from lxml import etree

list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def font_map(base64_str):
    with open('topic10.ttf', 'wb') as f:
        f.write(base64.b64decode(base64_str))
    font = TTFont('topic10.ttf')
    font.saveXML('topic10.xml')
    list2 = font.glyphOrder[1:11]
    font_dict = dict(zip(list2, list1))
    print(">>>字体对应表：　", font_dict)
    first_dict = font.getBestCmap()
    return first_dict, font_dict


def get_page(page):
    url = f"http://www.glidedsky.com/level/web/crawler-font-puzzle-2/?page={page}"
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': '_ga=GA1.2.500370608.1610345306; __gads=ID=dfd5daf8f7c4d660-22dde8e2a8c500aa:T=1610345306:RT=1610345306:S=ALNI_MYWz_NX1g3Z3hTYLJUIZF-M3rwuNw; footprints=eyJpdiI6IllqN3F4TUcxVXo5bnplZnJvU0YxZEE9PSIsInZhbHVlIjoiNHZcL0FzUG5LTEcxVHlGSFdFWlVVeTkyTGhBNU9lMlE0eElVU2QzUWRyQ1JmYnlMUVVXUHhNNXp5c09zXC9HYTZPIiwibWFjIjoiMWFjMWJjMjljMGYwMTYwYjkyNmU2NmVjNmE1ZTYwMTAxNzlmN2RhZWEyODIwN2FkMWNlODAyN2EzMTljZGI5ZSJ9; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IklmajRWazZmZ0p1RFwvSzczNXM0UUN3PT0iLCJ2YWx1ZSI6IjRcL05CUEU3TUkwWlh5NlwvTG5WMWZKb1RYeHdyQ2FCelFzNFo4WCsybmF5SHFXa2EyTjl2dXlzQ05OaXR2cnJ4VitLemNJRkNUQWg0Y1MwMEliM1VlZTVGbFFRcWNmOWlucGJrem5uTmdJbFdJS292XC9kS0tDR0o5WHFHMjBObXF1dWpHQmxaZENUZjl4REp0YjFmUFpuYjZVSk9xOUQyVHRZZktaVVd6SkRnTT0iLCJtYWMiOiJhNDhmNzgxMjM2ZGQ3OGJmNGI1NWI0NmE2OGNhYWU1ZjNiOGRjM2NlOTFkZWJkMzAwYzQyZmJmOWIwNTIzZmQwIn0%3D; _gid=GA1.2.196044008.1610593115; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1610345306,1610413927,1610593114,1610674931; XSRF-TOKEN=eyJpdiI6IlYzZWcxXC90OXFoYTFRa0c2RGIzTkNnPT0iLCJ2YWx1ZSI6InR6MjlTQWFhYjN4UXRKYkVSRk8yYmM3WWwyZkErNjBWejdkMEFiUU11ek1vRG9uZWozam5pUmc4VFpsNEVsNDkiLCJtYWMiOiI4MTZhYjdkZGY4MGJkMTc5NjkxMDA4YTg1ZjVmNzNlMWE3NTljZWVhY2U1ZDFiMGJhMTIyZTFmMGNhOGVmNTJlIn0%3D; glidedsky_session=eyJpdiI6IktGT1RCNEdzaWhIVElOYXhkTmVTbEE9PSIsInZhbHVlIjoiZThYZ0VVMTQ2cGhYMll3WVptQklOMFZ1TmZudis5dmRnalBsODVqUTdoeHRDb2RvQndobjl4Q1kweHNKaHFEcCIsIm1hYyI6IjU1NzQ1NDVlNjMyMGJlN2ZkMzM4NDJiMzc4ZmRjZGUzYWE2YWU4ZjU3MDJjNzZhMGUyNDFkMzdkYjA1YTFjOWQifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1610702179; XSRF-TOKEN=eyJpdiI6Ijg4VXdkaTdwMklaMG1JZXlsOU53cmc9PSIsInZhbHVlIjoiZGRxTGZjNmUyQ3ZvWEJcLytheUt1TmR5ekJGMFR2dTFSZjA4T3ByZTZLMW9mN3NlOEQzZlAyek9KTlNCeXlTNUIiLCJtYWMiOiI4ZmUyNDY5ODU4OGFhMjAzNDM5OWMxMzkxOTc3MWJhNjMyOWE3ZDE5Mjg5YmE2NzcxYmFiYmNmYWJmOTRjM2RiIn0%3D; glidedsky_session=eyJpdiI6IkxJdHZtbzJUM2lhNkFoQ056WEY5S1E9PSIsInZhbHVlIjoiYjdhV1wvM1JxTEQ5SUJIaCthTDBJZFU4aXBmdHZsRU1HQVp2dit1Rng5REtBamtpZnhDMHd2eHJlMStEMEc4OGkiLCJtYWMiOiI3MjNjODI1MWE4ZDE0MzIzODllODA2MjZkYmE5YzliZTE0YjlhM2Y4ZmViNzJkZjE1NzJjNjg3MGRmMTQzNGMwIn0%3D'
    }

    response = requests.request("GET", url, headers=headers)
    base64_str = re.search("data:font;charset=utf-8;base64,(.*?)\)", response.text).group(1)
    first_dict, font_dict = font_map(base64_str)
    html = etree.HTML(response.text)
    strings = html.xpath('//div[@class="col-md-1"]/text()')
    number_list = []
    for string in strings:
        string = string.strip()
        number = ''
        for s in string:
            unicode =  s.encode('unicode-escape').decode()
            hex_code = '0x'+ unicode[2:]
            key = int(hex_code, 16)
            number += font_dict[first_dict[key]]
        number_list.append(int(number))
    print(number_list)
    return number_list

if __name__ == '__main__':
    ans = 0
    for i in range(1, 1001):
        num_list = get_page(i)
        ans += sum(num_list)
    print('答案: ', ans)