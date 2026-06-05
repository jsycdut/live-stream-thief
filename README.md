# live-stream-thief
- [中文用户请看这里](./README-CN.md)

[StreamEast](https://streameaste.cc/) is great，it provides NBA, MLB，F1 and so many other games with high quality livestream watch experience, but too many ads in it!!! Every time I click the live stream page, like fullscreen, volumes up and down, it bumps to a new ads page before it really works, which really really drives me mad.

this project is simple, it extracts the pure working livestream url from the ads-surronded original web page.
All you need to do is: run the code, get the url and open it in your browser, enjoy it!

NOTICE: the parsed urls may contain ads too, but it seems only appears once when you click the play button first time.

## usage
make sure you know what [uv](https://docs.astral.sh/uv/) is, run the code as below.
```bash
➜  live-stream-thief git:(main) ✗ # you can filter the game category you want, like nba, wnba, nfl, f1.....
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
➜  live-stream-thief git:(main) ✗ # or get all games
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
