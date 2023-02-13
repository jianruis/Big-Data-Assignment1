# Program Structure
My code contains the following classes:
+ Card class, used to represent a card. Each card has a suit, a rank and a used flag.
+ Player class, used to represent a player. Each player has a list of cards, a name and a score.
+ Game class, used to represent the game. It contains a list of players.
And a main function to start the game.

## Function of each class
### Card class
The Card class has the following methods:
+ ``__init__`` Constructor, used to init the suit, rank and used flag of the card.
+ ``__str__``  used to print the card.
+ ``__repr__`` used to print the card directly.
+ ``__gt__`` used to compare the rank of two cards.
+ ``__lt__`` used to compare the rank of two cards.

### Player class
The Player class has the following methods:
+ ``__init__`` Constructor, used to init the cards, name and score of the player.

### Game class
The Game class has the following methods:
+ ``__init__`` Constructor, used to init the players of the game.
+ ``move`` used to get the card that the player chooses from terminal.
+ ``get_winner`` used to get the winner of the game.
+ ``round`` used to play a round of the game.
+ ``start`` used to start the game.

The main function will create a game object and start the game.