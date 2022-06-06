import requests
import json

var_dict1 = dict(Age=19, Name='Nick')
print(var_dict1)

var_dict2 = {"Age": 19, "Name": 'Nick'}
print(var_dict2)

var_dict3 = {}  # создание словаря
var_dict3["Age"] = 19
var_dict3["Name"] = 'Nick'
print(var_dict3)

var_dict4 = {
    "firstName": "Bennet",
    "lastName": "Valentine",
    "address": {
        "streetAddress": "Grove Street 2/3",
        "city": "LA",
        "postalCode": 505505
    },
    "phoneNumbers": [
        "555 400-34-31",
        "555 384-35-34"
    ]
}
print(type(var_dict4))

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    print("Well!")
else:
    print ("False")
json_data = response.content.decode()
airlines = json.loads(json_data)
print(type(airlines))
print(json_data)

with open('data.json', 'w') as file:
    json.dump(json_data, file)
    json.dumps()

with open('src/dist/new_file.json', 'r') as file:
    json_data1 = json.loads(file.read())
    print(json_data1)
    json.load()
    json.loads()