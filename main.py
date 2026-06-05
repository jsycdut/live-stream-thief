import nba
import sys
from game import Game

DEFAULT_GAME_CATEGORY = "NBA"

if __name__ == "__main__":
    game_category = "NBA"
    games: list[Game] = []
    if game_category == "NBA":
        games = nba.fetch_nba_game_info()
    for game in games:
        urls = nba.parse_livestream_sources(game.link)
        print(f"{game.title} {game.status}")
        for idx, url in enumerate(urls):
            print(f"source{idx+1} ==> {url}")
        print("------------")
