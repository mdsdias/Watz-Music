from pytube import YouTube, Playlist
from googleapiclient.discovery import build
import requests

DEVELOPER_KEY = "AIzaSyAgp_tp8uP5mdC0pjGxjZ8cVOI-V0mvktE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)

def audioDownload(song):
    idv = search(song, 'song')
    # idvideo = "https://mp3fromyou.tube/download/{}/mp3/320/1631505595/75dad4f5217100e2b9d4550f928cefe534a3507d4cbda4d679ad01dd4af5adfa/0".format(
    #     idv)
    # req = requests.get(idvideo, stream=True)
    idv = "https://www.youtube.com/view?v=" + 'M8yB4NqlnqQ'
    b = YouTube(idv).streams.filter(only_audio=True).download()


def playlistDownload(play):
    playurl = search(play, 'playlist')
    playurl = "https://www.youtube.com/playlist?list=" + playurl
    play = Playlist(playurl).streams.filter(only_audio=True).download()
    return


def search(idsearch):
    videos = []
    playlists = []
    search_response = youtube.search().list(
        q=idsearch,
        part="id,snippet",
        maxResults=100
    ).execute()
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append(search_result['id']['videoId'])
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#playlist':
            playlists.append(search_result['id']['playlistId'])
    return videos, playlists