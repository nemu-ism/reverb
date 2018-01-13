import twitter

class FollowRemove:
    def __init__(self):
        pass

    def follow_remove(self, api):
        name = input("リムーブしたいユーザーの＠ネームを入力してください： @").strip()
        try:
            api.DestroyFriendship(screen_name = name)
            print("{:} さんをリムーブしました".format(name))
        except:
            print("{:} さんをリムーブできませんでした".format(name))