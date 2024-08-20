import requests

response = requests.get("http://api.open-notify.org/iss-now")
print(response.text)

res_str = response.text
print(type(res_str))

res_dict = response.json()
x=res_dict['iss_position']
a=x['longitude']
b=x['latitude']
print('longitude =',a)
print('latitude =',b)

