import requests
from bs4 import BeautifulSoup
from lxml import etree
from pprint import pprint
from src.classes.record import Record
from src.classes.query import Query
from time import sleep
from itertools import count
from src.utils import get_regex
import re
status=["OK"]
meta={
    'NAME' : 'gasmusicstore',
    'BASEURL' : 'https://www.gasmusicstore.com/',
    'LOCATION' :['EU','Italy','Gioia Del Colle']
}

#AGGOINGI DECORATOR PER CARICARE DA STATIC
def search_on_site(query):
    '''
    This method make a search request on the website.
    Return the list of pages given by the research button of the target website.

    INPUT: QUERY
    OUTPUR: LIST OF SOUPS

    '''
    url = f'{meta["BASEURL"]}?post_type=product&s={query.search_string}&_screma_i_prodotti=usato-negozio'
    response = requests.get(url = url)#, params = '')
    soup = BeautifulSoup(response.content, 'html.parser')
    results = [soup]#+...
    #...
    
    for page_i in range(2,2+query.limit):
        sleep(0.3)
        next_url = f'{meta["BASEURL"]}page/{page_i}/?post_type=product&s={query.search_string}'
        next_response = requests.get(url = next_url)#, params = '')
        if next_response.status_code!=200:
            break
        next_soup = BeautifulSoup(next_response.content, 'html.parser')
        results.append(next_soup)
        page_i=page_i+1
    return results

def record_parser(soup, query=None):
    '''
    This methos parse all the result of the website, and return a list of records standardized
    for our backend.

    INPUT: soup
    OUTPUT: list of record objects

    '''
    dom=etree.HTML(str(soup))
    xpaths_elem = lambda i: {
        'prod_name':f'/html/body/div[1]/div[1]/div[2]/div[2]/div/section[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/ul/li[{i+1}]/h3/a/text()',
        'price':f'/html/body/div[1]/div[1]/div[2]/div[2]/div/section[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/ul/li[{i+1}]/div[2]/div/div[1]/span/span/bdi/text()',
        'link':f'/html/body/div[1]/div[1]/div[2]/div[2]/div/section[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/ul/li[{i+1}]/div[1]/div/a',
        'img':f'/html/body/div[1]/div[1]/div[2]/div[2]/div/section[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/ul/li[{i+1}]/div[1]/div/a/img'
    }
    web_items = []
    for index in count():
        item = {k:dom.xpath(v) for k,v in xpaths_elem(index).items()}
        if all([True if len(v)==0 else False for v in item.values()]):
            break
        web_items.append(item)

    result = []
    for i,_r in enumerate(web_items):
        _r['prod_name'] = _r['prod_name'][0]
        _r['link'] = _r['link'][0].attrib['href']
        _r['price'] = _r['price'][0] if len(_r['price'])>0 else 'N/A'
        images=_r['img'][0]
        #if images.attrib.has_key('srcset'):
        #    images = images.attrib['srcset'].split(', ')
        #    _r['img'] = [_el.split(' ') for _el in images][0][0]
        #else:
        _r['img'] = [images.attrib['src']]
        #_r['img'] = re.search(get_regex('gms_1'),_r['img']).groups()[0]
        result.append(Record(**_r))
    #pprint(records)
    #print(len(records))
    return result

def query_to_url(query):
    '''
    This method convert a query object to an url to request via http
    '''
    pass

def page_iterator(soup):
    next_soup=''
    return next_soup

def page_scroller(soup):
    pass

def build_search_url_from_query(query):
    pass