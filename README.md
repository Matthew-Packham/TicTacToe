# TicTacToe
Python implementation of TicTacToe. Includes a genius AI player, who never loses!

The implementation includes two .py files. player_class.py (which contains all the Player classes and attributes - The different players inherit from the super class Player) and the game_class.py (which contains the TicTacToe class which contains all then neccesary methods to run the game).

The 'Genius AI' is based on the MinMax Algorithm.

### What is Minimax?
Minimax is a artificial intelligence applied in two player zero sum games, such as tic-tac-toe, checkers, chess and go. These games are known as zero-sum games, since either one player wins (+1) and other player loses (-1) or neither win (0).

### How does it works?
The algorithm searches recursively, for the 'best' move - the move that given the current state maximises the utility of the 'Max' player and minimises the utility of the 'Min' player. The utility function is U = 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)


t consider the current state of the game and the available moves at that state, then for each valid move it plays (alternating *min* and *max*) until it finds a terminal state (win, draw or lose).

### Understanding the Algorithm
The algorithm was studied by the book Algorithms in a Nutshell (George Heineman; Gary Pollice; Stanley Selkow, 2009). Pseudocode (adapted):

```
minimax(state, depth, player)

	if (player = max) then
		best = [null, -infinity]
	else
		best = [null, +infinity]

	if (depth = 0 or gameover) then
		score = evaluate this state for player
		return [null, score]

	for each valid move m for player in state s do
		execute move m on s
		[move, score] = minimax(s, depth - 1, -player)
		undo move m on s

		if (player = max) then
			if score > best.score then best = [move, score]
		else
			if score < best.score then best = [move, score]

	return best
end
```

## Installation

Clone the repo
```sh
git clone https://github.com/Matthew-Packham/TicTacToe.git
```
## Usage
In game_class.py file there are two options. Either play a single game or iterate over a number of games. 

To play against computer just uncomment the str (at bottom of code) and choose your players (be sure to comment option 2).

run
```sh
python3 game_class.py
```
## Human vs Genius
![](Human%20Vs%20Genius.png)

## Genius vs Genius
![](Genius%20Vs%20Genius.png)
