import requests
import base64
from bs4 import BeautifulSoup
from game_meta_info import Game

GAME_RELEASE_PAGE = "https://streameaste.cc/"


def soup_for_url(url: str) -> BeautifulSoup:
    """获取BeautifulSoup，用于抓取页面信息"""
    response = requests.get(url)
    response.encoding = "utf8"
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    return soup


def parse_game_list() -> list[Game]:
    """从streameast主站，获取到当日比赛列表信息"""
    soup = soup_for_url(GAME_RELEASE_PAGE)
    match_list = soup.find("div", class_="match-list")
    if match_list is None:
        raise ValueError(
            f'比赛发布页{GAME_RELEASE_PAGE}中没有<div class="match-list"属性'
        )
    matches = match_list.find_all("a")
    if match_list is None:
        raise ValueError("比赛列表中没有可供跳转的a标签")
    games = []
    for match in matches:
        link = match.get("href")
        cat_tag = match.find("span", class_="match-cat")
        match_title_tag = match.find("span", class_="match-title-text")
        status_tag = match.find("span", class_="badge")
        if cat_tag and link and match_title_tag and status_tag:
            game = Game(
                cat_tag.text,
                match_title_tag.text,
                status_tag.text,
                # link是域名之后的路径，要拼接一下域名才能工作
                GAME_RELEASE_PAGE + str(link),
            )
            games.append(game)
    return games


def parse_livestream_sources(game_play_url: str) -> list[str]:
    """从比赛播放页中，提取出直播源列表url信息，一场比赛一般有好几个可替换直播源"""
    soup = soup_for_url(game_play_url)
    sources_grid = soup.find("div", class_="sources-grid")
    if sources_grid is None:
        # html中解析不到播放源列表信息
        return []
    sources = sources_grid.find_all("button", class_="source-btn")
    result: list[str] = []
    for source in sources:
        # 播放源url在原始html中是一个base64编码后的字符串，需要解析下
        source_tag = source.get("data-s")
        readable_url = base64.b64decode(str(source_tag)).decode("utf-8")
        result.append(readable_url)
    return result
