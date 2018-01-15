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

    def mute_add(self, api):
        name = input("ミュートしたいユーザーの＠ネームを入力してください： @").strip()
        try:
            api.CreateMute(screen_name = name)
            print("{:} さんをミュートしました".format(name))
        except:
            print("{:} さんをミュートできませんでした".format(name))

    def mute_remove(self, api):
        name = input("ミュートを外したいユーザーの＠ネームを入力してください： @").strip()
        try:
            api.DestroyMute(screen_name = name)
            print("{:} さんのミュートを外しました".format(name))
        except:
            print("{:} さんのミュートを外せませんでした".format(name))

    def mute_list(self, api):
        try:
            list = api.GetMutes()
            for l in list:
                print("{0:} (@{1:})".format(l.name, l.screen_name))
        except:
            print("ミュートしているユーザーがいません")