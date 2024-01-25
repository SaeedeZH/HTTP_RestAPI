import requests

# to make a DELETE request
res = requests.delete('https://httpbin.org/delete', data= {'key':'value'})
print(res)
print(res.json())