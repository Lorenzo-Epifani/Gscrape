from pprint import pprint
from bs4 import BeautifulSoup
import src.websites
import pkgutil
from importlib import import_module
from src.classes.webagent import WebAgent
from src.classes.query import Query

def scrape(context):
    query = Query(
        search_string=context['_LOC']['query'],
        limit=0
    )
    sitelist = [name for _, name, _ in pkgutil.iter_modules(src.websites.__path__)]
    result=[]
    for site in sitelist:
        agent_template = import_module(f'src.websites.{site}','.') 
        if 'DEV' in agent_template.status:
            continue
        agent = WebAgent(agent_template, pre=False)
        result.append({'source':agent_template.meta, 'content':agent.get_product_by_query(query)})
    return result




