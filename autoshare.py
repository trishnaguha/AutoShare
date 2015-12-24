'''AutoShare'''

import requests
import json
from settings import *

def video_url():

    # Get response
    r = requests.get(Youtube_base_url + Youtube_api_key)

    # Generates the latest video url
    try:
        if r.status_code == 200:
            json_data = json.loads(r.text)
            video_id = (json_data['items'][0]['snippet']['resourceId']['videoId'])
            video_url = Youtube_watch_url + video_id
            print(video_url)
        else:
            raise Exception(r)
    except Exception as e:
        print(e)

def main():
    video_url()

if __name__ == '__main__':
    main()
