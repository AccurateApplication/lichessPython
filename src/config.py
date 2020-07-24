import os
import subprocess
import configparser

#class LichessConfiguration(Configuration):
#    api_key = environ_setting("LICHESS_API_KEY", default=None, required=False)
#    api_key_cmd = None
#
#
#    
#class ChessConfiguration(Configuration):
#    lichess = LichessConfiguration()
#    CONF_PATHS = [
#        os.path.abspath("config.yml")
#    ]
#
class LichessConfig:
    def __init__(self,api_key=None,api_key_cmd=None):
        api_key = get_env_or_fallback("LICHESS_API_KEY")
        if api_key_cmd and not api_key:
            output = run_command(api_key_cmd)
            self.api_key = output
        else:
            self.api_key = api_key

def get_env_or_fallback(env,fallback=None):
    try:
        return os.environ[env]
    except KeyError:
        return fallback


class Configuration:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        api_key = config["lichess"].get("api_key")
        api_key_cmd = config["lichess"].get("api_key_cmd")
        self.lichess = LichessConfig(api_key,api_key_cmd)
        pass

def run_command(command_str):
    output = subprocess.check_output(command_str.split())
    return output.decode().strip()


def configuration():
    config = Configuration()

    return config
