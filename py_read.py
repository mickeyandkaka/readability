# -*- coding:utf-8 -*-

import re
import chardet
import requests
from readability import Readability


class py_read(object):
    """wrap the readability object"""

    # constract header
    scrap_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36'
            }


    def __init__(self, url):
        self.url         = self.regularization(url)
        self.response    = requests.get(url, timeout = 5, headers = self.scrap_header)
        self.charset     = self.get_html_charset(self.response)
        self.readability = Readability(self.response.content, self.url, self.charset)

        self.title       = self.readability.title
        self.content     = self.readability.content


    def regularization(self, url):
        if url.startswith('http://') is False and \
            url.startswith('https://') is False:
            url = 'http://' + url
        return url

    def get_html_charset(self, response):
        # firstly check whether the charset is in Header's Content-Type
        # secondly check the source code whether there's charset
        # if both failed, using chardet to detect the encode

        charset      = str()
        p            = re.compile(r'charset="?(gb2312|gbk|utf-8)"?', re.I)
        content_type = response.headers['Content-Type'].lower()
        
        if 'charset' in content_type:
            charset = p.search(content_type).group().replace('charset=','').replace('"','')
        else:
            charset = p.search(response.text.lower()).group().replace('charset=','').replace('"','')


        if charset == '':
            charset = chardet.detect(response.content)

        # using gbk instead of gb2312 in case of unexpected errors
        if charset == 'gb2312':
            charset = 'gbk'

        return charset

