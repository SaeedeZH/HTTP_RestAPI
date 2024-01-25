import requests
# making a POST request
## request.post(url, data, params)

# example 1
# res = requests.post('https://httpbin.org/post', data= {'key':'value'})
# print(res)
# print(res.json())

# JSONPlaceholder is a freely available fake API used for testing and prototyping.
# example 2

# Define new data to create
new_data = {
    "userID" : 1,
    "id" : 1,
    "title" : "making a post request",
    "body": "this is the data we created"
}
# The API endpoint to communicate with
url = "https://jsonplaceholder.typicode.com/posts"
# A POST request to the API
post_response = requests.post(url, json = new_data)  # send a JSON Object to the URL
# print the response
print(post_response.status_code)
post_response_json = post_response.json()

# example 3
url = "https://jsonplaceholder.typicode.com/todos"
url1 = "https://jsonplaceholder.typicode.com/todos/1"
res = requests.get(url1)
print(type(res.json()))
keys = res.json().keys()
print(keys)

new_item = {
        "userId" : 10,
        "id" : 500,
        "title" : "this is new one",
        "completed" : True
}
headers = {"content-type": "application/json"}
res = requests.post(url, new_item, headers)
print(res.status_code)
print(res.json())

import string
str = "abcdef"
print(str.find("de"))
res = requests.get(url)
title_list = [item["title"] for item in res.json() if (item["title"].find("new") != -1)]
print(title_list)
