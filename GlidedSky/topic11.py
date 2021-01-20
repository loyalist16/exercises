import requests
import re
import base64
from lxml import etree
from copy import deepcopy


def get_page(page):
    url = f"http://www.glidedsky.com/level/web/crawler-sprite-image-1?page={page}"

    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1610934886; __gads=ID=63eccdb07da4a9e4-227d7fdfc0c5006c:T=1610934887:RT=1610934887:S=ALNI_Mb20Pcitzo8TzAPU5pwevhaH3jRfA; _ga=GA1.2.532097488.1610934888; _gid=GA1.2.719089514.1610934889; footprints=eyJpdiI6IjBxVWtjdHpcL0dweE1uSFVFck96Zll3PT0iLCJ2YWx1ZSI6Imt1S3BybGxzWGR2bDFVbklrajU4T0dIb0Rhb1wvVFVDa0xtMWRWU1A3ZHRVTzA2MElpenh4MlNxd1g0bW9OeVhqIiwibWFjIjoiNmFhNDk4MTI2MmE2NTY0MzJhN2Y3ZTFmZWJmYTNiZGQ0YmEyOWQ4MmI3ODMzMDkyODEwNGRkNWM4MzdkNDU0NCJ9; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IkQwUjdHYlFjMGhuQml0NXpDQXhnWWc9PSIsInZhbHVlIjoiNnZtN1A2TkdBV21mWWsxMXF0blljS2lkSmRPSDdMVFpCZDBCZ09UNFlKQllMend1eWY3ZEFKOVg3UGx0c1BNanFTTWt2S05LV3JRMGJCK1ZcL2xnVWN1cE1UZlB4QzFiakl2b01wajhTbCtUQUZwRlpjOVVJT0tUXC9QNnk0a2xCRVRXSDJGbDh2bXhPMTZlbENnenB0SHdyYXJWVjU4dVlmamhHQUxpcGo1STg9IiwibWFjIjoiMDcxYWRkYjA0ZDg1YTgzNjExZGRhM2Q1OTQzNDExZTgxYWYzMThkMTFhNWNhZDQ3MGJjOTU5MzMzYWQ3ZGRiNyJ9; XSRF-TOKEN=eyJpdiI6IjJZUjh3K3l5T1QxVUVcL25kWFN5WXl3PT0iLCJ2YWx1ZSI6InZ6MmR4YlFzam1uTGtROExHZktqbHVGMWxic25BT29FMk5sZDFYbjZtR0h4Rzlsc0E1RTNWdTlnc3NsYjNCa0oiLCJtYWMiOiJhYmI0ZTYyZGM2NjNmY2I2MmZlZGIwOWUzZGY4NDlmMDhhNDVkNzk0NTliOWM2MGJjMjdiZWMzNmExMzhkNzY5In0%3D; glidedsky_session=eyJpdiI6IlBLZFlDZWhYQk5aMHpzNnZ6UW5NWFE9PSIsInZhbHVlIjoiV2Z0V1ZjS0o2dm4xTmtkaGNySXpSRmg0TjBPWklVYzB3RE50Y1grZEltSW1yejZKVmFtMTk1UkZaOE5JeDlRNyIsIm1hYyI6ImFhYzUzMmQzZjhjNmE0NjJlYjJiN2ZjNDBiYmQwMjVhZTIzZGJmY2M4ZjE4NDQ2Njg5ZjE1ZjA0YzA1OTY2YTIifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1610935143'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    # base64_str = re.search("data:image/png;base64,(.*?)\)", response.text).group(1)
    # with open('topic11.png', 'wb') as f:
    #     f.write(base64.b64decode(base64_str))
    position = set(re.findall('background-position-x:(-?\d+)px', response.text))
    sort_num = sorted(position, key=lambda x: int(x), reverse=True)
    sort_num_copy = deepcopy(sort_num)
    print(sort_num, len(sort_num))
    if len(sort_num) < 10:
        print(f"{page}页不完整")
        flag = 0
        if sort_num[0] != '0':
            sort_num_copy.insert(flag, '0')
            flag += 1

        for i in range(len(sort_num) - 1):
            if 15 < int(sort_num[i]) - int(sort_num[i + 1]) <= 30:
                flag += 1
                sort_num_copy.insert(i + flag, '')
            if int(sort_num[i]) - int(sort_num[i + 1]) > 30:
                flag += 2
                sort_num_copy.insert(i + flag - 1, '')
                sort_num_copy.insert(i + flag, '')
    print("补充后 >>> ", sort_num_copy)
    html = etree.HTML(response.text)
    style = html.xpath('//style/text()')[0]
    divs = html.xpath('//div[@class="col-md-1"]')
    number_list = []
    for div in divs:
        classes = div.xpath('./div/@class')
        number = ''
        for cls in classes:
            cls_name = cls[:cls.index(' ')]
            pos = re.search(cls_name + ' { background-position-x:(-?\d+)', style).group(1)
            number += str(sort_num_copy.index(pos))
        number_list.append(int(number))
    print(f'{page} >>> {number_list}')
    return number_list


if __name__ == '__main__':
    ans = 0
    for i in range(1, 1001):
        num_list = get_page(i)
        ans += sum(num_list)
    print('答案: ', ans)
    # get_page(375)
