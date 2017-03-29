# redditchatbot

```python
#TODO: a better (read: actually good) name
```

## about this project
I think reddit is cool, and after doing Stanford's [CS124](http://web.stanford.edu/class/cs124/), I think chatbots and Natural Language Processing are cool. One thing led to another, and redditchatbot happened.

This is an attempt to take the sometimes variegated, sometimes hivemind-esque arena that is reddit and synthesize its views on particular topics in a way that's engaging and new. I think that the ability to access so many perspectives so easily can be incredibly powerful tool, and I see this as a new way of interacting with the wealth of opinions on reddit.

It's early days yet, and I'm open to suggestions as to how to proceed to best aggregate opinions.


## what redditchatbot can do right now

Not much, just yet. See below for details

#### sentiment analysis
I've got a basic sentiment analysis module up and running (many thanks to the [MPQA subjectivity lexicon](http://mpqa.cs.pitt.edu/lexicons/subj_lexicon/)), which is just a naive weighted count of emotive words, but I still have some work to do before I can say it's complete.

I'm on the lookout for some way to procure some training data so I could use something like Naive Bayes or Logistic Regression, but for now this seems sufficient. If all else fails, I might just bootstrap some data myself. Suggestions for good ways to do this would be awesome.


#### building a corpus
Right now, the bot asks for a specific subreddit to talk to and a conversation topic. It then searches that subreddit for the most relevant posts to do with that topic and builds a corpus from the top-level comments in those posts. This is _okay_ for an initial attempt, but I'd ideally like to be able to speak to reddit as a whole as well. You can do that right now by specifying r/all as the subreddit you want to talk to, but that's a little hacky.

#### sentence generation and conversation
For now, I've just got markov chains being built from a corpus, and regenerated until one with the same sentiment as the prevailing sentiment about that topic is generated. This leads to some pretty hilarious insights:

```
RedditBot: Hi! Which subreddit would you like to talk to?
You: movies
RedditBot: Cool! What do you want to talk about?
You: Christopher Nolan
RedditBot: I saw Interstellar last night and I thought it felt kind of off, considering the rest of the movie itself is a magic trick in itself.
```

That said, the bot isn't currently contextually aware (technically, it doesn't even respond to the user so much as it does wait for the user to finish typing) so I'm going to revamp this. My two ideas right now are to use child comments as well and to hardcode some more specific kinds of responses. 

## setup

1) Clone the project
2) `cd` to the `src` directory and create the file `keys.py`
3) [Create a reddit app](https://ssl.reddit.com/prefs/apps). You'll need an account for this part. The app type is a script.
4) Get the client id (that's the bit below your app's name on the website), the client secret and fill out `keys.py` as such:

```python
client_id = "CLIENT ID HERE"
client_secret = "CLIENT SECRET HERE"
user_agent = "python:PROJECT_NAME_HERE:VERSION_NUMBER_HERE (by /u/YOUR REDDIT USERNAME HERE)."
```

Obviously, make the appropriate substitutions.

5) In the same directory, run `python main.py`

## the future

Obviously, of paramount importance right now is just getting it up and running.

In the future, I think it might be cool to make this a web app because while using the terminal is badass, I think this is something other people would like to use. That said, doing this will probably involve learning Django/Flask and a significant restructuring, so it's a long term goal.

## contact and contributing

If you have ideas or questions, feel free to ping me at brahm@stanford.edu

Otherwise, feel free to submit a pull request.

<br>
<br>
<br>

<p align='center'>
<em> Made with 💻 in 🇸🇬 by Brahm Capoor </em>
</p>
