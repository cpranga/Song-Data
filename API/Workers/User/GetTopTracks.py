from API.Worker import Worker


class GetTopTracks(Worker):
    def __init__(self, api_key):
        super().__init__(api_key, 'user.gettoptracks')

    def make_call(self, user_name: str, limit: int = 50) -> dict:
        params = {
            'user': user_name,
            'limit': limit
        }
        return super().make_call(params)


if __name__ == '__main__':
    user = input("Username: ")
    api_key = input("API Key: ")
    Worker = GetTopTracks(api_key)
    print(Worker.make_call(user))
