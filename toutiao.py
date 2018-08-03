import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool
import time

def get_page(offset):
    params={
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
    }
    url = 'https://www.toutiao.com/search_content/?'+ urlencode(params)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    data=json.get('data')
    if data:
        for item in data:
            title = item.get('title')
            images_list = item.get('image_list')
            if images_list:
                for image in images_list:
                    yield {
                        'image':image.get('url'),
                        'title':title
                    }



def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        local_image_url = item.get('image')
        new_image_url=local_image_url.replace('list','large')

        response = requests.get('https:'+ new_image_url)
        if response.status_code == 200:
            file_path='{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download',file_path)
    except requests.ConnectionError:
        print('Faile to Save image')

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_END = 20


if __name__ == '__main__':
    # pool = Pool()
    # groups= ([x*20 for x in range(GROUP_START,GROUP_END+1)])
    # pool.map(main,groups)
    # pool.close()
    # pool.join()
    for i in range(20):
        main(offset=i*10)
        time.sleep(1)