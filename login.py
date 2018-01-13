import sys
import twitter
import tweepy

Consumer_key = 'CqMaN3s51fk1fzc7LaVpzS788'
Consumer_secret = 'qSGbRed3cuDZFyfhKVusWD7wpTkTmvpn7w141f2vGCxpyzYNap'
Access_token = ''
Access_token_secret = ''
auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)


# # get url to get user's access_token and access_token_secrets
# rediret_url = auth.get_authorization_url()
# print("次のURLから認証コードを取得してください: {:}".format(rediret_url))
# for _ in range(10):
#     verifier = input('認証コードを入力: ').strip()
#     try:
#         auth.get_access_token(verifier)
#         Access_token = auth.access_token
#         Access_token_secret = auth.access_token_secret
#     except:
#         print("認証コードが違います。")
#         pass
# else:
#     print("認証コードの入力に失敗しました。")
#     sys.exit()

Access_token = '3148157702-l7yVVD3mLREox0e8Cic7lVKhzxiMTb0eDTGPji2'
Access_token_secret = 'pO24QfAWjOLzROMNd9Dqv1xafS8xddI3v2aCiiT1YIuf7'

api = twitter.Api(Consumer_key, Consumer_secret, Access_token, Access_token_secret)

print("ok")


