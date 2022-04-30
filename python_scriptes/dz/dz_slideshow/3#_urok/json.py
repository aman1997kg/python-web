import json


data = {
    'key' : 'value'
       }


with open("file_json.json", "w") as f:
    json.dump(data, f)

#with open("file_json.json", "r") as f:
 #   print(json.load(f))
