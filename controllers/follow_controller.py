import twitter

class FollowController:
    def __init__(self):
        pass

    def follow_add(self, api):
        name = input("フォローしたいユーザーの＠ネームを入力してください: @").strip()
        try:
            api.CreateFriendship(screen_name = name)
            print("{:} さんをフォローしました".format(name))
        except:
            print("{:} さんをフォローできませんでした".format(name))

    def follow_remove(self, api):
        name = input("リムーブしたいユーザーの＠ネームを入力してください： @").strip()
        try:
            api.DestroyFriendship(screen_name = name)
            print("{:} さんをリムーブしました".format(name))
        except:
            print("{:} さんをリムーブできませんでした".format(name))