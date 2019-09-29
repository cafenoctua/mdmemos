import requests

payload = {'key1': 'value1', 'key2': 'value2'}

# GET
r = requests.get('http://httpbin.org/get', params=payload)

print(r.status_code)
print(r.text)
print(r.json())

# POST
r = requests.post('http://httpbin.org/post', params=payload)

print(r.status_code)
print(r.text)
print(r.json())

# PUT
r = requests.put('http://httpbin.org/put', params=payload)

print(r.status_code)
print(r.text)
print(r.json())

# DELETE
r = requests.delete('http://httpbin.org/delete', params=payload)

print(r.status_code)
print(r.text)
print(r.json())

# POST タイムアウト処理
# POST
r = requests.post('http://httpbin.org/post', params=payload, timeout=1)

print(r.status_code)
print(r.text)
print(r.json())