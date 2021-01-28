# >>> scrapy runspider -L INFO --set FEED_EXPORT_ENCODING=utf-8 asyncscrapy.py

# the most important step of any data-driven project is obtaining quality data

#https://stackoverflow.com/questions/63941441/web-scraping-the-audio-and-related-text-form-ganjoor-site-by-colab-as-persian-sp

# where possible, the macro structure of the composition is preserved in the html tags,
# perhaps allowing training to capture couplet and quatrain structure, should it be desired
# alternatively, add token demarcating chapter, couplet, quartet

import scrapy
from bs4 import BeautifulSoup
import os
import re
from values import *


WRITE_DIR = './spider_data/'
START_TOKEN = '[START]'
END_TOKEN = '[END]'
REGEX = re.compile(r'sh[0-9]+')
TARGET = {}

TARGET |= ROODAKI
TGNAME = 'ROODAKI'

def make_urls(target):
    urls = []
    for k,v in target.items():
        if v==0:
            urls.append(k)
        else:
            urls += [k + 'sh' + str(i) for i in range(1, 1+v)]
    return urls
def clean(raw):
    t = BeautifulSoup(raw, "lxml").find('article')
    t.find('h2').decompose()
    [x.decompose() for x in t.find_all('a')]
    [x.decompose() for x in t.find_all('div', style=lambda v:v)]
    [x.decompose() for x in t.find_all('div', {'class':'spacer'})]
    [x.decompose() for x in t.find_all('nav')]
    [x.decompose() for x in t.find_all('div', {'id':'comments'})]
    [x.decompose() for x in t.find_all('div', {'class':'helpers'})]
    [x.decompose() for x in t.find_all('div', {'class':'cat'})]
    [x.decompose() for x in t.find_all('div', {'class':'com'})]
    t = t.__str__().replace('\n\n\n\n','').replace('<p>','').replace('</p>','')
    t = t.replace('</article>','').replace('</div>','').replace('\r','')
    t = t.replace('<small>', '').replace('</small>', '')
    t = t.replace('<em>', '').replace('</em>', '')
    t = t.replace('<sup>', '').replace('</sup>', '')
    t = t.replace('<br style="clear:both;"/>', '')
    # special tokens
    t = t.replace('<article>','[A]')
    t = t.replace('<div class="n">','[N]')
    t = t.replace('<div class="b">','[B]')
    t = t.replace('<div class="m1">','[M1]')
    t = t.replace('<div class="m2">','[M2]')
    t = t.replace('<div class="b2">','[B2]')
    return t
def order_and_flatten_dict(d):
    s = ''
    for i in sorted(d.keys()):
        s += d[i]
    return s


class GanjoorSpider(scrapy.Spider):
    name = 'Ganjoor.net Scrapy Spider'

    start_urls = make_urls(TARGET)
    data = {}

    def parse(self, response):
        cleaned = clean(response.css('div.poem article').get())
        stem = '/'.join(response.url.split('/')[3:-1])
        if REGEX.search(stem):
            i = int(stem.split('/')[-1][2:])
            stem = '/'.join(stem.split('/')[:-1])
            if stem in self.data:
                self.data[stem] |= {i: cleaned}
            else:
                self.data[stem] = {i: cleaned}
        else:
            self.data |= {stem : cleaned}
        #yield {stem:cleaned}
        #next_page = response.css('div.navleft a::attr("href")').get()
        #if next_page is not None:
        #   yield response.follow(next_page, self.parse)

    def closed(self, reason):
        print(reason)
        print('\t' + TGNAME)
        print('\texpected ' + str(sum([max(v,1) for v in TARGET.values()])))
        for stem in self.data.keys():
            out = self.data[stem]
            out = order_and_flatten_dict(out) if isinstance(out, dict) else out
            #os.makedirs(stem, exist_ok=True)
            with open(WRITE_DIR + stem.replace('/','_') + '.txt', 'w') as f:
                f.write(START_TOKEN + out + END_TOKEN)

