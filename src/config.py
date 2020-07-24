import subprocess
import configparser
import sys
from dynaconf import Dynaconf,Validator


def pass_cmd(command_str):
    try:
        
        output = subprocess.check_output(command_str.split())
        return output.decode().strip()
    except Exception as e:
        print(f"ERROR! Failed to run api_key_cmd:\n{e}")
        sys.exit(1)


def configuration():

    settings = Dynaconf(
        envvar_prefix="TCHESS",
        settings_files=['settings.toml'],
        load_dotenv=True,
        validators = [
            Validator('LICHESS.API_KEY', must_exist=True) | Validator('LICHESS.API_KEY_CMD', must_exist=True),

        ]

    )
    settings.validators.validate()

    if settings.lichess.get("api_key_cmd") and not settings.lichess.get("api_key"):
        settings.lichess.api_key = pass_cmd(settings.lichess.api_key_cmd)
        

    return settings
