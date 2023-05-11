import requests
from bs4 import BeautifulSoup
from lxml import etree
from pprint import pprint

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
    url = f'{meta["BASEURL"]}?post_type=product&s={query}'
    response = requests.get(url = url)#, params = '')
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
    elements = dom.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/section[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/ul/li')
    cursor=[]
    list_records_xpaths = [{
        'name':f'/html/body/div[1]/div[1]/div[2]/div[2]/div/section[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/ul/li[{i+1}]/h3/a/text()',
        'price':f'/html/body/div[1]/div[1]/div[2]/div[2]/div/section[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/ul/li[{i+1}]/div[2]/div/div[1]/span/span/bdi/text()',
        'link':f'/html/body/div[1]/div[1]/div[2]/div[2]/div/section[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/ul/li[{i+1}]/div[1]/div/a',
        'img':f'/html/body/div[1]/div[1]/div[2]/div[2]/div/section[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/ul/li[{i+1}]/div[1]/div/a/img'
    }for i in range(len(elements))]

    records = [
        {k:dom.xpath(v) for k,v in rec_xpath.items()}
        for rec_xpath in list_records_xpaths
    ]
    for i,_r in enumerate(records):
        _r['name'] = _r['name'][0]
        _r['link'] = _r['link'][0].attrib
        _r['price'] = _r['price'][0] if len(_r['price'])>0 else 'N/A'
        images=_r['img'][0]
        if images.attrib.has_key('srcset'):
            images = images.attrib['srcset'].split(', ')
            _r['img'] = [_el.split(' ') for _el in images][0][0]
        else:
            _r['img'] = [{'std':images.attrib['src']}]
    #pprint(records)
    #print(len(records))
    return records