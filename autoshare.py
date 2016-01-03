"""AutoShare"""

import requests
import json
from settings import Facebook_base_url,Access_token
from youtube_url_generator import video_post


def facebook_post():
    """Posts the video url on facebook wall"""

    post_message = video_post
    post_message.replace(' ', '+')

    response_get = requests.get(Facebook_base_url + "?access_token=" + Access_token)
    r_get = response_get.status_code
    try:
        if r_get == 200:
            try:
                get_data = json.loads(response_get.text)
                for i in get_data['data']:

                    # Checks if the post is already on facebook wall
                    if (i['message']) == post_message:
                        raise Exception("DuplicateMessageError: The link has already" +
                                    " been shared before: No Duplicate post allowed")
                else:
                    """Posting on facebook wall"""
                    response_post = requests.post(Facebook_base_url + "?message=" + \
                                        post_message + "&access_token=" + Access_token)
                    r_post = response_post.status_code

                    # Prints error if posting is not successful
                    try:
                        if r_post != 200:
                            raise Exception(r_post)
                        else:
                            pass
                    except Exception as e:
                        get_error = json.loads(response_post.text)
                        print("Posting is not successful")
                        print('ErrorMessage: ' + (get_error['error']['message']))
                        print('ErrorType: ' + (get_error['error']['type']))
                        print(e)

            # Prints error if message/post is duplicate
            except Exception as e:
                print(e)
        else:
            raise Exception(r_get)

    # Prints error if unable to retrieve posts
    except Exception as e:
        error_message = json.loads(response_get.text)
        print('ErrorMessage: ' + (error_message['error']['message']))
        print('ErrorType: ' + (error_message['error']['type']))
        print(e)


if __name__ == '__main__':
    facebook_post()
