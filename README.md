AutoShare
===========

Automates sharing of video url on facebook wall when uploaded on Youtube.
The application uses Python 3. But you can run with Python 2 as well.

##Installation##

    sudo dnf install python3-virtualenv
    virtualenv venv
    source venv/bin/activate
    git clone https://github.com/trishnaguha/AutoShare.git
    cd AutoShare
    pip install -r requirements.txt

##Usage##

* Get PlaylistId and API Key from Youtube and Access Token from Facebook.
* Add them to `Youtube_playlistId`, `Youtube_api_key` and `Access_token` is settings.py
* `python3 autoshare.py`

###YouTube Settings###

* Go to [Console developers google](https://console.developers.google.com)
* Create a new project and go to API manager.
* Make sure the status is ON for YouTube Data API v3.
* Select Credentials from left sidebar and generate API key.
* [Resource](https://developers.google.com/youtube/registering_an_application) for YouTube API doc
* Go to [Api explorer for YouTube](https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.channels.list)
* Fill `part` as `ContentDetails` and `mine` as `true`.
* Make sure the status is ON for OAuth 2.0 and grant permission for all scopes.
* Then click on Execute that will generate Response.
* Copy the `uploads` id which is the `playlistId`.

###Facebook Settings###

* Go to [Developers facebook](https://developers.facebook.com/tools/explorer)
* Get Access token from `Extended Permissions` selecting `publish_actions` and from `User Data Permissions` selecting `user_posts`

##Development Purpose

Follow [Installation](https://github.com/trishnaguha/AutoShare#installation) and [Usage](https://github.com/trishnaguha/AutoShare#usage) for development
