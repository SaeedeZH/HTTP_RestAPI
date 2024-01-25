import requests

def get_data():
      # set api_endpoint
    url = "http://127.0.0.1:5000/tasks/1"

    # Set the response format to headers
    headers = {'Accept': 'application/json'}

    # Set the query as a pyload for API
    # payload = {'query': query}

    # Send a RESTful request to the api_endpoint address, query and the output format we expect
    # response = requests.get(url=url, params=payload, headers=headers)
    #param = "1"
    try:
      response = requests.get(url)
      response.raise_for_status()
      print(response.json())
    except requests.exceptions.HTTPError as err:
      print(f"this is {err}")

def post_data():
   new_data = { 'title': 'Task 4' }
   url = "http://127.0.0.1:5000/tasks"
   post_respone = requests.post(url, json=new_data)
   print(f"The satats of Post function {post_respone.status_code}")
   print(post_respone.json())



get_data()
post_data()