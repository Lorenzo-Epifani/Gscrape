# Description
This is a template to simplify cli coding in python.<br>
Inside ```controller.py```, you can use the decorator: 
<br>

```python
@set_config('example')
    def function1(context):
        ...
```
In this way, running: 

```bash
python main.py example
```
you will execute ```function1(context)```.

```context``` will be a ```dict``` having these keys-values pairs:

| key   |      value      |  source |
|----------|:-------------|:------|
| ```_LOC``` |local config files | ```config/example__c/values.json``` |
| ```_GLB``` |global config files   |   ```config/global.json``` |
| ```_CLA``` |command line arguments |     |

In this way, you just have to create: 
```
config/command__c/values.json
``` 
In order to make usable the ```@set_config('command')``` decorator. \
Only folders ending with ```__c``` are bound to the corresponding decorator (without the ending ```'__c'```). \
You also have to create the ```config/command__c/validator.py``` file. \
This file expose and validate the parent ```values.json```. \
You can just copy paste the ```config/default__c``` folder for fast prototyping. This folder represent the minimum working example.


# TODO
ADD CLA OVERRIDE
ADD DEBBUGGER GENERATOR FUNCTION