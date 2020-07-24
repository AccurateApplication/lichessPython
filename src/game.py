import logging
import src.terminal as terminal
import src.api as api

from src.config import configuration

class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        self.config = configuration()
        print(self.config)
        self.api = api.Api(api_key=self.config.lichess.api_key)
        self.stream = self.api.stream_board_state(self.game_id)
        self.tui = terminal.GameUi(config=self.config, stream=self.stream, game_id=self.game_id, api=self.api)

    def play(self):
        self.tui.start()
