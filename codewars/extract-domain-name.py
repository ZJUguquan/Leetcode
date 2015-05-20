# coding: utf-8

import re
from urlparse import urlparse
def domain_name(url):
    if '//' not in url:
        url = 'http://' + url
    url_netloc = urlparse(url).netloc
    print url_netloc
    domain = re.findall(r'(www\.)?(.*)\.', url_netloc)[0][1]
    return domain

# others method:

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

print domain_name("sina.com")