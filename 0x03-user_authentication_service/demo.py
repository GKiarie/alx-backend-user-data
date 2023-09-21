import requests

payload = {'key1': 'value1', 'key2': 'value2'}

res = requests.get('https://httpbin.org/get', params=payload)

print(res.content)
