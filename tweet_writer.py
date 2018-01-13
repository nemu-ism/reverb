import reverb
import twitter

api = reverb.api

tweet_content = input("Your tweet is:").strip()
try:
    api.PostUpdates(tweet_content)
except:
    print("つぶやき内容の取得に失敗しました。")