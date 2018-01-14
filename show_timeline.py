import color_palette
import twitter

class ShowTimeline:
    def __init__(self):
        self.colors = color_palette.colors()
        pass

    def show_home(self, api):
        statuse = api.GetHomeTimeline(count=15)

        for s in statuse:
            time = s.created_at.split()
            print(self.colors.random_color()+ "{0:}(@{1:}) at {2:}/{3:}/{4:} {5:}".format(
                s.user.name,s.user.screen_name, time[5], time[1], time[2], time[3]
                ) +self.colors.END, end="")
            print(" id:{:}".format(s.id))
            print("""{:}""".format(s.text)
            )  

    def show_mylists(self, api):
         list = api.GetListsList()
         for l in list:
             print(self.colors.random_color()+ "{0:} @{1:}".format(
                 l.name, l.user.screen_name
                 ) +self.colors.END, end="")
             print(" id:{:}".format(l.id))

    def show_timeline(self, api):
        id = input("表示したいリストのIDを入力してください： ").strip()
        try:
            statuse = api.GetListTimeline(id, count=15)
        except:
            print("リストの取得に失敗しました")

        for s in statuse:
            time = s.created_at.split()
            print(self.colors.random_color()+ "{0:}(@{1:}) at {2:}/{3:}/{4:} {5:}".format(
                s.user.name,s.user.screen_name, time[5], time[1], time[2], time[3]
                ) +self.colors.END, end="")
            print(" id:{:}".format(s.id))
            print("""{:}""".format(s.text)
            ) 