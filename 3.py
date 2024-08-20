import requests

response = requests.get("https://sv443.net/jokeapi/v2")
print(response.text)

#res_str = response.text
#print(type(res_str))

#res_dict = response.json()
#print(type(res_dict))