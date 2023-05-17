
import inspect

class STATUS:
    USED = 'USED'
    NEW = 'NEW'

class CAT:
    class GUITAR:
        SOLID =  'SOLID'
        SEMI_HOLLOW = 'SEMI_HOLLOW'
        ACOUSTIC = 'ACOUSTIC'
        CLASSIC = 'CLASSIC'
    class BASS:
        SOLID = 'SOLID'
        SEMI_HOLLOW = 'SEMI_HOLLOW'
        ACOUSTIC = 'ACOUSTIC'
    class AMP:
        HEAD_CONE = 'HEAD_CONE'
        COMBO = 'COMBO'
    for cls in [GUITAR,BASS,AMP]:
        #print(inspect.getmembers(cls))
        for attr in inspect.getmembers(cls):
            if type(attr) == tuple and all([True if type(el)== str else False for el in attr]):
                setattr(cls, attr[0], (cls.__name__,attr[0])) 
            else:
                break
          
#print(CAT.AMP.HEAD_CONE)


#NICE BUT I DON T WANT TO SET THE AT RUNTIME! I WANT AUTOCOMPLETION   
def comment1():
    '''
    class Category:
    def __init__(self,kv_list) -> None:
        for k,v in kv_list:
            setattr(self,k,v) 

    categories_schema = {
        'GUITAR':{
            'SOLID':1,
            'SEMI_HOLLOW':2,
            'ACOUSTIC':3,
            'CLASSIC':4
        },
        'BASS':{
            'SOLID':1,
            'SEMI_HOLLOW':2,
            'ACOUSTIC':3
        },
        'AMP':{
        'HEAD_CONE':1,
        'COMBO':2
        }
    }


    categories_schema=make_dotdict(categories_schema)
    '''


   


