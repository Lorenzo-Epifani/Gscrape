import json
from socket import timeout
from typing import List, Set, Dict, Union, Any, Callable, Tuple
from xml.dom import ValidationErr
from cerberus import Validator
import json
from pprint import pprint
import os 
VALIDATE_ENABLED = True

def type_required(_type,required=True):
    return {'type': _type,'required':required}

def get_rules():
    rule_list=[]
    doc_rule = ({'doc':type_required('string')}, True)
    rule_list.append(doc_rule)

    #CREATE AND APPEND HERE YOUR VALIDATION RULES
    #A RULE IS A 2 DIM TUPLE:
    #----POS 1 : THE STD CERBERUS RULE
    #----POS 2 : ALLOW UNKNOWN OPTION FOR VALIDATOR. 

    return rule_list

def _init()->Dict[str,Dict[str,str]]:


    rule_list = get_rules()
    #APPEND OTHER RULES TO VALIDATE

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/values.json') as config_file:
        conf = json.load(config_file) #CONFIG FILE

    results=[]

    for i,rule in enumerate(rule_list):
        val_res= {"rule_n":i, "status":None, "err":None}
        v=Validator(rule[0],allow_unknown=rule[1])
        val_ok = v.validate(conf)
        val_res['status'] = "OK" if val_ok else "NOK"
        val_res['err'] = v.errors
        results.append(val_res)
        if VALIDATE_ENABLED and not all([el['status']=="OK" for el in results ]):
            print(results)
            raise ValidationErr() 
    return (conf,results)

def _info():
    pprint(_init())

content, validation = _init()
