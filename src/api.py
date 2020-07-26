import os
import requests
import json
import ndjson

class Api:
    def __init__(self, api_key):
        self.api_key = api_key

    def stream_board_state(self, game_id):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        return requests.get(f'https://lichess.org/api/board/game/stream/{game_id}', headers=headers, stream=True)
    def make_board_move(self, game_id, move):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        return requests.post(f'https://lichess.org/api/board/game/{game_id}/move/{move}', headers=headers)

    def get_profile(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        return requests.get(f'https://lichess.org/api/account', headers=headers)

