import os
import requests
import json
import ndjson

def stream_board_state(game_id, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    return requests.get(f'https://lichess.org/api/board/game/stream/{game_id}', headers=headers, stream=True)
def make_board_move(game_id, move,api_key = os.environ["LICHESS_API_KEY"]):
    headers = {"Authorization": f"Bearer {api_key}"}
    return requests.post(f'https://lichess.org/api/board/game/{game_id}/move/{move}', headers=headers)

