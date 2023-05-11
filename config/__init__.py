from importlib.resources import path
from importlib import import_module
import os 
import json
import re
this_dirname = os.path.dirname(__file__)
global_conf=None
with open(f'{this_dirname}/global_conf.json') as g_f:
    global_conf=json.load(g_f)
all_folders=[a for a in os.walk(this_dirname)][0][1]
conf_list=[a for a in all_folders if bool(re.findall(r"__c$",a))]
entry={}
validation={}
for module_name in conf_list:
    mod=import_module(f'config.{module_name}.validator','.')
    for elem in conf_list:
        entry[module_name]=mod.content
        validation[module_name]=mod.validation
    
