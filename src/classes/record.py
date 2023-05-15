class Record:
    def __init__(self, prod_name, price, link, img=None, categ={}) -> None:
        self.prod_name = prod_name
        self.price = price
        self.link = link
        self.img = img
        self.categ = categ
        #obj_meta = import_module(f'src.websites.{name}','.')
        #self.initiator = agent_tmp.initiator#obj_meta.souper
        #self.miner = agent_tmp.miner#obj_meta.parser
    def to_dict(self):
        return {
            "prod_name" : self.prod_name,
            "price" : self.price,
            "link" : self.link,
            "img" : self.img,
            "category" : self.category
        }

