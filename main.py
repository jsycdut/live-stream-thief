import sys
import game_parser
from game_meta_info import Game
from rich.console import Console

DEFAULT_GAME_CATEGORY = "NBA"

if __name__ == "__main__":
    # 解析今日比赛列表
    games: list[Game] = game_parser.parse_game_list()
    console = Console()
    if len(games) == 0:
        console.print(
            f"在{game_parser.GAME_RELEASE_PAGE}中没有解析到比赛信息，今日大概率无比赛，打开网页核实下"
        )
        exit(0)

    # 根据比赛类型排序，避免在无比赛类别过滤条件下输出的比赛列表混乱
    games.sort(key=lambda x: x.category)

    target_game_catetory: str | None = sys.argv[1] if len(sys.argv) >= 2 else None
    for game in games:
        # 过滤目标比赛类型
        if (
            target_game_catetory
            and target_game_catetory.lower() != game.category.lower()
        ):
            continue

        # 解析播放URL
        urls = game_parser.parse_livestream_sources(game.link)
        console.print(
            f"[bold yellow]{game.category}[/bold yellow] [bold cyan]{game.title}[/bold cyan] {game.status}"
        )
        for idx, url in enumerate(urls):
            console.print(f"[bold green]source{idx+1}[/bold green] ==> {url}")
        print("------------")
