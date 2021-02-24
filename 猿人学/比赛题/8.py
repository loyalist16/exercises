# -*- coding: utf-8 -*-
# @Time : 2021/2/24 9:40
# @Author : loyalist
# @Email : lzl0118@foxmail.com
# @File : 8.py
# @Desc :

import requests
import cv2
import base64
import re
from aip import AipOcr
import time

APP_ID = '16755537'
API_KEY = 'xgVZIQ3i01g6vHy2rll3thvT'
SECRET_KEY = 'yy90nNlMyUZLn0bRPOOLUaSDUH2vsAA1'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def ocr(file):
    '''
    通用文字识别（高精度版）
    '''
    """ 读取图片 """

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(file)

    """ 调用通用文字识别（高精度版） """
    result = client.basicAccurate(image)
    return result


def process_captcha(base64str):
    with open('8_captcha.jpg', 'wb') as f:
        f.write(base64.b64decode(base64str))
    img = cv2.imread('8_captcha.jpg')
    # cv2.namedWindow('Image')
    background = ''
    for i in img[0][:10]:
        if str(i) != '[0 0 0]':
            background = str(i)
    print(background)

    for i in img:
        for j in i:
            if str(j) == background or str(j) == '[0 0 0]':
                j[0] = 255
                j[1] = 255
                j[2] = 255
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dst = cv2.erode(gray_img, kernel)
    dst = cv2.dilate(dst, kernel)
    ret, thresh = cv2.threshold(dst, 240, 255, cv2.THRESH_TOZERO)
    cv2.imwrite('process_captcha.jpg', thresh)

    # cv2.imshow('Image', thresh)
    # 最后还要写一句代码，这样就可以使窗口始终保持住
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def crop_img():
    img = cv2.imread('process_captcha.jpg')
    cv2.imwrite('8_0.jpg', img[0:100, 0:100])
    cv2.imwrite('8_1.jpg', img[0:100, 100:200])
    cv2.imwrite('8_2.jpg', img[0:100, 200:300])
    cv2.imwrite('8_3.jpg', img[100:200, 0:100])
    cv2.imwrite('8_4.jpg', img[100:200, 100:200])
    cv2.imwrite('8_5.jpg', img[100:200, 200:300])
    cv2.imwrite('8_6.jpg', img[200:300, 0:100])
    cv2.imwrite('8_7.jpg', img[200:300, 100:200])
    cv2.imwrite('8_8.jpg', img[200:300, 200:300])


def get_base64str():
    url = "http://match.yuanrenxue.com/api/match/8_verify"
    response = session.get(url)
    html = response.json().get('html')
    verify_word = re.findall('<p>(\w?)</p>', html)
    print(verify_word)
    base64str = re.search('data:image/jpeg;base64,(.*?)" alt', html).group(1)
    return verify_word, base64str


anwser_map = {
    0: 156,
    1: 166,
    2: 176,
    3: 456,
    4: 466,
    5: 476,
    6: 755,
    7: 766,
    8: 776
}


def get_answer():
    verify_word, base64str = get_base64str()
    # 处理验证码
    process_captcha(base64str)
    # 裁剪验证码成一个字一张图
    crop_img()
    answer = [0] * 4
    for i in range(9):
        result = ocr(f'8_{i}.jpg')
        print(result)
        time.sleep(0.5)
        if result.get('words_result_num') == 1:
            word = result.get('words_result')[0]['words']
            if word in verify_word:
                ind = verify_word.index(word)
                pos = anwser_map.get(i)
                answer[ind] = pos
    print(answer)
    return answer


def get_page(page, answer):
    ans = ""
    for i in answer:
        ans += f"{i}|"
    print(ans)
    url = "http://match.yuanrenxue.com/api/match/8"
    params = {
        'page': page,
        'answer': ans
    }

    res = session.get(url, params=params)
    print(res.json())


if __name__ == '__main__':
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'yuanrenxue.project',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://match.yuanrenxue.com/match/8',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
    }
    session = requests.Session()
    session.headers = headers
    for page in range(5, 6):
        print("======= page: ", page, '=======')
        answer = get_answer()
        while 0 in answer:
            print("此处识别失败")
            answer = get_answer()
        get_page(page, answer)

    # p1 = [{'value': 7453}, {'value': 1457}, {'value': 5053}, {'value': 2127}, {'value': 4455}, {'value': 4290},
    #       {'value': 9875}, {'value': 7453}, {'value': 8778}, {'value': 2571}]
    # p2 = [{'value': 3932}, {'value': 5963}, {'value': 3372}, {'value': 9736}, {'value': 7831}, {'value': 1706},
    #       {'value': 887}, {'value': 9955}, {'value': 4029}, {'value': 3034}]
    # p3 = [{'value': 9606}, {'value': 3850}, {'value': 4106}, {'value': 2381}, {'value': 8545}, {'value': 2403},
    #       {'value': 9984}, {'value': 7453}, {'value': 3585}, {'value': 7545}]
    # p4 = [{'value': 5231}, {'value': 7453}, {'value': 6090}, {'value': 6476}, {'value': 2965}, {'value': 5510},
    #       {'value': 3879}, {'value': 7453}, {'value': 5821}, {'value': 1356}]
    # p5 = [{'value': 4798}, {'value': 8040}, {'value': 3086}, {'value': 7453}, {'value': 9874}, {'value': 4251}, {'value': 2862}, {'value': 677}, {'value': 9708}, {'value': 7902}]