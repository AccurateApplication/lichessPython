import os
import subprocess
from confire import Configuration
from confire import environ_setting

class LichessConfiguration(Configuration):
    api_key = environ_setting("LICHESS_API_KEY", default=None, required=False)
    api_key_cmd = None


    
class ChessConfiguration(Configuration):
    lichess = LichessConfiguration()
    CONF_PATHS = [
        os.path.abspath("config.yml")
    ]


def run_command(command_str):
    output = subprocess.check_output(command_str.split())
    return output.decode()


def configuration():
    config = ChessConfiguration.load()

    if config.lichess.api_key_cmd and not config.lichess.api_key:
        output = run_command(config.lichess.api_key_cmd)
        config.lichess.api_key = output
    return config
