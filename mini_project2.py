import requests

def pull_data(url_api):
    '''
    Download TV show Data form endpoint

    '''
    url = url_api
    page_number = 1
    series = []
    while True:
        response = requests.get(f"https://jsonmock.hackerrank.com/api/tvseries?page={page_number}")
        if response.status_code == 200:
            if response.json()["data"] == []:
                break
            series.append(response.json()["data"])
        else:
            print(f"Error no: {response.status_code}" )
            break
        page_number = page_number + 1
    #print(series)
    series_list = [(item["name"], item["genre"], item["imdb_rating"]) for show_list in series for item in show_list]
    return series_list

def bestInGenre(series, genre):
    
    series_of_genre = [(item[0], item[2])  for item in series if item[1].find(genre)!= -1]
    series_of_genre.sort(key= lambda item : (-item[1], item[0]))
    print(series_of_genre[0], series_of_genre[0:4])

if __name__ == "__main__":
    url = "https://jsonmock.hackerrank.com/api/tvseries?page"
    series = pull_data(url)
    #print(series)
    while(True):
        genre = input("Enter the type of genre (press no for Exit): ")
        if genre == "Exit":
            break
        bestInGenre(series, genre)

