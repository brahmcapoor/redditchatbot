import praw
import itertools
import markovify
import pickle
import json
import os
from SentimentClassifier import SentimentClassifier


class RedditCorpus():

    """
    Wrappers around praw functionality to get sentiment / generate
    a sentence etc
    """

    def __init__(self, reddit, classifier, debug):
        self.reddit = reddit
        self.classifier = classifier
        self.corpus = []
        self.debug = debug
        self.debug_msg = lambda text: print("CORPUS_DEBUG: " + str(text))


    def build_corpus(self, subreddit, topic):

        def find_sentiment():

            #TODO: Weight by upvotes? Number of comments?

            sentiment = 0

            for comment in self.corpus:
                sentiment += self.classifier.classify(comment.body)

            return sentiment/len(self.corpus)

        def try_load_corpus_and_model():
            name = "{}_{}".format(subreddit, topic)

            corpus_filename = "../data/{}.pickle".format(name)
            model_filename = "../data/{}_model.txt".format(name)

            if os.path.isfile(corpus_filename):

                with open(corpus_filename, 'rb') as corpus:
                    self.corpus = pickle.load(corpus)

                with open(model_filename, 'r') as model:
                    print(str(model))
                    self.text_model = markovify.Text.from_json(model.read())

                self.debug_msg("Loaded corpus and model from file")

                return True

            return False

        def save_corpus_and_model():

            name = "{}_{}".format(subreddit, topic)
            corpus_filename = "../data/{}.pickle".format(name)

            with open(corpus_filename, 'wb') as f:
                pickle.dump(self.corpus, f)

            model_json = self.text_model.to_json()

            model_filename = "../data/{}_model.txt".format(name)

            with open(model_filename, 'w') as f:
                f.write(model_json)

            self.debug_msg("Saved corpus and model to {} and {}".format(corpus_filename, model_filename))

        def load_from_web():
            results = self.reddit.subreddit(subreddit).search(topic,
                                                              sort='relevance',
                                                              time_filter = 'all')

            for post in itertools.islice(results, 10):
                submission = praw.models.Submission(self.reddit,
                                                    id = post.id)

                submission.comments.replace_more(limit=0)

                for comment in submission.comments:
                    self.corpus.append(comment)


        if self.debug:
            self.debug_msg("Attempting to load corpus and model from file")
            if not try_load_corpus_and_model():
                self.debug_msg("Failed. Downloading from website")
                load_from_web()
        else:
            load_from_web()

        self.sentiment = find_sentiment()

        if self.debug:
            self.debug_msg("Sentiment of corpus is " + str(self.sentiment))

        self.text_model = markovify.Text(" ".join([comment.body for comment in self.corpus]), state_size = 3)

        if self.debug:
            save_corpus_and_model()


    def get_sentiment(self):
        return self.sentiment

    def generate_sentence(self):
        sentence = self.text_model.make_sentence()

        while not sentence or (self.classifier.classify(sentence) > 0) != (self.sentiment > 0):
            sentence = self.text_model.make_sentence()

        return sentence
