## To be able to play lichess in the terminal you will need to create an API key [here](https://lichess.org/account/oauth/token) 

To be able to play using this program you will first have to create an API [here](https://lichess.org/account/oauth/token)

When you have your api key an option is to create a pass entry and export it as done in [.env.example file](.env.example)

For now you will have to put the game id into both [game.py](game.py) (line 13) and [src/terminal.py](/src/terminal.py) (line 11) once that is done you will be able to launch game.py.

While in game you can move around your cursor using vim-bindings (hjkl). To move a piece you select the piece you want to move using "c", select which square you want to move to using "x" and make the move using "m"
