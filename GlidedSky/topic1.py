import requests
from lxml import etree

def get_numbers():
    url = "http://www.glidedsky.com/level/web/crawler-basic-1"

    payload = {}
    headers = {
        'Host': 'www.glidedsky.com',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': 'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1610345306; _ga=GA1.2.500370608.1610345306; _gid=GA1.2.2026030606.1610345306; __gads=ID=dfd5daf8f7c4d660-22dde8e2a8c500aa:T=1610345306:RT=1610345306:S=ALNI_MYWz_NX1g3Z3hTYLJUIZF-M3rwuNw; footprints=eyJpdiI6ImVRK2NRNmVoUWlRUmNXZVQrM3R3eFE9PSIsInZhbHVlIjoiWFp1aXM4ZlllamprYk5hVU9RYnU2N2Vza1ROT0R1U1cwcTVudW9qM2k5eEdYRGJSTE9yQnJVdlAxMlVwSXhweSIsIm1hYyI6IjU2ODQ0ZmRhOTVlMzY2MjkxNzZiNjcyMzUzNDg1OGFkNzdiODc4YTI5ZWMxNWM0MmU2NDU3OTU4NzEzZTZlOGIifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IkFYNUJkN3htYmNzRjdqYjIxWEJrc1E9PSIsInZhbHVlIjoielZPcTJBZUpYbjZqbXliNVwvWTdBemxTTDgzQ1FzTWNsdWp4anBpUGRXWERMQmhJRm9yTTRteEhpdVo5VzJ5eXIiLCJtYWMiOiI0MGVlOTUwNWJhOTc2YjJhZjJhN2M1YTUwN2Y2MGJmNTgzNDJmNDE4ZDVmNGJhOTkzNzZjNDU5ZTVjZWFlN2EwIn0%3D; glidedsky_session=eyJpdiI6Im5LdVFaaGdrMHBldGc4K0VzanpmaXc9PSIsInZhbHVlIjoiVE1NbTA2TUVYczlGa29QZjg0QmpWQ0FnK3NmbnFWeUVPSjNqRlJcL1lycmxoemZ4WmNvamZveFwvTWFjczhGZ1FUIiwibWFjIjoiZjU2Yzg1NGY0M2U4Yjg5MmVjNTJhYjg2NjNmOGI0NGUxZTVlOGFkYTI3OWRlNTNkZDhlMjk3NTUyMjZmNjFhNCJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1610351269; XSRF-TOKEN=eyJpdiI6IlA4M25DVFJZeEVvOWZ5T3RhUkZaUGc9PSIsInZhbHVlIjoiajVuV1ExNE4wbUhkSm9PaWtLdGd4Njd3VXdhaitPdm1JeExpVXloSU5lT25FdlJaUmxaYkNzMzZjVUt0TDJPbyIsIm1hYyI6IjllMmNjOWMxNmNlODU2MzE4MGE2YzkxNmJiZjEzZjc3ZjkzNDQzMzhmMzI4YTBmNmY5Yjg0NGQ1NGViYjE5MmIifQ%3D%3D; glidedsky_session=eyJpdiI6InFwMUVXcTFCcURwVnJSTlpMbnduMkE9PSIsInZhbHVlIjoiQU4xenNWMWJLUjBMQ1JraU5sWXJCeHgzUHVEaTJtbmxKWTFNRExYU0dxc0NwbDRJalRzMzZRMG42cW5cL3FOZTUiLCJtYWMiOiJkZmZlN2MzZGMwYmVkMWJkNDRmMDlmODVmMDY4ZTBhY2NjMmY4OTg2MGYyM2Y4NzY2ZGZhZWJhYjcwNDNlMGU0In0%3D'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    html = etree.HTML(response.text)
    numbers = html.xpath('//div[@class="col-md-1"]/text()')


    return [int(num) for num in numbers]


if __name__ == '__main__':
    num_list = get_numbers()
    print("答案: ", sum(num_list))