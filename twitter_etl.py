
import pandas as pd
import time
import s3fs
import os
import googleapiclient.discovery

def process_comments(response_items):
    comments = []
    for comment in response_items:
        author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
        publish_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
        comment_info = {
            'author': author,
            'comment': comment_text,
            'published_at': publish_time
        }
        comments.append(comment_info)
    print(f'Finished processing {len(comments)} comments.')
    return comments

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBUMD_3YVfzN3fUtg1Wic_LA6MKwJsqaRg"  # Keep this secure!

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    video_id = "q8q3OFFfY6c"
    comments_list = []

    # Initial request
    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=video_id,
        maxResults=100  # optional but recommended
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
    df = pd.DataFrame(comments_list)
    csv_file = "comments.csv"
    df.to_csv(csv_file, index=False)
    print(f"Comments saved to {csv_file}")

if __name__ == "__main__":
    main()
