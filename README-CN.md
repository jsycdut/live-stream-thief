# live-stream-thief
[streameast](https://streameaste.cc/)是一个可以观看众多赛事的直播网站，包括NBA、NFL、F1等赛事，你只要打开过这个网站就会发现，它的广告太多了，几乎你任何一次点击，都必须承受新的广告页的折磨，当然作为一个免费的网站我是理解这样的做法的，但是我的脑子实在是被这无休止的广告给折磨得够呛。

live-stream-thief只是简单的把播放链接从网页中剥离出来，直接去到单纯的播放页，少受一点广告的折磨（并非一条广告都没有，但是比起streameast而言我只能说是几乎没有了）

# 用法
你需要[uv](https://docs.astral.sh/uv/)来运行这个项目。
```bash
➜  live-stream-thief git:(main) ✗ # 可以指定过滤你想要的比赛类别，比如nba wnba f1 nfl....
➜  live-stream-thief git:(main) ✗ uv run main.py wnba
WNBA Indiana Fever vs Atlanta Dream LIVE
source1 ==> https://embedsports.top/embed/admin/ppv-atlanta-dream-vs-indiana-fever/1
source2 ==> https://embedsports.top/embed/golf/22864/1
source3 ==> https://embedsports.top/embed/delta/live_wnba_fever-atlanta-live-streaming-1210764024/1
------------
WNBA Minnesota Lynx vs Golden State Valkyries LIVE
source1 ==> https://embedsports.top/embed/admin/ppv-golden-state-valkyries-vs-minnesota-lynx/1
source2 ==> https://embedsports.top/embed/golf/22865/1
source3 ==> https://embedsports.top/embed/delta/live_wnba_lynx-valkyries-live-streaming-1210765023/1
------------
➜  live-stream-thief git:(main) ✗ # 或者直接获取所有比赛
➜  live-stream-thief git:(main) ✗ uv run main.py
CFL Hamilton Tiger-Cats vs Montreal Alouettes LIVE
------------
International Friendly Match Czech Republic vs Guatemala LIVE
source1 ==> https://embedsports.top/embed/admin/ppv-czechia-vs-guatemala/1
source2 ==> https://embedsports.top/embed/golf/22903/1
source3 ==> https://embedsports.top/embed/delta/live_int-friendly-games_czechia-guatemala-live-streaming-1337528133/1
source4 ==> https://embedsports.top/embed/echo/czech-republic-vs-guatemala-football-1542893/1
------------
International Friendly Match Mexico vs Serbia --
source1 ==> https://embedsports.top/embed/admin/ppv-mexico-vs-serbia/1
source2 ==> https://embedsports.top/embed/golf/22904/1
source3 ==> https://embedsports.top/embed/delta/live_int-friendly-games_mexico-serbia-live-streaming-1337529132/1
source4 ==> https://embedsports.top/embed/echo/mexico-vs-serbia-football-1528284/1
------------
MLB Atlanta Braves vs Toronto Blue Jays LIVE
source1 ==> https://embedsports.top/embed/admin/ppv-toronto-blue-jays-vs-atlanta-braves/1
source2 ==> https://embedsports.top/embed/golf/22871/1
source3 ==> https://embedsports.top/embed/delta/live_mlb_braves-blue-jays-live-streaming-1309431258/1
source4 ==> https://embedsports.top/embed/echo/atlanta-braves-vs-toronto-blue-jays-baseball-178948/1
------------
MLB Minnesota Twins vs Kansas City Royals LIVE
source1 ==> https://embedsports.top/embed/admin/ppv-kansas-city-royals-vs-minnesota-twins/1
source2 ==> https://embedsports.top/embed/golf/22872/1
source3 ==> https://embedsports.top/embed/delta/live_mlb_twins-royals-live-streaming-1309432257/1
source4 ==> https://embedsports.top/embed/echo/minnesota-twins-vs-kansas-city-royals-baseball-178944/1
------------
MLB Chicago Cubs vs Athletics LIVE
```