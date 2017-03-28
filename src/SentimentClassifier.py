import re
import sys
import string

class SentimentClassifier():

    def __init__(self):
        self.load_sentiment_data()


    def load_sentiment_data(self):
        """
        Loads the sentiment data into a hashmap lexicon.

        Hashmap is from word stem to tuples of (multiplier, sentiment)
        """

        lexicon = {}

        pattern = r"type=(\w+) len=1 word1=([\w-]+) pos1=\w+ stemmed1=[yn] priorpolarity=(\w+)"

        with open('../data/subjclueslen1-HLTEMNLP05.tff', 'r') as f:
            for line in f:
                info = list(re.findall(pattern, line)[0])
                # process info
                info[0] = 2 if 'strong' in info[0] else 1 # multiplier

                if info[2] == "positive":
                    info[2] = 1
                elif info[2] == "negative":
                    info[2] = -1
                else:
                    info[2] = 0

                lexicon[info[1]] = (info[0], info[2])

        self.sentiment_lexicon = lexicon


    def classify(self, text):
        """
        Classify a text and return integer representing sentiment
        """
        for char in string.punctuation:
            text = text.replace(char, ' ')

        sentiment = 0
        for word in text.split():
            if word in self.sentiment_lexicon.keys():
                multiplier, sentiment_val = self.sentiment_lexicon[word]
                delta = multiplier * sentiment_val
                sentiment += delta

        return sentiment

if __name__ == '__main__':
    m = SentimentClassifier()
    m.classify(sys.argv[1])
