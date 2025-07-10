# Reddit Trend Analyzer

A beginner-friendly end-to-end NLP + Machine Learning project that collects real Reddit data, analyzes trends, and predicts which posts might go viral based on their titles.

---

## Project Overview

This project walks through the full data science process:
- 📡 Collect live Reddit posts using Reddit’s API (`praw`)
- ✂️ Clean and tokenize the post titles using NLP
- 📊 Perform sentiment analysis with `textblob`
- 🔍 Visualize most common words and sentiment distribution
- 🤖 Train a machine learning model to predict post virality
- 📈 Analyze which words most influence upvote success

---

## Dataset

- **Source**: Reddit API (`praw`)
- **Topic**: Posts containing the keyword `"AI"` (from r/all)
- Each record includes: `title`, `score`, `num_comments`, `subreddit`, and `timestamp`

---

## Tools Used

| Category | Tools |
|---------|-------|
| Programming | Python |
| Data | pandas, praw |
| NLP | nltk, textblob |
| ML | scikit-learn (LogisticRegression, RandomForest) |
| Visualization | seaborn, matplotlib |
| Environment | Jupyter Notebook, Anaconda |

---