from SentimentClassifier import SentimentClassifier

class ChatBot:

    def __init__(self, reddit):
        self.name = "RedditBot"
        self.SentimentClassifier = SentimentClassifier()
        self.reddit = reddit

        self.say = lambda text: print(self.name + ": " + text)
        self.listen = lambda: input("You: ")

    def start(self):
        self.say("Hi! What do you want to talk about?")
        topic = self.listen()
