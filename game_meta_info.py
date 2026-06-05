class Game:
    """比赛信息"""

    def __init__(self, category: str, title: str, status: str, link: str):
        # 比赛类别，NBA/NFL/F1/WNBA/...
        self.category = category
        # 比赛名称
        self.title = title
        # 比赛状态
        self.status = status
        # 比赛播放页链接
        self.link = link

    def __str__(self) -> str:
        return " ".join((self.category, self.title, self.link, self.status))
