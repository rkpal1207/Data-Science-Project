import praw
import pandas as pd
from datetime import datetime

# 🔐 Replace with your own credentials
client_id = "PASTE CLIENT_ID"
client_secret = "PASTE CLIENT SECRET"
user_agent = "APP name-app by user"

# 🌐 Connect to Reddit API
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# 🔍 Choose a topic or subreddit
subreddit = reddit.subreddit("all")
keyword = "AI"

# 🔎 Search top 100 posts by keyword
posts = []
for submission in subreddit.search(query="AI", sort="new", limit=200):
    posts.append({
        "title": submission.title,
        "score": submission.score,
        "num_comments": submission.num_comments,
        "created_utc": datetime.utcfromtimestamp(submission.created_utc),
        "subreddit": submission.subreddit.display_name,
        "url": submission.url
    })

# 💾 Save to CSV
df = pd.DataFrame(posts)
df.to_csv("../data/reddit_ai_posts.csv", index=False)
print("✅ Saved Reddit posts to data/reddit_ai_posts.csv")
