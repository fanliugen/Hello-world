import requests
import re
import json
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import pymongo
from redis import StrictRedis

def writetoMongo(item):
    client = pymongo.MongoClient(host='localhost',port=27017)
    db=client['penshaji']
    collection = db.sheet
    result = collection.insert_one(item)

def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None
def parse_one_page(html):
    #pyquery方法
    doc = pq(html)
    items = doc('.right  .content li').items()
    for item in items:
        yield {
            'title':item('a').text(),
            'link':item('a').attr('href'),
            'date':item('span').text(),
        }

    #BeautifulSoup方法
    # soup = BeautifulSoup(html,'lxml')
    # items = soup.select('.right  .content li')
    # for item in items:
    #     yield {
    #         'title':item.select('a')[0].string,
    #         'link':item.select('a')[0].attrs['href'],
    #         'date':item.select('span')[0].string,
    #     }

    #正则表达式方法
    # pattern = re.compile('<li><a.*?href=(.*?)>(.*?)</a>.*?</li>',re.S)
    # items = re.findall(pattern,text)
    # for item in items:
    #     yield {
    #         'title':item[1],
    #         'link':item[0]
    #     }
    # return items
def main(page):
    url = 'http://www.psj666.com/news_gsxwck6/p/%s/' % (page)
    print('============'+url)
    html = get_one_page(url)
    items=parse_one_page(html)
    for item in items:
        # print(item)
        #save to file 方法
        # with open('penshaji.txt','a',encoding='utf-8') as file:
        #     file.write(json.dumps(item,ensure_ascii=False)+'\n')

        #save to mongodb方法 
        writetoMongo(item)

    # print(html)
    # with open('html','a',encoding='utf-8') as file:
    #     file.write(html)


if __name__ == '__main__':
    for i in  range(1,4,1):
        main(i)

