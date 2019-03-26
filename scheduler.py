import requests

url = "https://leetcode.com/api/problems/algorithms/"
r = requests.get(url=url)

print(r.json()) #displays the json given by the url
