import requests

BASE = "http://127.0.0.1:5000/"
data = [{"likes": 90, "name": "Jackass", "views": 100},
        {"likes": 100, "name": "How to make REST API", "views": 8000000},
        {"likes": 1, "name": "Odyn", "views": 740000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())
