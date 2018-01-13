import secrets
import sys
import twitter
import tweepy

class Login:

    def __init__(self):
        pass

    def login(self):
        Consumer_key = 'lIOyR3Dr4s71IToKL17EMCYAD'
        Consumer_secret = 'kzhdWMMlzezKgJWsh8WfPlYnDUe3iyjFRbwHrsqjOlbulbOmXm'
        Access_token = ''
        Access_token_secret = ''
        auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)


        # # get url to get user's access_token and access_token_secrets
        # rediret_url = auth.get_authorization_url()
        # print("次のURLから認証コードを取得してください: {:}".format(rediret_url))
        # verifier = input('認証コードを入力: ').strip()
        # try:
        #     auth.get_access_token(verifier)
        # except:
        #     print("認証コードが違います。")
        #     sys.exit()
        
        # Access_token = auth.access_token
        # Access_token_secret = auth.access_token_secret

        Access_token = secrets.secrets.ACCESS_TOKEN
        Access_token_secret = secrets.secrets.ACCESS_TOKEN_SECRET

        api = twitter.Api(Consumer_key, Consumer_secret, Access_token, Access_token_secret)

        print("login：ok")
        return api

if __name__ == '__main__':
    api = Login().login()
    tweet_content = '進捗dame'
    try:
        api.PostUpdates(tweet_content)
        print("次の内容でつぶやきました：{:}".format(tweet_content))
    except:
        print("つぶやき内容の取得に失敗しました。")