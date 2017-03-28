import praw
import keys
from ChatBot import ChatBot


def main():
    reddit = praw.Reddit(client_id = keys.client_id,
                         client_secret = keys.client_secret,
                         user_agent = keys.user_agent)

    bot = ChatBot(reddit)
    bot.start()


if __name__ == '__main__':
    main()
