import color_palette
import twitter

class ShowTimeline:
    def __init__(self):
        self.colors = color_palette.colors()
        pass

    def show_homeTimeline(self, api):
        statuse = api.GetHomeTimeline(count=15)

        for s in statuse:
            time = s.created_at.split()
            print(self.colors.random_color()+ "{0:}(@{1:}) at {2:}/{3:}/{4:} {5:}".format(
                s.user.name,s.user.screen_name, time[5], time[1], time[2], time[3])
                +self.colors.END, end="")
            print(" id:{:}".format(s.id))
            print("""{:}""".format(s.text)
            )   