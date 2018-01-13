import color_palette
import twitter

class ShowTimeline:
    def __init__(self):
        colors = color_palette.colors()
        pass


def show_HomeTimeline(self, api):
    statuse = api.GetHomeTimeline(count=8)
    # countに指定した個数のタイムラインを取得することができます。
    # 取得できる最大値は200です。

    for s in statuse:
        time = s.created_at.split()
        print(colors.random_color()+ "{0:}(@{1:}) at {2:}/{3:}/{4:} {5:}:".format(
            s.user.name,s.user.screen_name, time[5], time[1], time[2], time[3])
            +colors.END)
        print("""    {:}""".format(s.text)
        )