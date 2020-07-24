# Lichess Terminal Client

## Setup
### Token setup
To be able to play lichess in the terminal you will need to create an API key [here](https://lichess.org/account/oauth/token) 


### Keybindigs

While in game you can move around your cursor using vim-bindings hjkl. To move a piece you select the piece you want to move using "c", select which square you want to move to using "x" and make the move using "m"


### Configuring

#### Using .env file
*Copy .env from example:*
```shell
cp .env.example .env
```

*Fill in your own configuration in* `.env`.

#### Using environment variable
*Set the variable `TCHESS_LICHESS__API_KEY`:*
```shell
export TCHESS_LICHESS__API_KEY=$(pass show api/lichess.org) # or just enter a plain text api key.
```

#### Using config file:
*Copy settings.toml from example:*
```
cp settings.toml.example settings.toml
```

*Fill in your own configuration in* `settings.toml`.



### Start game
```
pipenv run play_game <game_id>
```
