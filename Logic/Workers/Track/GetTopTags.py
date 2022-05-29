"""
Grabs the top tags for a song.
"""

from Logic.Worker import Worker

class GetTopTags(Worker):
    def __init__(self, api_key):
        super(GetTopTags, self).__init__(api_key, 'track.gettoptags')

    def make_call(self, track_name=None, artist_name=None, mbid=None, limit=50):
        params = {
            'limit': limit
        }
        if track_name:
            params['track'] = track_name
        if artist_name:
            params['artist'] = artist_name
        if mbid:
            params['mbid'] = mbid
        return super().make_call(params)

if __name__ == '__main__':
    track_name = input('Track Name: ')
    artist_name = input('Artist Name: ')
    mbid = input('Mbid: ')
    api_key = input("API Key: ")

    Worker = GetTopTags(api_key)
    print(Worker.make_call(track_name, artist_name, mbid))
