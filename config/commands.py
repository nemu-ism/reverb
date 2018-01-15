class Commands:
    def __init__(self):
        pass

    def show_commands(self):
        dict = {
            'tweet':'ツイートできます',
            'retweet':'リツイートできます',
            'favorite':'つぶやきIDを利用してふぁぼれます',
            'home':'Homeタイムラインを表示します(15件)',
            'search':'ワードからツイートを検索できます(15件)',
            'lists':'ユーザーの登録しているリスト一覧を表示します',
            'timeline':'リストのタイムラインを表示します(15件)',
            'follow':'ユーザーをフォローします',
            'remove':'ユーザーをリムーブします',
            'mute':'ユーザーのミュートを操作、リストを表示します',
            'stalk':'特定ユーザのストーキングリストを作成します',
            'help':'コマンド一覧を表示します',
            'exit':'プログラムを終了します'
        }
        print("-"*80)
        for k, v in dict.items():
            print("{0:} : {1:}".format(k, v))
        print("-"*80)