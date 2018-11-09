from bs4 import BeautifulSoup
import csv
import re
import requests
import time
from multiprocessing.pool import Pool

# 可更改为'<地区名>/'，如'panyu/'、'tianhe/’等。
qu = 'huadou/'
# 输入最后页面数（最大为100）
end = 3
"""
以上两项可更改为字典形式遍历。
"""
# 输入'<文件名>.csv'
csvname = '链家广州租房10花都.csv'
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
    pattern = re.compile('<span>/</span>.*?<span>/</span>(.*?)</div></div><div class="chanquan">')
    year = re.findall(pattern, html)
    soup = BeautifulSoup(html, 'lxml')
    items = soup.select("h2 a")
    return(year, items)

def parse_page(year0, text):
    info = {}
    soup = BeautifulSoup(text,'lxml')
    weizhi = re.compile('<p><i>位置：</i><a href=".*?">(.*?)</a>')
    #https://gz.lianjia.com/zufang/panyu/"
    info['行政区域'] = re.findall(weizhi, text)[0]
    info['楼盘标题'] = soup.select('h1.main')[0].text
    info['户型属性'] = soup.select('div.zf-room p.lf')[1].text[5:].strip()
    info['面积属性'] = soup.select('div.zf-room p.lf')[0].text[3:]
    info['朝向属性'] = soup.select('div.zf-room p.lf')[3].text[5:]
    info['楼层'] = soup.select('div.zf-room p.lf')[2].text[3:]
    info['建设年份'] = year0
    quwei = re.compile('<p><i>位置：</i><a href=".*?">.*?</a>.*?>(.*?)<')
    info['区位'] = re.findall(quwei, text)[0]
    info['租金'] = soup.select('span.total')[0].text + '元/月'
    parternxy = re.compile("resblockPosition:'(.*?),(.*?)'")
    items = re.findall(parternxy, text)
    for item in items:
        info['坐标经度'] = item[0]
        info['坐标纬度'] = item[1]
    return info

def write_to_csv(info):
    with open(csvname,'a',encoding='gb2312', errors="ignore", newline='') as csvfile:
        fieldnames = ['行政区域', '楼盘标题', '户型属性', '面积属性', '朝向属性', '楼层', '建设年份', '区位', '租金', '坐标经度', '坐标纬度']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(info)


def main(pg):
    url = 'https://gz.lianjia.com/zufang/' + qu + 'pg' + str(pg)
    # 检查点
    print(pg)
    html = get_one_page(url)
    year, items = parse_one_page(html)
    for i in range(len(items)):
        item0 = items[i].attrs['href']
        year0 = year[i]
        text = get_one_page(item0)
        #print(parse_page(text))
        info = parse_page(year0, text)
        # print(info)
        write_to_csv(info)

if __name__ == '__main__':
    pool = Pool()
    groups = ([x for x in range(1, end + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
    # for i in range(0, 100):
    #     print(i + 1)
    #     main(pg=i + 1)
    #     time.sleep(5)
