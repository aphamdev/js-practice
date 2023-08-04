# Please complete the following function that accepts two parameters: a JSON-formatted string representing a
# dictionary, and a value. The function should return the key for a matching value
#  if it exists in the dictionary represented by the JSON, and None otherwise.


# JSON-formatted string	Property value	Output
# {}                  	"Noor"	        None
# '{"age": 23}'       	"Noor"	        None
# '{"name": "Noor"}'    'Noor"      	"name"


import json

def key_for_value(json_string, property_value):
    d = json.loads(json_string)
    for k, v in d.items():
        if v == property_value:
            return k
