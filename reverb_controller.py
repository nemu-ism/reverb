import sys
import commands
import follow_add
import tweet_writer
import tweet_favoritter
import show_timeline

class Main:
    def __init__(self):
        self.commands = commands.Commands()
        self.adder = follow_add.FollowAdd()
        self.tweeter = tweet_writer.TweetWriter()
        self.favoritter = tweet_favoritter.TweetFavoritter()
        self.timeliner = show_timeline.ShowTimeline()
        pass

    def main(self, api):
        while(True):
            control = input("何をしますか？:").strip()
            if control == "help":
                self.commands.show_commands()
            elif control == "follow":
                self.adder.follow_add(api)
            elif control == "tweet":
                self.tweeter.tweeter(api)
            elif control == "favorite":
                self.favoritter.favoritter(api)
            elif control == "timeline":
                self.timeliner.show_homeTimeline(api)
            elif control == "exit":
                break
        sys.exit() 