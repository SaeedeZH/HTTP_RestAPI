import requests


whole_data = []
for i in range(20):
    url = f"https://jsonmock.hackerrank.com/api/tvseries?page={i+1}"
    response = requests.get(url)
    #print(f"page {i+1}= {response.json()} \n ")
    data = response.json()["data"]
    whole_data.append(data)

movies = []
for list_i in whole_data:
    for sery in list_i:
        movies.append([sery["name"], sery["genre"],sery["imdb_rating"] ])

#for item in movies:
    #print("\n", item) 

def bestInGenre(genre):
    genre_movies = []
    for movie in movies:
        if movie[1].find(genre) != -1:
        #if movie[1] == genre:
            genre_movies.append((movie[0], movie[2]))
    return genre_movies

same_genre = bestInGenre("Animation")
same_genre.sort(key= lambda item: (-item[1], item[0]) )#, reverse=True)
print("\n", same_genre[0], same_genre[0:4])



