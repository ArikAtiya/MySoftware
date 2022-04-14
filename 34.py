from datetime import datetime
import requests
print(datetime.now())

response = requests.get("https://api.github.com/users/avielb/repos")
#response_walla = requests.get("http://www.walla.co.il")


def check_url_online(url):
    if requests.get(url).status_code == 200:
        print("url " + url + "is up")
    else:
        print(requests.get(url).status_code)


check_url_online("http://www.walla.co.il")
#print(response.json())
#print(response.json()["login"])
#print(response.text)
#print(type(response))
if response.status_code == 200:
    print("github is up and running")


for repo in response.json():
    print(repo["full_name"])
