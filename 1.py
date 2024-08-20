import requests

response = requests.get("https://api.genderize.io?name=hope")
print(response.text)

#res_str = response.text
#print(type(res_str))

res_dict = response.json()
print(res_dict)