import requests

# json_bin_api_key = "$2b$10$hi6XDXJIpSChb99CYImQqeCYWKEeOFouRFTfFnsVgKNTIiK4xhFRC"
# game_bin_id = "62edcbf25c146d63ca61134d"

class JSON_Bin:

    # init
    def __init__(self, json_bin_api_key, game_bin_id):
        self.url = f'https://api.jsonbin.io/v3/b/{game_bin_id}/latest'
        self.headers = { 'X-Master-Key': json_bin_api_key }

    # get data
    def get(self):
        req = requests.get(self.url, json=None, headers=self.headers)
        return req.json()

        # apple = (8, 8)
        # snake = [(5, 6), (4, 6), (3, 6), (2, 6)]

    def put(self, data):
        req = requests.put(self.url, data=data, json=None, headers=self.headers)
        return req.text