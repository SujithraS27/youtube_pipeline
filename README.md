# Twitter Data Pipeline – End-to-End Data Engineering Project

This is an **End-to-End Data Engineering Project** using **Airflow** and **Python**.  
In this project, we extract data using the **Twitter API**, transform it using **Python**, deploy the code on **Airflow/EC2**, and save the final result on **Amazon S3**.

---

## 📂 Project Overview

The goal of this project is to build a complete data pipeline workflow:

1. **Extract** tweets from a specific user using Twitter API.
2. **Transform** the data using Python (e.g., filtering retweets, formatting timestamps).
3. **Load** the data into Amazon S3 for storage and further analysis.
4. **Deploy** the pipeline using Airflow for scheduling and automation.

---

## 📝 Task 1 – Getting Data from Twitter API

### Objective
Extract tweets from a specific user using the Twitter API and prepare them for further processing.

### Implementation Details
- Used **Tweepy v2 Client** with bearer token authentication.
- Fetched tweets from Elon Musk’s account.
- Filtered out retweets to focus on original content.
- Handled API rate limits (**429 Too Many Requests**) using retry logic with `time.sleep`.
- Handled exceptions to make the script robust against temporary API failures.
- Python scripts are organized to integrate easily with Airflow DAGs for scheduling.
- Output can be saved in **CSV/JSON** for further analysis or demonstration.

### Issues Encountered
1. **403 Forbidden Error**  
   - Occurred due to insufficient API access or temporary account restrictions.
2. **429 Too Many Requests Error**  
   - Rate limit exceeded; handled by pausing the script before retrying.
3. **Missing Bearer Token**  
   - Initially forgot to save the token; learned the importance of secure credential handling.

### Lessons Learned
- API rate limits and authentication must be properly handled in real-world pipelines.  
- Tweepy and Python allow efficient extraction and transformation of API data.  
- Exception handling ensures stability in automated data pipelines.  
- Documenting tasks and issues helps track progress and debugging.

### How to Run Task 1
1. Replace placeholder `'YOUR_BEARER_TOKEN'` in the script with your actual token.
2. Install required packages:

```bash
pip install tweepy pandas s3fs
