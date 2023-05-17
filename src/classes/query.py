

class Query:
    def __init__(self,search_string=None,
                 price_rng=None, category=None, 
                 state='U', condition=None, limit=0):
        '''
        State can be U or N (used or new)
        '''
        self.search_string = search_string #STRINGA TESTUALE DI RICERCA
        self.price_rng = price_rng #PREZZO
        self.category = category #CATEGORIA
        self.state = state #NAZIONE
        self.condition = condition #NUOVO/USATO. EXDEMO MAPPATO COME USATO
        self.limit = limit