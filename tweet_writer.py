import twitter

class TweetWriter:
    def __init__(self):
        pass

    def tweeter(self, api):
        tweet_content = input("つぶやく内容を入力してください:").strip()
        try:
            api.PostUpdates(tweet_content)
            print("次の内容でつぶやきました：{:}".format(tweet_content))
        except:
            print("つぶやき内容の取得に失敗しました。")