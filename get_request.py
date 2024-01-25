import requests

## All HTTP methods:
## requests.get(URL, parameter={key: value}, arguments) = request.get(url, params/Headers)
## requests.post(URL, data=[data], json=[json], arguments) = request.post(url, data, params)
## requests.put(URL, data=[data], arguments)
## requests.delete(URL, arguments)
## requests.head(URL, arguments)
## requests.patch(URL, arguments)

# making a GET request

# example 1
# res = requests.get('https://www.google.com/search?q=hello')
# res1 = requests.get('https://api.github.com/users/naveenkrnl')
# print(res1)
# print(res1.content)

# JSONPlaceholder is a freely available fake API used for testing and prototyping. 
# example 2

# The API endpoint 
url = "https://jsonplaceholder.typicode.com/posts/1"
# Get request to the API
response = requests.get(url)
# print the response
response_json = response.json()
print(response.status_code)
print(response_json)
print(f" \n The header is: {response.headers}")
print("*****************************")
# example 3. pass parameters to GET

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts"
# Adding a payload/ parameters
params = {"id":[1,2,3], "userId":1}
# Get request to the API
response = requests.get(url, params)    
# print the response
print("\n",response.status_code)
response_json = response.json()
for i in response_json:
    print("\n", i)
print("*****************************")

# The JSONPlaceholder API does not require any authentication for you to start interacting with it. 
# But, there are several instances where a REST API may require authentication before access is granted to specific endpoints

# example 4
from requests.auth import HTTPBasicAuth
private_url = "https://api.github.com/user"
github_username = "username"
token = "token"

private_url_response = requests.get(url = private_url,  auth= HTTPBasicAuth(github_username,token))
print(private_url_response.status_code)
print("*****************************")

# example 5
# manage the reported errors
url =  "https://jsonplaceholder.typicode.com/postz"  # a deliberate typo
# attepmt to Get data from provided endpoint
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(error)
print("*****************************")

# example 6

# r = requests.get('https://reqbin.com/echo/get/json', 
#                  headers={'Accept': 'application/json'})

# print(f"Status Code: {r.status_code}, Content: {r.json()}")

# example 7
#response_API = requests.get('https://api.covid19india.org/state_district_wis')
#print("$$$", response_API.json())
#count = 0
# if response_API.status_code == 200:
#     for i in response_API.json().items():
#         print(f"item{count}= {i} \n")
#         count = count+1
# else:
#     print(f"Error in pulling data with response code: {response_API.status_code}")

### or 

try:
    url = "https://jsonplaceholder.typicode.com/postsh"
    response = requests.get( url) #  https://api.covid19india.org/state_district_wis')
    response.raise_for_status()
    count = 0
    for i in response.json():
        print(f"item{count}= {i} \n")
        count = count+1
except requests.exceptions.HTTPError as err:
    print(f"Error in pulling data, {err}")

#### example 8

### get request with parametere as user info + error managment + private Url(authentication)
from requests.auth import HTTPBasicAuth
# The endpoint
url = "https://jsonplaceholder.typicode.com/posts"
username = ""
password = ""
param = {"id": [1,2,3,4,5] ,"userId":1}
try:
    # get request
    res_api = requests.get(url, params= param, auth= HTTPBasicAuth(username, password))
    res_api.raise_for_status()
    json_data = res_api.json()
    for item in json_data:
        print(f"\n item: {item}")
except requests.exceptions.HTTPError as err:
    print(f"There is an error: {err}")

