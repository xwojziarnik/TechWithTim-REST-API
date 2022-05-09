import requests

BASE = "http://127.0.0.1:5000/"

# update
response = requests.patch(BASE + "video/2", {"views": 99, "likes": 21})
print(response.json())

input()

# add new one
response = requests.put(BASE + "video/21", {"name": "Wojtek - junior Python dev", "views": 0, "likes": 0})
print(response.json())

input()

# update last video
response = requests.patch(BASE + "video/21", { "views": 100, "likes": 47})
print(response.json())
