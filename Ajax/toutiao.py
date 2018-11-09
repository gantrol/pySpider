
from urllib.parse import urlencode
import requests
import os# 读写模块
from hashlib import md5# 去重复
from multiprocessing.pool import Pool


GROUP_0 = 1
GROUP_E = 3

# 以offset作为参数传递
def get_page(offset):
    params = {
        'offset': offset,
        'format':'json',
        'keyword':'街拍',# 更改此处即可换搜索关键词
        'autoload':'true',
        'count':'20',
        'cur_tab':'3',
        'from':'gallery'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        return None


# 解析，返回图片标题与链接，字典。
def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            # print(item)
            image_list = item.get('image_list')
            title = item.get('title')
            # print(image_list)
            if image_list:
                for image in image_list:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        local_image_url = item.get('image')
        new_image_url = local_image_url.replace('list','large')
        response = requests.get('http:' + new_image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')
    

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_0, GROUP_E + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
