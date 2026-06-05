class Game:
    """比赛信息"""

    def __init__(self, category: str, title: str, status: str, link: str):
        self.category = category
        self.title = title
        self.status = status
        self.link = link

    def __str__(self) -> str:
        return " ".join((self.category, self.title, self.link, self.status))


# class GameIssuePageURL:
