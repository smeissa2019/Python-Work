#%%
class MyClass:
    """A simple example class"""
    i = 12345
    def __init__(self, name):
        self.name = name
    def f(self):
        return 'hello world from ' + self.name

#%%
aClass = MyClass("John")
print(aClass.f())
bClass = MyClass("Lucy")
print(bClass.f())

#%%
import json
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
#%% 
with open('out.json','w') as fh:
    json.dump(data, fh)

#%%
# Importing data from a json file:
with open('out.json', 'r') as nfh:
    obj = json.load(nfh)
    print(obj)
    print(obj["president"]["name"])

#%%
import re
txt = "The rain in Spain"
x = re.search ("^The.*Spain$", txt)
print (x)
#%%
import re
zipcode1 = "315"
print(re.search("\d{5}",zipcode1))

#%%
import re
zipcode1 = "31545-8765"
print(re.search("\d{5",zipcode1))

#https://www.debuggex.com/cheatsheet/regex/pcre
