import json
from urllib.parse import urlencode
import requests
import os# 读写模块
from hashlib import md5# 去重复

"""
get_images方法的页面追踪没做好。
"""


headers = {
    'Host': 'huaban.com',
    'Referer': 'http://huaban.com/favorite/beauty',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie':'_uab_collina=153572835042485686577819; __auc=1347e9a0165908af7a381f97a1d; __gads=ID=33e8c3248d63a6b2:T=1535728349:S=ALNI_MYuKpeTylFniJoQYMOFGPKElTIUOw; UM_distinctid=165928d4c649ca-046ed74c237be7-9393265-144000-165928d4c66119; CNZZDATA1256914954=1691845574-1536568949-null%7C1536568949; sid=K6dSvfe91zRqyV2iy5tar6qkG8X.4lv%2FrHOY6dyww6%2FtSCQqhVCB1h8SsHBeaVEulp%2FiX38; _hmt=1; uid=19470664; _f=iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAAC00lEQVRYR%2BWWT0hUURSHv6MTUZs2swgiZhH2RxdROEYUOBUYlhQRSAxEUUwhUbNIUFq4cFEKBg4RhkNRCbOQIgLDiEiFXDiK1CKMosUsQ5EMskU2J%2B6b%2B4ZxbMYpxsp8m7nz7n33nu%2F8fue8J6gq%2BS4RyTv%2FhyY7pzvzxikGZO3sLNFQiGAsRiwYJBSN0tLaSlN7uwlzBKgTmMoXs4IX6AO6Be4Um68gEHOod2qKSDhMOBJhyuvFwHU0NtLQ1VUuMFFIYApnzLp%2FFgQ4BQSA08BdYFCgWaENaAJiQAg4AVQCh4Bhe88H9APm96DdawZYB2wqRG2TnF9SpK%2Bujl0jxkmpK%2BHz4UskyoFJIAKEgQqgFrgHXARagFbgBrAbOGABzP13wGYLYrY0zxko86wZHwMeFaL4L4HkstbPQKwibl2st4EZEMdaCtUm43ZsLHcbMEVnQGozFO0XGFrMusUCSdjMdwBHbJZNVs3%2FBqA5QxEXxNjOCdoq8yFDkaUBKaRrAY22Hp4C24ALwE2byY%2FAgLVYFAgCZ60abh3FAQ9QCmy36pj6KqgrFqxITmmX03vkv3khrlgQfRmv4Js8QfChJFilh%2FlesoGk9jpJKZF6qa58Zobz1%2Bp12Vdlai196UC8A5HL7j6yt%2BqNO6lDYzV2z089W8d906u%2F5q6A3%2F3WcgKckweI3pLqKvOOQQfHLiG8dSFS90YfO6d79Apz0oNIcxoyFWg3JXKOZLIGkTIJ%2BI%2FOAzVrVNt6tozvWBKQzCDdw3Uw3oKHh%2FOyOjg6jGivgXWgVN%2B7quhQPIxKvQT8e5zsq7bh0ZMLVFlykIzDHWupHpeA%2F3zaGlmqLQBJ2Wq%2FBPw7%2FyqIVWUc1RcInxFmXJulYZaDIg6IzSroBB6uZtpi2dRIVld6nV2oubqWbQAbHUtlda1U90vep4RrlPLc7Y6Ta74QK3tV%2FK612EdesedXzCfKD1HkETenQIVMAAAAAElFTkSuQmCC%2CWin32.1536.864.24; Hm_lvt_d4a0e7c3cd16eb58a65472f40e7ee543=1539492274,1540619161,1541761884; __asc=d96cdd8b166f82b61f0c426b020; CNZZDATA1256903590=1150130295-1535761091-%7C1541762484; Hm_lpvt_d4a0e7c3cd16eb58a65472f40e7ee543=1541764064; _cnzz_CV1256903590=is-logon%7Clogged-in%7C1541764065271%26urlname%7Ck5spfh6f1d%7C1541764065271',

}


def get_page(max):
    params = {
        'max': max,
        'limit': 20,
        'wfl': 1
    }
    url = 'http://huaban.com/favorite/beauty?jo9yikt6' + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:

            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


# 解析，返回图片标题与链接，字典。
def get_images(json0):
    pins = json0.get('pins')
    if pins:
        for pin in pins:
            # print(item)
            hua = {}
            image_url = 'http://img.hb.aicdn.com/' + pin.get('file').get('key')
            title = pin.get('board').get('title')
            # print(image_list)
            if image_url:
                hua['image'] = image_url
                hua['title'] = title
                yield hua
        max_n = pins[-1].get('pin_id')
        print(max_n)
        json_n = get_page(max_n)
        get_images(json_n)


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        image_url = item.get('image')
        response = requests.get(image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(max):
    json0 = get_page(max)
    for item in get_images(json0):
        print(item)
        save_image(item)


if __name__ == '__main__':
    main(2108450734)
