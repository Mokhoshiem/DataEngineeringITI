

import os
import googleapiclient.discovery
import csv
def get_youtube_service():
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "YOUR API KEY"
    print('apikey',api_key)
    return googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

def search_channels(query, max_results=50):
    youtube = get_youtube_service()
    request = youtube.search().list(
        part="snippet",
        type="channel",
        q=query,
        maxResults=max_results
    )
    response = request.execute()
    return response.get("items", [])

def main():
    query = "Mathematics"
    max_results = 500
    channels = search_channels(query, max_results)
    print('Starting ...........')
    with open(f'{query}.csv','a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title','channel_id','description'])
        for channel in channels:
            title = channel["snippet"]["title"]
            channel_id = channel["snippet"]["channelId"]
            description = channel["snippet"]["description"]
            writer.writerow([title,channel_id,description])
            print(f"Title: {title}")
            print(f"Channel ID: {channel_id}")
            print(f"Description: {description}")
            print("="*40)
    print('Done........')

if __name__ == "__main__":
    main()
