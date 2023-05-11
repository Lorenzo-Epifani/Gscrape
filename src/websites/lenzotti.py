import requests
from bs4 import BeautifulSoup
from lxml import etree
from pprint import pprint
from src.utils import get_regex

meta={
    'NAME' : 'lenzotti',
    'BASEURL' : 'https://shop.lenzotti.it/',
    'LOCATION' :['EU','Italy','Modena']
}

#AGGOINGI DECORATOR PER CARICARE DA STATIC
def search_on_site(query):
    '''
    This method make a search request on the website.
    Return the list of pages given by the research button of the target website.
    INPUT: QUERY
    OUTPUR: LIST OF SOUPS
    '''
    url = f'{meta["BASEURL"]}?s={query}&post_type=product&dgwt_wcas=1'
    headers = headers = {
        'Host':'shop.lenzotti.it:80',
        'User-Agent': 'Chrome v22.2 Linux Ubuntu',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
        }

    response = requests.get(url = url, headers=headers)#, params = '')
    soup = BeautifulSoup(response.content, 'html.parser')
    #...
    result = [soup]#+...
    return result

def record_parser(soup, query=None):
    '''
    This methos parse all the result of the website, and return a list of records standardized
    for our backend.
    INPUT: soup
    OUTPUT: list of record objects
    '''
    dom=etree.HTML(str(soup))
    elements = dom.xpath('//*[@id="main"]/div[1]/p/text()')
    #print(dir(elements))
    reg = get_regex('lenzotti_1')
    elements = int(reg.search(elements[0]).groups()[1])-int(reg.search(elements[0]).groups()[0])+1
    list_records_xpaths = [{
        'name':f'//*[@id="main"]/div[2]/ul/li[{i+1}]/div[3]/div/a/text()',
        'price':f'//*[@id="main"]/div[2]/ul/li[{i+1}]/div[3]/span/span/bdi/text()',
        'link':f'//*[@id="main"]/div[2]/ul/li[{i+1}]/div[2]/a',
        'img':f'//*[@id="main"]/div[2]/ul/li[{i+1}]/div[2]/a/img'
    }for i in range(elements)]

    records = [
        {k:dom.xpath(v) for k,v in rec_xpath.items()}
        for rec_xpath in list_records_xpaths
    ]
    results=[]
    for i,_r in enumerate(records):
        _r = {k:v[0] if len(v)==1 else None for k,v in _r.items()}
        #_r['price']=_r['price']
        _r['img']=_r['img'].attrib['src']
        _r['link']=_r['link'].attrib['href']
        results.append(_r)

    #pprint(records)
    #print(len(records))
    return results

def page_iterator(soup):
    next_soup=''
    return next_soup

def page_scroller(soup):
    pass