import json
import re
import requests
from requests.exceptions import RequestException
import time



def getOnePage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parseOnePage(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*?data-src="(.*?)".*?'
                         + 'star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'index': item[0],
            'title': item[1],
            'image': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }
    
def writeToFile(content):
    with open('maoYan.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = getOnePage(url)
    for item in parseOnePage(html):
        # print(item)# 相当于进度条吧，个人觉得没必要
        writeToFile(item)
        
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
