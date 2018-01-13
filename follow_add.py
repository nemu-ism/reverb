import twitter

class FollowAdd():
    def __init__(self):
        pass

    def follow_add(self, api):
        try:
            name = input("フォローしたいユーザーの＠ネームを入力してください: @").strip()
            api.CreateFriendship(screen_name=name)
            print("{:} さんをフォローしました".format(name))
        except:
            ("{:} さんをフォローできませんでした".format(name))