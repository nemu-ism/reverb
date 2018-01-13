import sys
import commands
import tweet_writer
import tweet_favoritter
import show_timeline

class Main:

    def __init__(self):
        self.commands = commands.Commands()
        self.tweeter = tweet_writer.TweetWriter()
        self.favoritter = tweet_favoritter.TweetFavoritter()
        self.timeliner = show_timeline.ShowTimeline()
        pass



    def main(self, api):
        while(True):
            control = input("何をしますか？:").strip()
            if control == "tweet":
                self.tweeter.tweeter(api)
            if control == "favorite":
                self.favoritter.favoritter(api)
            elif control == "timeline":
                self.timeliner.show_homeTimeline(api)
            elif control == "help":
                self.commands.show_commands()
            elif control == "exit":
                break
        sys.exit() 