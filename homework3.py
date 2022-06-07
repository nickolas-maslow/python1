import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
zapros = requests.get(url)
otvet_decod = zapros.content.decode()
otvet_dict = json.loads(otvet_decod)

for i in otvet_dict:
    with open(f"homework_/get_one{i['id']}.json", "w") as file:
        json.dump(i, file)

