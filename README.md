# live-stream-thief
- [中文用户请看这里](./README-CN.md)

[StreamEast](https://streameaste.cc/) is great，it provides NBA, MLB，F1 and so many other games with high quality livestream watch experience, but too many ads in it!!! Every time I click the live stream page, like fullscreen, volumes up and down, it bumps to a new ads page before it really works, which really really drives me mad.

this project is simple, it extracts the pure working livestream url from the ads-surronded original web page.
All you need to do is: run the code, get the url and open it in your browser, enjoy it!

NOTICE: the parsed urls may contain ads too, but it seems only appears once when you click the play button first time.

## usage
make sure you know what [uv](https://docs.astral.sh/uv/) is, run the code as below.
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
