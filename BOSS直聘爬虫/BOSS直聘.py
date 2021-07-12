# coding=gbk
# -*- coding:uft-8 -*-
# BOSS直聘

from lxml import etree
import random
from time import sleep
import re
from seleTool import sele
import requests


def collect(url):
    res = sele(url)
    tree = etree.HTML(res)
    for li in tree.xpath('//div[@class="job-list"]/ul/li'):
        numLs = ['133', '149', '153', '173', '130', '131', '132', '134', '135', '136', '137', '138', '139', '159', '188']
        detailUrl = 'https://www.zhipin.com' + li.xpath('.//span[@class="job-name"]/a/@href')[0]
        detailRes = sele(detailUrl)
        detailTree = etree.HTML(detailRes)
        name = li.xpath('.//span[@class="job-name"]/a/text()')[0]
        company = li.xpath('.//div[@class="company-text"]/h3/a/text()')[0]
        info = ''.join(detailTree.xpath('//div[@class="job-sec"]/div/text()')).replace('\n', '/').replace(',', '//').replace(' ', '').strip()
        bandUrl = detailTree.xpath('//div[@class="company-info"]/a/img/@src')[0]
        headers = {
            'user-agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/91.0.4472.124Safari/537.36'
        }
        band = requests.get(url=bandUrl, headers=headers).content
        with open(f'./公司图标/{company}.jpg', 'wb') as f:
            f.write(band)
        ex = '[a-zA-Z]+'
        pattern = re.compile(ex)
        skill = '/'.join(pattern.findall(info))
        phone = random.choice(numLs) + str(random.randint(10000000, 100000000))
        address = li.xpath('.//span[@class="job-area-wrapper"]/span/text()')[0]
        salary = li.xpath('.//div[@class="job-limit clearfix"]/span/text()')[0]
        code = ''.join([random.choice('0123456789qwertyuiopasdfghjklzxcvbnm') for i in range(10)])
        row = f'{name},{info},{company},{skill},{phone},{address},{salary},{code}'
        try:
            print(row)
        except Exception as e:
            print(str(e))
        with open('BOSS直聘.csv', 'a', encoding='utf-8-sig') as f:
            f.write(row + '\n')
        sleep(1)


def main():
    url = 'https://www.zhipin.com/c101010100/d_203-e_108/?query=%E5%AE%9E%E4%B9%A0&amp;ka=sel-degree-203'
    collect(url)


if __name__ == '__main__':
    main()
