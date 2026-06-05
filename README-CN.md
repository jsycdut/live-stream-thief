# live-stream-thief
[streameast](https://streameaste.cc/)是一个可以观看众多赛事的直播网站，包括NBA、NFL、F1等赛事，你只要打开过这个网站就会发现，它的广告太多了，几乎你任何一次点击，都必须承受新的广告页的折磨，当然作为一个免费的网站我是理解这样的做法的，但是我的脑子实在是被这无休止的广告给折磨得够呛。

live-stream-thief只是简单的把播放链接从网页中剥离出来，直接去到单纯的播放页，少受一点广告的折磨（并非一条广告都没有，但是比起streameast而言我只能说是几乎没有了）

# 用法
你需要[uv](https://docs.astral.sh/uv/)来运行这个项目。
```bash
➜  live-stream-thief git:(main) ✗ uv run main.py
Atlanta Braves vs Toronto Blue Jays LIVE
source1 ==> https://embedsports.top/embed/admin/ppv-toronto-blue-jays-vs-atlanta-braves/1
source2 ==> https://embedsports.top/embed/golf/22871/1
source3 ==> https://embedsports.top/embed/delta/live_mlb_braves-blue-jays-live-streaming-1309431258/1
source4 ==> https://embedsports.top/embed/echo/atlanta-braves-vs-toronto-blue-jays-baseball-178948/1
------------
Minnesota Twins vs Kansas City Royals --
source1 ==> https://embedsports.top/embed/admin/ppv-kansas-city-royals-vs-minnesota-twins/1
source2 ==> https://embedsports.top/embed/golf/22872/1
source3 ==> https://embedsports.top/embed/delta/live_mlb_twins-royals-live-streaming-1309432257/1
------------
Chicago Cubs vs Athletics --
source1 ==> https://embedsports.top/embed/admin/ppv-athletics-vs-chicago-cubs/1
source2 ==> https://embedsports.top/embed/golf/22873/1
------------
Houston Astros vs Pittsburgh Pirates --
source1 ==> https://embedsports.top/embed/admin/ppv-pittsburgh-pirates-vs-houston-astros/1
source2 ==> https://embedsports.top/embed/golf/22874/1
source3 ==> https://embedsports.top/embed/delta/live_mlb_astros-pirates-live-streaming-1309434255/1
source4 ==> https://embedsports.top/embed/echo/houston-astros-vs-pittsburgh-pirates-baseball-178945/1
------------
Arizona Diamondbacks vs Los Angeles Dodgers --
source1 ==> https://embedsports.top/embed/admin/ppv-los-angeles-dodgers-vs-arizona-diamondbacks/1
source2 ==> https://embedsports.top/embed/golf/22875/1
source3 ==> https://embedsports.top/embed/echo/arizona-diamondbacks-vs-los-angeles-dodgers-baseball-178949/1
------------
```