from bs4 import BeautifulSoup
import csv
import re
import requests
import time
from multiprocessing.pool import Pool


# 可更改为'<地区名>/'，如'panyu/'、'tianhe/’等。
qu = 'yuexiu'
# 输入最后页面数（此网站页面数最大为100）
end = 52
"""
以上两项可更改为字典形式遍历，则理论上可一次爬完。但此爬虫非分布式爬虫，稳定性一般，不推荐使用。
"""
# 输入'<文件名>.csv'
csvname = '链家广州二手房4越秀.csv'


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
        return response.text
    except requests.ConnectionError:
        return None

def parse_one_page(html):
    pattern = re.compile('<div.*?class="item".*?data-houseid=".*?"><a class="img".*?href="(.*?)"', re.S)
    items = re.findall(pattern, html)
    return(items)

def parse_page(text):
    info = {}
    soup = BeautifulSoup(text,'lxml')
    info['行政区域'] = soup.select('.info a')[0].text
    info['楼盘标题'] = soup.select('h1.main')[0].text
    info['户型属性'] = soup.select('div.room div.mainInfo')[0].text
    info['面积属性'] = soup.select('div.area div.mainInfo')[0].text
    info['朝向属性'] = soup.select('div.type div.mainInfo')[0].text
    info['装修类型'] = soup.select('div.introContent div.content ul li')[8].text[4:]
    info['电梯配置'] = soup.select('div.introContent div.content ul li')[10].text[4:]
    info['楼层'] = soup.select('div.introContent div.content ul li')[2].text[4:]
    info['建设年份'] = soup.select('.subInfo')[2].text
    info['区位'] = soup.select('.info a')[1].text
    info['售价'] = soup.select('.total')[0].text + '万'
    info['单价'] = soup.select('.unitPriceValue')[0].text
    parternxy = re.compile("resblockPosition:'(.*?),(.*?)'")
    items = re.findall(parternxy, text)
    for item in items:
        info['坐标经度'] = item[0]
        info['坐标纬度'] = item[1]
    return info

def write_to_csv(info):
    with open(csvname,'a',encoding='gb2312', errors="ignore", newline='') as csvfile:
        fieldnames = ['行政区域', '楼盘标题', '户型属性', '面积属性', '朝向属性', '装修类型', '电梯配置', '楼层', '建设年份', '区位', '售价', '单价', '坐标经度', '坐标纬度']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(info)


def main(pg):
    url = 'https://gz.lianjia.com/ershoufang/' + qu + '/pg' + str(pg)
    html = get_one_page(url)
    items = parse_one_page(html)
    for item in items:
        text = get_one_page(item)
        #print(parse_page(text))
        info = parse_page(text)
        print(info)
        write_to_csv(info)



if __name__ == '__main__':
    pool = Pool()
    groups = ([x for x in range(0, end + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
    # for i in range(0, 100):
    #     print(i + 1)
    #     main(pg=i + 1)
    #     time.sleep(5)

