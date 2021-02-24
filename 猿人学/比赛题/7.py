# -*- coding: utf-8 -*-
# @Time : 2021/2/23 10:28
# @Author : loyalist
# @Email : lzl0118@foxmail.com
# @File : 7.py
# @Desc :

from fontTools.ttLib import TTFont
import base64
import requests
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import Glyph

map = {
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1): 4,
    (1, 1, 1, 1, 1, 1, 1): 7,
    (1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0): 0,
    (1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1,
     0, 0, 1, 0, 0): 9,
    (1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
     0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0): 8,
    (1, 0, 0, 1, 1, 0, 1, 1, 1, 1): 1,
    (1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1,
     1): 5,
    (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1,
     0, 1, 0, 0, 0): 6,
    (1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1,
     0, 1, 0, 1, 0, 1, 0, 0): 3,
    (1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0): 2
}


def get_map():
    font = TTFont('7.ttf')
    font.saveXML('7.xml')
    gly_list = font.getGlyphOrder()
    gly_map = {}
    for gly in gly_list:
        if gly == "notdef":
            continue
        g: Glyph = font['glyf'][gly]
        f = tuple(g.flags.tolist())
        # print(gly, f)
        # print(map.get(f))
        gly_map[gly] = map.get(f)
    print(gly_map)
    return gly_map


def get_page(page):
    url = f"http://match.yuanrenxue.com/api/match/7"
    params = {
        'page': page,
    }
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'yuanrenxue.project',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://match.yuanrenxue.com/match/7',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': 'sessionid=ni9dklbc35l86t5vukwx53669udjbjtt;'
    }

    response = requests.request("GET", url, headers=headers, params=params).json()
    woff = response.get('woff')
    with open("7.ttf", 'wb') as f:
        f.write(base64.b64decode(woff))
    gly_map = get_map()
    data = response.get('data')
    print(data)
    l = []
    for datum in data:
        value_list = datum['value'].strip(' ').split(' ')
        num = ""
        for value in value_list:
            num += str(gly_map['uni' + value[3:]])
        l.append(int(num))
    print(l)
    return l


if __name__ == '__main__':
    name = [
        '极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖',
        '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀',
        '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮',
        '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子',
        '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风', '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚',
        '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵'
    ]
    max_num = 0
    max_page = 0
    max_index = 0
    for page in range(1, 6):
        l = get_page(page)
        max_ = max(l)
        if max_ > max_num:
            max_num = max_
            max_page = page
            max_index = l.index(max_)
    print(max_num, max_page, max_index)
    print(name[max_index + 1 + (max_page - 1) * 10])
    #  9711 3 9
    # 冷视天下
