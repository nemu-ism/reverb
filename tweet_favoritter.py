import twitter

class TweetFavoritter:
    def __init__(self):
        pass

    def favoritter(self, api):
        id = int(input("つぶやきIDを入力してください:").strip())
        try:
            api.CreateFavorite(status_id=id)
            print("ふぁぼりました")
        except:
            print("ふぁぼれませんでした、つぶやきIDを確認してください")