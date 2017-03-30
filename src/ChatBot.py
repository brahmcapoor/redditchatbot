from SentimentClassifier import SentimentClassifier
from RedditCorpus import RedditCorpus

class ChatBot:

    def __init__(self, reddit, debug):
        # Initializing attributes
        self.name = "RedditBot"
        self.sentiment_classifier = SentimentClassifier()
        self.reddit_corpus = RedditCorpus(reddit, self.sentiment_classifier, debug)

        # helpers
        self.say = lambda text: print(self.name + ": " + str(text))
        self.listen = lambda: input("You: ")
        self.debug_msg = lambda text:print("BOT_DEBUG: " + str(text))

        # flags
        self.debug = debug # increases bot verbosity if True

    def start(self):

        self.say("Hi! Which subreddit would you like to talk to?")
        subreddit = self.listen()

        self.say("Cool! What do you want to talk about?")
        topic = self.listen()

        self.reddit_corpus.build_corpus(subreddit, topic)


        while True:
            self.say(self.thoughts())
            self.listen()


    def thoughts(self):
        return self.reddit_corpus.generate_sentence()
