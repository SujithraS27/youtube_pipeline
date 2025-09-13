# Twitter Data Pipeline

This is a beginner-level Data Engineering project where I explored how to extract data from Twitter using the X (formerly Twitter) API with Python and handle real-world issues like authentication and rate limits.

---

## 📂 Project Overview

The goal of this project was to build a simple data pipeline that:

1. Authenticates using API keys and bearer tokens.
2. Fetches tweets from a specific user’s timeline.
3. Filters out retweets.
4. Handles API rate limits by waiting and retrying.
5. Prints the extracted tweets for demonstration.

This project helped me understand how APIs work, how to handle errors, and how to build robust scripts that can deal with limitations in external services.

---

## ✅ What I implemented

- Used the Tweepy library to interact with the Twitter API.
- Accessed user tweets via Tweepy’s `Client` with a bearer token.
- Filtered tweets to exclude retweets.
- Handled errors like:
   - **403 Forbidden** – due to API access restrictions.
   - **429 Too Many Requests** – API rate limits requiring retry logic.
- Used exception handling to pause the script when needed.

---

## 🚧 Issues I encountered

1. **403 Forbidden**  
   The API blocked requests because of insufficient permissions or locked accounts.

2. **429 Too Many Requests**  
   The API limited the number of requests in a time window, requiring pauses and retries.

3. **Missing Credentials**  
   Initially forgot to save the bearer token and realized how crucial it is for making requests.

---

## ✅ What I learned

✔ Working with APIs requires understanding authentication, permissions, and limits  
✔ Exception handling is crucial for real-world data pipelines  
✔ Documenting problems helps in debugging and explaining the process  
✔ API rate limits need planning to avoid script failures

---

## 📌 Notes

- All sensitive credentials have been removed from the code.
- To run this project, you need to replace placeholders like `'YOUR_BEARER_TOKEN'` with your actual keys.
- This is a learning project aimed at improving API integration skills.

---

## 📈 Next Steps

- Explore advanced error handling and logging.
- Store data in cloud storage like AWS S3 or databases.
- Integrate scheduling tools like Apache Airflow.
