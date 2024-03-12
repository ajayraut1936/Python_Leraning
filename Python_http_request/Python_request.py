
import    requests

url = "https://reqres.in"
header=   "{Content-Type=application/json" 

response=requests.get(url,header)
print(response.content)
print(response.status_code)
print(response.headers)
print(response)