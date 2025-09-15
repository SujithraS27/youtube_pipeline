# YouTube Comments Data Pipeline using Airflow

## **Project Overview**

This is an **End-to-End Data Engineering Project** using **Airflow** and **Python**. The main goal of this project is to:

- Extract comments from YouTube videos using the **YouTube Data API**.
- Transform the data using **Python** and **Pandas**.
- Deploy the pipeline on **Airflow/EC2**.
- Save the final results on **Amazon S3** for downstream use.

---

## ✅ **Task 1 – Getting Data from YouTube API**

### **Objective**

Extract comments from a specific YouTube video and prepare them for further processing.

### **Implementation Details**

- Used `googleapiclient.discovery` with API key authentication.
- Fetched comments from the specified video by its ID.
- Handled pagination using `nextPageToken` to retrieve all comments.
- Transformed the data using **Python** and **Pandas**, extracting:
  - Author name  
  - Comment text  
  - Published date
- Saved the final result as a CSV file (`comments.csv`) that can be opened in Excel.

### **Issues Encountered**

- **403 Forbidden Error** – caused by API not being enabled or incorrect API key configuration.  
- **Line Ending Warnings (LF vs CRLF)** – resolved using Git settings for consistent line endings on Windows.

### **Lessons Learned**

- Proper API authentication and permissions are crucial.  
- Handling pagination ensures complete data extraction.  
- Pandas is powerful for transforming and structuring data.  
- Documenting issues and solutions aids troubleshooting and future development.
