class Commands:
    def __init__(self):
        pass

    def show_commands(self):
        dict = {
            'tweet':'ツイートできます',
            'favorite':'つぶやきIDを利用してふぁぼれます',
            'timeline':'Homeタイムラインを表示します(15件)',
            'follow':'ユーザーをフォローします',
            'remove':'ユーザーをリムーブします',
            'help':'コマンド一覧を表示します',
            'exit':'プログラムを終了します'
        }
        for k, v in dict.items():
            print("{0:} : {1:}".format(k, v))