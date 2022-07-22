import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url=url)
data = response.json()
