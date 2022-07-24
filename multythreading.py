import requests
import json
import threading
import multiprocessing
import aiohttp


def download_json(name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url='https://jsonplaceholder.typicode.com/todos/1')
    response_json = response.json()

    with open(f'json_files/response{name}.json', 'w') as file:
        json.dump(response_json, file)


for i in range(1, 10):  # последовательная загрузка
    download_json(i)

###########################################################################################################

thread_list = [threading.Thread(target=download_json, args=(f"thread_{x}",), kwargs={}) for x in range(1, 10)]
for i in thread_list:
    i.start()
                                #  многопоточная загрузка
for i in thread_list:
    i.join()

##############################################################################################################

process_list = [multiprocessing.Process(target=download_json, args=(f"process_{x}",), kwargs={}) for x in range(1, 10)]

for i in process_list:
    i.start()
                                    #  мультипроцессовая загрузка
for i in process_list:
    i.join()

######################################################################################################################


async def async_download_json(name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://jsonplaceholder.typicode.com/todos/1", headers=headers) as await_response:
            data = await await_response.json()

    with open(f'json_files/response{name}.json', 'w') as file:
        json.dump(data, file)

# асинхронная загрузка


