import requests

url = "https://jsonplaceholder.typicode.com/todos/10"
res = requests.get(url)
print(res.json())

update_item = {
        "userId": 1, 
        "id" : 10,
        "title" : "this is new",
        "completed": False
}

res = requests.put(url, update_item)
print(res.status_code)
print(res.json())

# PATCH
# requests.patch(): modify the value of a specific field on an existing data.
# PATCH differs from PUT in that it doesn’t completely replace the existing resource.
# It only modifies the values set in the JSON sent with the request.

update_item = {
        "title" : "upadte!",
}

res = requests.patch(url, update_item)
print(res.status_code)
print(res.json())