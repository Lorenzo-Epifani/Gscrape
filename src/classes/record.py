from enum import Enum


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

class Status(Enum):
    USED = 1
    NEW = 2

class Category:
    def __init__(self,kv_list) -> None:
        for k,v in kv_list:
            setattr(self,k,v) 
    
categories_schema=[
    ('GUITAR',Category([
        ('SOLID',1),
        ('SEMI_HOLLOW',2),
        ('ACOUSTIC',3),
        ('CLASSIC',4)])
        ),
    ('BASS',Category([
        ('SOLID',1),
        ('SEMI_HOLLOW',2),
        ('ACOUSTIC',3)])
        ),
    ('AMP',Category([
        ('HEAD_CONE',1),
        ('COMBO',2)])
        )
]

CATEGORIES = Category(categories_schema)
print(CATEGORIES.GUITAR.SOLID)

   

