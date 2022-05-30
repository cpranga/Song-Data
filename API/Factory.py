from API.Workers.User.GetTopTracks import GetTopTracks
from API.Workers.Track.GetTopTags import GetTopTags


class Factory:
    def __init__(self, api_key):
        self._api_key = api_key

    def make_worker(self, type):
        if type == 'track.gettoptags':
            return GetTopTags(self._api_key)
        elif type == 'user.gettoptracks':
            return GetTopTracks(self._api_key)


if __name__ == '__main__':
    api_key = input('API Key: ')
    username = input('Username: ')
    factory = Factory(api_key)
    worker = factory.make_worker('user.gettoptracks')
    print(worker.make_call(username))
