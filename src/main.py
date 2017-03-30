import praw
import keys
from ChatBot import ChatBot
import argparse


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-d",
                        "--debug",
                        help = "Run in debug mode",
                        action="store_true")

    args = parser.parse_args()

    if args.debug:
        print()
        print("Running bot in debug mode")
        print()
        print()

    reddit = praw.Reddit(client_id = keys.client_id,
                         client_secret = keys.client_secret,
                         user_agent = keys.user_agent)

    bot = ChatBot(reddit, args.debug)
    bot.start()


if __name__ == '__main__':
    main()
