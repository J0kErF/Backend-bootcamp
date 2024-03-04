import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

# Define URL to scrape
url = "https://store.steampowered.com/"


# Function to extract game data
def get_games_data(url):
    steam_page = requests.get(url)
    parsed = BeautifulSoup(steam_page.content, "html.parser")
    games = parsed.find_all("div", id="tab_newreleases_content")
    games_dict = {}
    for game in games:
        game_names=[]
        game_genres=[]

        game_name = game.find_all("div", class_="tab_item_name")
        game_genre = game.find_all("div", class_="tab_item_top_tags")

        for name in game_name:
            game_names.append(name.text)
        for genre in game_genre:
            game_genres.append(genre.text)

        games_dict = dict(zip(game_names, game_genres))
    return games_dict

def plot_game_data(games):
    genres = {}
    for game in games:
        for genre in games[game].split(", "):
            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1
    plt.bar(genres.keys(), genres.values())
    plt.savefig("plot.png")
def genre_percentage():
    all_genres={}
    for game in games:
        for genre in games[game].split(", "):
            if genre not in all_genres:
                all_genres[genre]=0
            all_genres[genre]+=1
    genres_sum=sum(all_genres.values())
    for i,genre in enumerate(all_genres):
        print(i,genre)
    print("")
    genre_index=(input("Enter the name of the genre you want to know the percentage of"))

    return (all_genres[genre_index]/genres_sum)*100
        
            
    
games=get_games_data(url)

plot_game_data(games)
print(genre_percentage())

