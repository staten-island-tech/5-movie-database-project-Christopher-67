import json

movies = open("./movies.json", encoding="utf8")

data = json.load(movies)

print("title of movies")
for index, item in enumerate(movies):
    print(index, ":",item["title"])
