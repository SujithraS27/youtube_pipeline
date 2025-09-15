import pandas as pd
import os
from dotenv import load_dotenv
import googleapiclient.discovery

def process_comments(response_items):
    """
    Processes a list of YouTube comment items and returns structured data.
    """
    comments = []
    for comment in response_items:
        snippet = comment['snippet']['topLevelComment']['snippet']
        comment_info = {
            'author': snippet['authorDisplayName'],
            'comment': snippet['textOriginal'],
            'published_at': snippet['publishedAt']
        }
        comments.append(comment_info)
    print(f'Finished processing {len(comments)} comments.')
    return comments

def main():
    # Load environment variables from .env
    load_dotenv()

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # For local testing only

    API_KEY = os.getenv("YOUTUBE_API_KEY")  # Read key from .env

    if not API_KEY:
        raise ValueError("YouTube API key not found! Please set it in .env file.")

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=API_KEY
    )

    video_id = "q8q3OFFfY6c"  
    comments_list = []

    # Initial request
    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=video_id,
        maxResults=100
    )
    response = request.execute()
    comments_list.extend(process_comments(response.get('items', [])))

    # Handle pagination
    while 'nextPageToken' in response:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=video_id,
            pageToken=response['nextPageToken'],
            maxResults=100
        )
        response = request.execute()
        comments_list.extend(process_comments(response.get('items', [])))

    print(f"Total comments fetched: {len(comments_list)}")

    # Save to CSV
    df = pd.DataFrame(comments_list)
    csv_file = "comments.csv"
    df.to_csv(csv_file, index=False)
    print(f"Comments saved to {csv_file}")

if __name__ == "__main__":
    main()
