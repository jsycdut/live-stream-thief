import requests
from bs4 import BeautifulSoup
from game import Game
import base64

NBA_GAME_RELEASE_PAGE = "https://streameasti.ch/mlb"
NBA = "NBA"


def fetch_nba_game_info() -> list[Game]:
    response = requests.get(NBA_GAME_RELEASE_PAGE)
    response.encoding = "utf8"
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    match_list = soup.find("div", class_="match-list")
    if match_list is None:
        raise ValueError("解析NBA比赛列表标签错误，没有match-list属性")
    matches = match_list.find_all("a")
    if match_list is None:
        raise ValueError("比赛列表中没有可供跳转的a标签")
    games = []
    for match in matches:
        link = match.get("href")
        name_tag = match.find("span", class_="match-title-text")
        status_tag = match.find("span", class_="badge")
        if link and name_tag and status_tag:
            game = Game(NBA, name_tag.text, status_tag.text, str(link))
            games.append(game)
    return games


def parse_livestream_sources(game_page_url: str) -> list[str]:
    response = requests.get(game_page_url)
    response.encoding = "utf8"
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    sources_grid = soup.find("div", class_="sources-grid")
    if sources_grid is None:
        return []
    # if sources_grid is None:
    #    raise ValueError("页面无sources-grid标签，装载直播流来源的页面结构可能已变化")
    sources = sources_grid.find_all("button", class_="source-btn")
    result: list[str] = []
    for source in sources:
        source_tag = source.get("data-s")
        blank_url = base64.b64decode(str(source_tag)).decode("utf-8")
        result.append(blank_url)
    return result
