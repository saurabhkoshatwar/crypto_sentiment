# crypto_sentiment

## Summary
* ### Exported the telegram messages from 1 May 2021 to 15 May 2021 using the api client.iter_messages() of library telethon containing words "SHIB" and "DOGE.".
* ### Used the regex library to remove the non english sentences.
* ### Leveraged the spacy library to compute the sentiment score.
* ### Finaly generated the data plots of "Number of messages per day" and "Average sentiments per day" using plotly library. 

## Steps to RUN
1. To install all the dependencies
  `pip install -r requirements.txt` 
2. Run main file
  ` python main.py `

### Inputs
1. #### data.json : List of messages with their timestamp
## Outputs
1. #### count.html : Plot of number of messages per day
2. #### sentiment.html : Plot of average sentiments per day



## Plots

## Number of messages per day

![Count](/Num_messages.JPG)

## Average sentiments per day

![Sentiment](/Average_sentiments.JPG)
  
 
