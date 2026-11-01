import pandas as pd
import re
import time
# We will use TextBlob for sentiment analysis
try:
    from textblob import TextBlob
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "textblob"])
    from textblob import TextBlob

def clean_tweet(text):
    """Utility function to clean tweet text by removing links, special characters using simple regex."""
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)  # remove mentions
    text = re.sub(r'#', '', text)               # remove hashtags
    text = re.sub(r'RT[\s]+', '', text)         # remove RT
    text = re.sub(r'https?:\/\/\S+', '', text) # remove hyperlinks
    return text.strip()

def get_sentiment(text):
    """Analyze sentiment polarity and classify."""
    analysis = TextBlob(clean_tweet(text))
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity == 0:
        sentiment = 'Neutral'
    else:
        sentiment = 'Negative'
    
    return sentiment, round(polarity, 2)

def simulate_twitter_data():
    print("Simulating active Twitter feed retrieval for targeted keywords (#AI, #Tech, #Future)... ")
    
    # High fidelity sample tweets across various topics and sentiments
    raw_tweets = [
        ("@tech_insider AI is going to absolutely change the world for the better! Insanely excited for what is next! #AI #Future", "AI"),
        ("Had a horrible experience with the new software update. It crashed my system three times today. Avoid it. #tech #fail", "Tech"),
        ("Just reading the new guidelines on artificial intelligence regulation. Pretty standard stuff, nothing exciting.", "AI"),
        ("The new electric vehicle models look incredibly sleek! Innovation is booming right now.", "Future"),
        ("I do not understand the hype around this new app. It is extremely slow and laggy.", "Tech"),
        ("Generative AI tools are saving me hours of work every single week. Highly recommend checking them out!", "AI"),
        ("Cloud servers are down again. This is unacceptable for a multi-billion dollar enterprise.", "Tech"),
        ("Beautiful morning to sit down, grab a coffee, and code some web scrapers!", "Future"),
        ("The debate around artificial general intelligence is getting a bit exhausting honestly.", "AI"),
        ("I love how open-source libraries make NLP so accessible to everyone.", "Tech")
    ]
    
    processed_data = []
    for i, (tweet, topic) in enumerate(raw_tweets, 1):
        sentiment, score = get_sentiment(tweet)
        processed_data.append({
            "Tweet_ID": f"179040{i:03d}",
            "Topic": topic,
            "Raw_Tweet": tweet,
            "Clean_Tweet": clean_tweet(tweet),
            "Sentiment": sentiment,
            "Polarity_Score": score
        })
        time.sleep(0.2) # Throttling simulator
        
    df = pd.DataFrame(processed_data)
    df.to_csv('twitter_sentiment_data.csv', index=False)
    print("Analysis complete! Data successfully saved to 'twitter_sentiment_data.csv'")

if __name__ == '__main__':
    simulate_twitter_data()
