# Twitter Sentiment Analysis Project

A professional NLP pipeline to parse, clean, and analyze the sentiment of tweets regarding trending topics (#AI, #Tech, #Future).

## 📋 Project Features
- **Text Preprocessing**: Cleans raw social media noise (mentions, hashtags, RT tags, and hyperlinks) using regex.
- **Sentiment Classification**: Employs **TextBlob** to perform NLP analysis on cleaned tweet text.
- **Polarity Profiling**: Grades sentiment on a scale from -1.0 (Highly Negative) to +1.0 (Highly Positive).
- **Structured Output**: Saves the resulting processed metadata directly to an exportable CSV dataset.

## 🛠️ Tech Stack
- **Python 3.x**
- **TextBlob**: For polarity and sentiment determination.
- **Pandas**: For dataset formatting and management.
- **Re**: Regular expressions for text processing.

## 🚀 Getting Started

### Prerequisites
Install requirements via pip:
```bash
pip install textblob pandas
```

### Run the Pipeline
```bash
python scraper_twitter.py
```

## 📄 Dataset Schema

| Column | Description |
| :--- | :--- |
| **Tweet_ID** | Unique ID for the post |
| **Topic** | The overarching discussion theme (e.g. AI, Tech) |
| **Raw_Tweet** | Original tweet string directly from the source |
| **Clean_Tweet** | Preprocessed tweet text devoid of hashtags/mentions |
| **Sentiment** | Categorical polarity (Positive, Neutral, Negative) |
| **Polarity_Score** | Numerical polarity rating (-1.0 to 1.0) |
