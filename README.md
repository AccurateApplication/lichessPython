# Lichess Terminal Client

## Setup
### Token setup
To be able to play lichess in the terminal you will need to create an API key [here](https://lichess.org/account/oauth/token) 


### Keybindigs

While in game you can move around your cursor using vim-bindings hjkl. To move a piece you select the piece you want to move using "c", select which square you want to move to using "x" and make the move using "m"


### Running a game
##### Run game with env variables

###### __Create .env file__

```
cp .env.example .env
```

_edit .env with your own settings_

###### __Start game__
```
pipenv run game_with_env <game_id>
```


##### Run game with config file

###### __Create configuration file__
```
cp config.yml.example config.yml

```
_edit config.yml and set either and set either:_ `api_key_cmd` _or_ `api_key`.

###### __Start game__
```
pipenv run game <game_id>
```
