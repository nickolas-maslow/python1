import json
import requests

url = "https://api.instantwebtools.net/v1/airlines/-10"
response = requests.get(url)

print(response.status_code)
json_data = response.content.decode()
print(json_data)

url = "https://jsonplaceholder.typicode.com/posts"
url = "https://api.instantwebtools.net/v1/airlines"
response = requests.get(url)
content = response.content
print(type(content))
json_data = content.decode()
print(type(json_data))
print(json_data)


airlines = json.loads(json_data)
print(type(airlines))
print(airlines[1:1:2])
print(type(json.load(json_data)))

for airline in airlines[1:1:2]:
    print(airline)
    with open(f'temp/data_{airline["id"]}.json', 'w') as file:
         json.dump(airline, file)
    with open('temp/data_%s.json' % airline["id"], 'w') as file:
        json.dump(airline, file)
        json.dumps(airline)

file_name = 'temp/data_4.json'

with open('data.json', 'w') as file:
    json.dump(json_data, file)
    json.dumps()

with open(file_name, 'r') as file:
    json_new_data = json.load(file)

    print(json_new_data)
    print(type(json_new_data))
    json_data1 = json.loads(file.read())
    print(json_data1)
    json.load()
    json.loads()