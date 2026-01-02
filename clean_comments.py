import pandas as pd

df = pd.read_csv("comments.csv")

df = df.dropna(subset=["comment"])

df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce")

df["comment_length"] = df["comment"].astype(str).apply(len)
df["word_count"] = df["comment"].astype(str).apply(lambda x: len(x.split()))

df.to_csv("comments_clean.csv", index=False)

print("✅ Cleaning complete. File saved as comments_clean.csv")
