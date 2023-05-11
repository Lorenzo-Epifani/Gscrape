from distutils.command.config import config
from os import getenv
import sys
from src.monoscrape import scrape 
import config
from pprint import pprint
#print(config.entry['conf1'])
#print(config.global_conf)
cmd_to_f={}

def _help():
    print(f'\nCOMMANDS LIST:\n')
    for elem in config.conf_list:
        
        print('##################################\n')
        print(f'Function name:\n{elem.replace("__c","")}\n')
        print(f'Description:\n{config.entry[elem]["doc"]}\n')
    print('##################################\n')
    exit()
    
def set_config(key):
    def inner(func):
        global cmd_to_f
        cla_1 = None
        try:
            config_name = f'{key}__c'
        except IndexError as e:
            _help()
        _context={
            "_LOC" : config.entry[config_name],
            "_GLB" : config.global_conf,
        }
        cmd_to_f[key] = lambda: func(_context)
        return func
    return inner


@set_config('search_all')
def _search_all(context):
    '''
    Write your code here.
    This will be executed with 'function1' as command line argument.
    _LOC takes values from config/function1/value.json
    _GLB takes values from config/global.json
    '''
    scrape(context)


@set_config('function2')
def s2_count(context):
    '''
    Write your code here.
    This will be executed with 'function2' as command line argument.
    _LOC takes values from config/function2/value.json
    _GLB takes values from config/global.json
    '''
    pass


@set_config('debug')
def debug_function(context):
    '''
    Write your code here.
    This will be executed with 'debug' as command line argument.
    _LOC takes values from config/debug/value.json
    _GLB takes values from config/global.json

    '''
    print('debug')
    pprint(context)
    pass





 
 
