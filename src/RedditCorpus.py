import praw
import itertools
from SentimentClassifier import SentimentClassifier
import markovify

class RedditCorpus():

    """
    Wrappers around praw functionality to get sentiment / generate
    a sentence etc
    """

    def __init__(self, reddit, classifier):
        self.reddit = reddit
        self.classifier = classifier
        self.corpus = []


    def build_corpus(self, subreddit, topic):

        def find_sentiment():

            #TODO: Weight by upvotes? Number of comments?

            sentiment = 0

            for comment in self.corpus:
                sentiment += self.classifier.classify(comment.body)

            return sentiment/len(self.corpus)

        results = self.reddit.subreddit(subreddit).search(topic,
                                                          sort='relevance',
                                                          time_filter = 'all')

        for post in itertools.islice(results, 20):
            submission = praw.models.Submission(self.reddit,
                                                id = post.id)
            # if not submission.is_self:
            #     continue

            submission.comments.replace_more(limit=0)

            for comment in submission.comments:
                self.corpus.append(comment)

        self.sentiment = find_sentiment()

        self.text_model = markovify.Text(" ".join([comment.body for comment in self.corpus]), state_size=3)


    def get_sentiment(self):
        return self.sentiment

    def generate_sentence(self):
        sentence = self.text_model.make_sentence()

        while not sentence or (self.classifier.classify(sentence) > 0) != (self.sentiment > 0):
            sentence = self.text_model.make_sentence()

        return sentence
