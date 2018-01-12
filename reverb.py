import tweepy
from Tools.scripts.treesync import raw_input


Consumer_key = 'JQlDOEzxGeq2eLEgErFCLzy2z'
Consumer_secret = 'rnBWO8k0dZMaO4RjGpTudCTNWDRqIDnTm05at1sbKL6f1Fbqbi'
auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)

## get url to get user's access_token and access_token_secrets
#rediret_url = auth.get_authorization_url()
#print("Get your Verification code from: {:}".format(rediret_url))
#
#verifier = raw_input('Type the verification code: ').strip()
#auth.get_access_token(verifier)
#Access_token = auth.access_token
#Access_token_secret = auth.access_token_secret

Access_token = '3148157702-Mm2cHiHoqf2jUwzy8qIYeDzJZFL9jSSGGFmphN1'
Access_token_secret = 'JGIImXrX99T1BTHeAe1LOaDu2aNNfix8l8rjv2fA4Sdwu'
auth.set_access_token(Access_token, Access_token_secret)

api = tweepy.API(auth)

print('ok')