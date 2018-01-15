import sys
import controllers
import config

class Main:
    def __init__(self):
        self.commands = config.commands.Commands()
        self.oauth = controllers.oauth_controller.OauthController()
        self.follower = controllers.follow_controller.FollowController()
        self.tweeter = controllers.tweet_controller.TweetController()
        self.favoritter = controllers.favorite_controller.FavoriteController()
        self.timeliner = controllers.timeline_controller.TimelineController()
        pass

    def main(self, api):
        while(True):
            control = input("何をしますか？:").strip()
            if control == "help":
                self.commands.show_commands()
            elif control == "follow":
                self.follower.follow_add(api)
            elif control == "remove":
                self.follower.follow_remove(api)
            elif control == "mute":
                choice = input("ミュートに加えますか？外しますか？(add or remove or list):").strip()
                if choice == "add":
                    self.follower.mute_add(api)
                elif choice == "remove":
                    self.follower.mute_remove(api)
                elif choice == "list":
                    self.follower.mute_list(api)
            elif control == "tweet":
                self.tweeter.tweet(api)
            elif control == "retweet":
                self.tweeter.retweet(api)
            elif control == "favorite":
                self.favoritter.add_favorite(api)
            elif control == "home":
                self.timeliner.show_home(api)
            elif control == "lists":
                self.timeliner.show_lists(api)
            elif control == "timeline":
                self.timeliner.show_timeline(api)
            elif control == "search":
                self.timeliner.show_search(api)
            elif control == "stalk":
                self.timeliner.stalk(api)
            elif control == "exit":
                break
        sys.exit() 

if __name__ == '__main__':
    reverb = Main()
    try:
        print("reverbを開始します")
        api = reverb.oauth.login()
        reverb.main(api)
    except:
        print("reverbを終了します")
        sys.exit()