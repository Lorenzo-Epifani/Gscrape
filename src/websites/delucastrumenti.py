import requests
from bs4 import BeautifulSoup
from lxml import etree
from pprint import pprint
from src.utils import get_regex
from src.classes.record import Record
from src.classes.query import Query
from time import sleep
from itertools import count


status=["DEV"]
meta={
    'NAME' : 'delucastrumenti',
    'BASEURL' : 'https://www.delucastrumenti.com/', #BASEURL WITH BACKSLASH INCLUDED
    'LOCATION' :['EU','Italy','Salerno']
}

def search_on_site(query):
    '''
    This method make a search request on the website.
    Return the list of pages given by the research button of the target website.

    INPUT: query item
    OUTPUT: list of soups

    '''
    url = f'{meta["BASEURL"]}?post_type=product&s={query.search_string}'
    headers = headers = {
        'Host':f'{meta["BASEURL"]}:80',
        'User-Agent': 'Chrome v22.2 Linux Ubuntu',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
        }

    response = requests.get(url = url, headers = headers)#, params = '')
    soup = BeautifulSoup(response.content, 'html.parser')
    #...
    result = [soup]
    for page_i in range(2,2+query.limit):
        sleep(0.3)
        next_url = f'{meta["BASEURL"]}page/{page_i}/?s={query.search_string}&post_type=product&dgwt_wcas=1'
        next_response = requests.get(url = next_url, headers=headers)#, params = '')
        if next_response.status_code!=200:
            break
        next_soup = BeautifulSoup(next_response.content, 'html.parser')
        result.append(next_soup)
        page_i=page_i+1
    return result

def record_parser(soup, query=None):
    '''
    This methos parse all the result of the website, and return a list of records standardized
    for our backend.

    INPUT: soup
    OUTPUT: list of record objects

    '''
    
    dom=etree.HTML(str(soup))

    xpaths_elem = lambda i: {   
        'prod_name':f'//*[@id="main"]/div[2]/ul/li[{i+1}]/div[3]/div/a/text()',
        'price':f'//*[@id="main"]/div[2]/ul/li[{i+1}]/div[3]/span/span/bdi/text()',
        'link':f'//*[@id="main"]/div[2]/ul/li[{i+1}]/div[2]/a',
        'img':f'//*[@id="main"]/div[2]/ul/li[{i+1}]/div[2]/a/img'
    }
    web_items = []
    for index in count():
        item = {k:dom.xpath(v) for k,v in xpaths_elem(index).items()}
        if all([True if len(v)==0 else False for v in item.values()]):
            break
        web_items.append(item)
    results=[]
    for i,_r in enumerate(web_items):
        _r = {k:v[0] if len(v)==1 else None for k,v in _r.items()}
        #_r['price']=_r['price']
        _r['img']=_r['img'].attrib['src']
        _r['link']=_r['link'].attrib['href']
        results.append(Record(**_r))

    #pprint(records)
    #print(len(records))
    return results

def query_to_url(query):
    '''
    This method convert a query object to an url to request via http
    '''
    pass

