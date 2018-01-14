import twitter

class FavoriteController:
    def __init__(self):
        pass

    def add_favorite(self, api):
        id = int(input("ふぁぼりたいツイートのIDを入力してください: ").strip())
        try:
            api.CreateFavorite(status_id=id)
            print("ふぁぼりました")
        except:
            print("ふぁぼれませんでした、つぶやきIDを確認してください")