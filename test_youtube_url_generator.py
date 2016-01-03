"""Test for Youtube url generator"""

import unittest
import requests
import json
import os
from mock import patch
from youtube_url_generator import r, video_title, video_id, video_url, video_post


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


class TestVideoPost(unittest.TestCase):
    """Tests Video Post"""

    def setUp(self):
        """Retrieving data for test"""

        response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part= \
                            snippet&maxResults=1&playlistId=UUH-6LPIGL5V32Xipz38q-aA&key= \
                            AIzaSyBmBXYMZ2TnFYUqpSAd5qmuJ0rEd3OBczA")
        with open('response.json','w') as f:
            f.write(response.text)

    @patch('youtube_url_generator.video_title')
    def test_video_title(self, mock_video_title):
        """Checks if the video title is correct"""

        with open('response.json','r') as fobj:
            get_data = json.load(fobj)

            mock_video_title.return_value = 'Begun Posto (Eggplant curry with Poppy seed) Bengali recipe'
            result = video_title
            title = get_data['items'][0]['snippet']['title']
            self.assertEqual(title, result)

    @patch('youtube_url_generator.video_id')
    def test_video_id(self, mock_video_id):
        """Checks if video id is correct"""

        with open('response.json','r') as fobj:
            get_data = json.load(fobj)

            mock_video_id.return_value = 'jIBelHyXhmY'
            result = video_id
            id = get_data['items'][0]['snippet']['resourceId']['videoId']
            self.assertEqual(id, result)

    @patch('youtube_url_generator.video_url')
    def test_video_url(self, mock_video_url):
        """Checks if video url is correct"""

        with open('response.json','r') as fobj:
            get_data = json.load(fobj)

            mock_video_url.return_value = 'https://www.youtube.com/watch?v=jIBelHyXhmY'
            result = video_url
            watch_url = "https://www.youtube.com/watch?v="
            id = get_data['items'][0]['snippet']['resourceId']['videoId']
            url = watch_url + id
            self.assertEqual(url, result)

    @patch('youtube_url_generator.video_post')
    def test_video_post(self, mock_video_post):
        """Checks if video post is correct"""

        with open('response.json','r') as fobj:
            get_data = json.load(fobj)

            mock_video_post.return_value = ('Begun Posto (Eggplant curry with Poppy seed) Bengali recipe' + '\n' 
                                    + 'https://www.youtube.com/watch?v=jIBelHyXhmY')
            result = video_post
            watch_url = "https://www.youtube.com/watch?v="
            title = get_data['items'][0]['snippet']['title']
            id = get_data['items'][0]['snippet']['resourceId']['videoId']
            url = watch_url + id
            post = title + '\n' + url
            self.assertEqual(post, result)



    def tearDown(self):
        """Deletes the file created for test"""

        os.remove('response.json')


if __name__ == '__main__':
    unittest.main()
