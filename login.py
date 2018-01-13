import sys
import twitter
import tweepy

Consumer_key = 'JQlDOEzxGeq2eLEgErFCLzy2z'
Consumer_secret = 'rnBWO8k0dZMaO4RjGpTudCTNWDRqIDnTm05at1sbKL6f1Fbqbi'
Access_token = ''
Access_token_secret = ''
auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)


# get url to get user's access_token and access_token_secrets
rediret_url = auth.get_authorization_url()
print("次のURLから認証コードを取得してください: {:}".format(rediret_url))
for _ in range(10):
    verifier = input('認証コードを入力: ').strip()
    try:
        auth.get_access_token(verifier)
    except:
        print("認証コードが違います。")
        pass
    else:
        Access_token = auth.access_token
        Access_token_secret = auth.access_token_secret
        break
else:
    print("認証コードの入力に失敗しました。")
    sys.exit()

# Access_token = '3148157702-Mm2cHiHoqf2jUwzy8qIYeDzJZFL9jSSGGFmphN1'
# Access_token_secret = 'JGIImXrX99T1BTHeAe1LOaDu2aNNfix8l8rjv2fA4Sdwu'

api = twitter.Api(Consumer_key, Consumer_secret, Access_token, Access_token_secret)

print("ok")

