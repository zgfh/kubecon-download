#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 2019/6/26 10:09 AM
"""
URL = ["https://kccncosschn19chi.sched.com/2019-06-{}/overview?iframe=no".format(day) for day in ["24", "25", "26"]]

import requests
import os
import logging
from bs4 import BeautifulSoup
from urlparse import urljoin

LOG = logging.getLogger(__name__)


def mkdir(result_dir):
    if result_dir[-1] != "/":
        result_dir = result_dir + "/"
    if not os.path.exists(result_dir[:-1]):
        os.makedirs(result_dir)
    return result_dir


def downloadFile(url, output_path, local_filename='', type=""):
    if not local_filename:
        local_filename = url.split('/')[-1]
    if len(local_filename.split('.')) == 1:
        type = ".pdf"
    filename = os.path.join(output_path) + local_filename + type
    LOG.info(u"Download File={}".format(filename))

    while os.path.exists(filename):
        output_path = output_path + "_1"
    r = requests.get(url, allow_redirects=True)  # to get content after redirection
    with open(filename, 'wb') as f:
        f.write(r.content)
    return local_filename


def evnet(url, resut_dir=''):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html5lib')
    sched_files = soup.find_all('div', attrs={'class': "sched-file"})
    if not sched_files:
        LOG.exception(u"skip event {} {}".format(resut_dir, url))
        return
    files = sched_files[0].find_all('a')
    for file in files:
        try:
            downloadFile(urljoin(url, file.attrs['href']), mkdir(resut_dir))
        except Exception as e:
            LOG.exception(u"Download File={} error:".format(file))


def Main(resut_dir='events',
         urls=URL):
    for url_page in urls:
        res = requests.get(url_page)
        soup = BeautifulSoup(res.content, 'html5lib')
        date_str = soup.find_all('div', attrs={'class': "sched-current-date"})[0].text
        events = soup.find_all('span', attrs={'class': "event"})
        for event in events:
            event_links = event.find_all('a')
            for event_link in event_links:
                evnet(urljoin(url_page, event_link.attrs['href']),
                      os.path.join(mkdir(resut_dir), date_str, event_link.text))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)-8s %(message)s')
    Main()
