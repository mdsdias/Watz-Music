def __init__(idsearch):
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