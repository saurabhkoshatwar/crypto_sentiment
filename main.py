
import json
from nltk.stem.snowball import SnowballStemmer
import re
import spacy
import pandas as pd
import plotly

def read():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data

def preprocess(sentences):
    for w in sentences:
        if not re.search('[a-zA-Z]', w["message"]) or re.findall("[^\u0000-\u05C0\u2100-\u214F]+", w["message"]):
            sentences.remove(w)
    return sentences

def compute_sentiment(sentences):
    sentences_score = []
    nlp = spacy.load('en_core_web_sm')
    for s in sentences:
      doc = nlp(s["message"])
      score = 0
      for token in doc:
          if token.pos_ == 'ADJ':
              score += token.vector[0]
      s["score"] = score        
      sentences_score.append(s)        
    return sentences_score

def convert_to_df(data):
    df = pd.DataFrame(data)
    return df

def plot_msg_count(df):
    plotly.offline.plot({
        "data": [dict(
            x=df['timestamp'],
            y=df['num_messages'],
            type='bar'
        )],
        "layout": dict(
            title='Number of messages per day'
        )
    },filename="count.html")

def plot_avg_sentiment(df):
    plotly.offline.plot({
        "data": [dict(
            x=df['timestamp'],
            y=df['avg_sentiment'],
            type='bar'
        )],
        "layout": dict(
            title='Sentiment Score Distribution'
        )
    }, filename="sentiment.html")

if __name__ == '__main__':
    data = read()
    preprocessed = preprocess(data)
    message_with_sentiment = compute_sentiment(preprocessed)
    messages_df = convert_to_df(message_with_sentiment)
    num_msg_per_day = messages_df.groupby('timestamp').size().reset_index(name="num_messages")
    plot_msg_count(num_msg_per_day)
    avg_sentiment = messages_df.groupby('timestamp')['score'].mean().reset_index(name="avg_sentiment")
    plot_avg_sentiment(avg_sentiment)

