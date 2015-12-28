"""Test for Youtube url generator"""

import unittest
import requests
import json
import os
from mock import patch
from youtube_url_generator import r


class TestRequestsStatus(unittest.TestCase):
    """
    Tests the status code of response
    """
    @patch('youtube_url_generator.r')
    def test_requests_status(self, mock_r):
        """Tests the status of response"""

        mock_r.return_value = 200
        result = r
        self.assertEqual(200, result)

    @patch('youtube_url_generator.r')
    def test_requests_status_error(self,mock_r):
        """
        Tests exception raise due to not
        getting proper response
        """
        mock_r.return_value = 200
        result = r
        self.assertRaises(Exception, result, 400)
        self.assertRaises(Exception, result, 404)


class TestYoutubePost(unittest.TestCase):
    """Tests YouTube post"""

    def setUp(self):
        """Setting up for test"""

        response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part= \
                            snippet&maxResults=1&playlistId=UUH-6LPIGL5V32Xipz38q-aA&key= \
                            AIzaSyBmBXYMZ2TnFYUqpSAd5qmuJ0rEd3OBczA")
        with open('response.json','w') as f:
            f.write(response.text)

    def test_video_post(self):
        """
        Tests if the post is correct
        """
        watch_url = "https://www.youtube.com/watch?v="

        with open('response.json','r') as fobj:
            get_data = json.load(fobj)

            # Checks video title
            video_title = get_data['items'][0]['snippet']['title']
            title ='Begun Posto (Eggplant curry with Poppy seed) Bengali recipe'
            self.assertEqual(title, video_title, video_title)

            # Checks video id
            video_id = get_data['items'][0]['snippet']['resourceId']['videoId']
            id = 'jIBelHyXhmY'
            self.assertEqual(id, video_id, video_id)

            # Checks video url
            video_url = watch_url + id
            url = 'https://www.youtube.com/watch?v=jIBelHyXhmY'
            self.assertEqual(url, video_url, video_url)

            # Checks video post
            video_post = title + '\n' + url
            post = ('Begun Posto (Eggplant curry with Poppy seed) Bengali recipe' + '\n' 
                        + 'https://www.youtube.com/watch?v=jIBelHyXhmY')
            self.assertEqual(post, video_post, video_post)

    def tearDown(self):
        """Deletes the file created for test"""

        os.remove('response.json')

if __name__ == '__main__':
    unittest.main()
