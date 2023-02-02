import requests

url = "http://127.0.0.1:8000/api/todo/"

payload = {}
headers = {}

# response = requests.request("POST", url, headers={}, data={"title": 'Задача кодом 1'})
response = requests.request("DELETE", url, headers={}, data={'id': 1})

print(response.json())


