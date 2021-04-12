# Fireball-Game
"Fireball" game in python

INSTRUCTIONS:

There can be several rounds in this game. In each round, the player can:

1 - Charge (Build up charge required for other moves)
2 - Block  (Blocks all attacks)
3 - Attack (Use one of several attacks to eliminate the other player)

Different attacks require different amounts of charge. If both players attack, then the one with the stronger attack wins.

The game ends if either player gets eliminated by an attack.


ENEMY BOT (PLAYER 2):

The enemy bot will choose to eliminate the player if victory is assured. This happens in the case where the bot has enough charge to attack and the player does not have enough charge to block.

The enemy bot will choose to charge if it cannot attack and the player is unable to attack as well. 


OBJECTIVE:

Predict the actions of your enemy and make the best move to counter them. Try surviving long enough while collecting charge to test out your strongest attacks.


OTHER NOTES:

Flexibility: The main aspect of this implementation of the "Fireball" game is the ability to add new attacks. Make your own custom version of the game to play simply by editing the list of attacks.
