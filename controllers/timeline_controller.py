import materials
import twitter

class TimelineController:
    def __init__(self):
        self.colors = materials.color_palette.colors()
        pass

    def show_home(self, api):
        try:
            statuses = api.GetHomeTimeline(count=15)
        except:
            print("タイムラインの取得に失敗しました")

        print("-"*80)
        for s in statuses:
            time = s.created_at.split()
            print(self.colors.random_color()+ "{0:}(@{1:}) at {2:}/{3:}/{4:} {5:}".format(
                s.user.name,s.user.screen_name, time[5], time[1], time[2], time[3]
                ) +self.colors.END, end="")
            print(" id:{:}".format(s.id))
            print("""{:}""".format(s.text)
            ) 
        print("-"*80) 

    def show_mylists(self, api):
        try:
            list = api.GetListsList()
        except:
            print("リストの取得に失敗しました")

        for l in list:
             print(self.colors.random_color()+ "{0:} @{1:}".format(
                 l.name, l.user.screen_name
                 ) +self.colors.END, end="")
             print(" id:{:}".format(l.id))

    def show_timeline(self, api):
        id = input("表示したいリストのIDを入力してください： ").strip()
        try:
            statuses = api.GetListTimeline(id, count=15)
        except:
            print("リストの取得に失敗しました")

        print("-"*80)
        for s in statuses:
            time = s.created_at.split()
            print(self.colors.random_color()+ "{0:}(@{1:}) at {2:}/{3:}/{4:} {5:}".format(
                s.user.name,s.user.screen_name, time[5], time[1], time[2], time[3]
                ) +self.colors.END, end="")
            print(" id:{:}".format(s.id))
            print("""{:}""".format(s.text)
            ) 
        print("-"*80)

    def show_search(self, api):
        word = input("検索したいワードを入力してください： ")
        try:
            statuses = api.GetSearch(term = word, count = 15)
        except:
            print("検索に失敗しました")
        print("-"*80)
        for s in statuses:
            time = s.created_at.split()
            print(self.colors.random_color()+ "{0:}(@{1:}) at {2:}/{3:}/{4:} {5:}".format(
                s.user.name,s.user.screen_name, time[5], time[1], time[2], time[3]
                ) +self.colors.END, end="")
            print(" id:{:}".format(s.id))
            print("""{:}""".format(s.text)
            ) 
        print("-"*80)
            
    def stalk(self, api):
        name = input("誰のストーカーリストを作成しますか？: @").strip()
        try:
            # get friend's follows
            friends = api.GetFriendIDs(screen_name = name)
            
            list = api.CreateList(name = "@{:}".format(name))
            print("しばらくお待ちください")
            for f in friends:
                api.CreateListsMember(list_id = list.id, user_id = f)

            print("リストを作成しました") 
        except:
            ("リストの作成に失敗しました")
