import os
import time
import uuid

import requests
from bs4 import BeautifulSoup

def out_wrapper(func):  #decorator in measuring the time consuming 
    def inner_wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('Used time {}'.format(stop_time-start_time))
    return inner_wrapper

def save_flag(img, filename):  #save the single pic
    path = os.path.join('down_photos', filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def download_one(url):  #download one pic
    image = requests.get(url)
    save_flag(image.content, str(uuid.uuid4()))

def user_conf():  #get all the url in pics
    url = 'http://www.nipic.com/topic/show_27202_1.html'
    ret = requests.get(url)
    soup = BeautifulSoup(ret.text, "lxml")
    zzr = soup.find_all('img')
    ret = []
    num = 0
    for item in zzr:
        if 'pic' in item.get("src") and num < 30:
            num += 1
            ret.append(item.get("src"))
    return ret

@out_wrapper
def download_many():
    zzr = user_conf()
    for item in zzr:
        download_one(item)

if __name__ == '__main__':
    download_many()
