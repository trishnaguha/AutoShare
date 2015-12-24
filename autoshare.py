"""AutoShare"""

import requests
import json
from settings import Facebook_base_url,Access_token
from youtube_url_generator import video_url


def facebook_post():
    """Posts the video url on facebook wall"""

    post_message = video_url
    post_message.replace(' ', '+')

    """Posting on facebook wall"""
    r = requests.post(Facebook_base_url + post_message + "&access_token=" + Access_token)

    # Prints error if posting is not successful
    try:
        if r.status_code != 200:
            raise Exception(r)
        else:
            pass
    except Exception as e:
        json_error = json.loads(r.text)
        print("Posting is not successful")
        print('ErrorMessage: ' + (json_error['error']['message']))
        print('ErrorType: ' + (json_error['error']['type']))
        print(e)


if __name__ == '__main__':
    facebook_post()
