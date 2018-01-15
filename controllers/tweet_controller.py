import twitter

class TweetController:
    def __init__(self):
        pass

    def tweet(self, api):
        tweet_content = input("ツイートする内容を入力してください: ").strip()
        try:
            api.PostUpdates(tweet_content)
            print("次の内容でツイートしました：{:}".format(tweet_content))
        except:
            print("ツイート内容の取得に失敗しました。")

    def retweet(self, api):
        id = input("リツイートするツイートのIDを入力してください: ").strip()
        try:
            api.PostRetweet(stasus_id = id)
            print("リツイートしました")
        except:
            print("リツイートに失敗しました、ツイートIDを確認してください")