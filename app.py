import json

movies = open("./movies.json", encoding="utf8")

data = json.load(movies)

print("title of movies")
for index, item in enumerate(json):
    print(index, ":",item["title"])

Searching = True

Movies_after2020 = input("show movies after 2020?: ").lower()
if Movies_after2020 != "yes":
    Searching = False