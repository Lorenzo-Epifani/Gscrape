import sys
import pickle
import os 
import re
def store_soup(soup,name,query):
    sys.setrecursionlimit(99999)
    with open(f'./src/websites/static/{name}_{query}.pkl', 'wb') as outp:
        pickle.dump(soup, outp, pickle.HIGHEST_PROTOCOL)
    sys.setrecursionlimit(1000)

def load_soup(name,query):
    with open(f'./src/websites/static/{name}_{query}.pkl', 'rb') as file:
        soup = pickle.load(file)
    return soup

def get_regex(reg_name):
    reg_dict={
        'lenzotti_1': re.compile(r'di ([0-9]+)-([0-9]+) di'),
        "example":re.compile(r'_([^_]+)_[^._]+\.jp2')
    }

    result = reg_dict.get(reg_name, None)
    if result == None:
        raise Exception('REGEX_NAME_ERROR')
    return result

def make_dotdict(_dict):
    class dotdict(dict):
        """dot.notation access to dictionary attributes"""
        __getattr__ = dict.get
        __setattr__ = dict.__setitem__
        __delattr__ = dict.__delitem__

    for k,v in _dict.items():
        if type(v) is dict:
            _dict[k]=make_dotdict(v)
    _dict=dotdict(_dict)
    return _dict


    