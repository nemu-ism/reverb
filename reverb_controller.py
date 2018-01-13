import sys
import tweet_writer
import show_timeline

class Main:

    def __init__(self):
        self.tweeter = tweet_writer.TweetWriter()
        self.timeliner = show_timeline.ShowTimeline()
        pass



    def main(self, api):
        while(True):
            control = input("何をしますか？:").strip()
            if control == "tweet":
                self.tweeter.tweeter(api)
            elif control == "timeline":
                self.timeliner.show_homeTimeline(api)
            elif control == "exit":
                break
        sys.exit() 