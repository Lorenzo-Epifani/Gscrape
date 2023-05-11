import src.websites
from importlib import import_module
from src.utils import load_soup


class WebAgent:
    def __init__(self, agent_tmp, pre=False) -> None:
        self.meta = agent_tmp.meta
        self.pre = pre
        self.search_on_site=agent_tmp.search_on_site
        self.record_parser=agent_tmp.record_parser
        #obj_meta = import_module(f'src.websites.{name}','.')
        #self.initiator = agent_tmp.initiator#obj_meta.souper
        #self.miner = agent_tmp.miner#obj_meta.parser


    def get_product_by_query(self,query):
        search_result_pages = self.search_on_site(query)
        records=[]
        for _page in search_result_pages:
            records.extend(self.record_parser(_page))
        return records
