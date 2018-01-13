import twitter

class FollowAdd():
    def __init__(self):
        pass

    def follow_add(self, api):
        name = input("フォローしたいユーザーの＠ネームを入力してください: @").strip()
        try:
            api.CreateFriendship(screen_name = name)
            print("{:} さんをフォローしました".format(name))
        except:
            print("{:} さんをフォローできませんでした".format(name))