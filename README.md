# Scrabble
This is a Python implementation of the game Scrabble
The game will start with a blank board, the game is continuing until the bag of tiles isn't empty and a word can be added.
Currentlly it is adapted only for one player.

We use standart rules:
The first player (the  must play his or her first word on the center square of the board, the spot that has a ‘star’ on it. All words must be two or more letters long. Words are played either vertically or horizontally. Diagonal word play is not permitted.
Player must play off of words already present on the board. This may involve changing existing words (for example, making the word ‘play’ into ‘player’) or by incorporating a letter into the word you are playing. You may only place letters in a straight line horizontally or vertically. You can place letters in both directions on a single turn. The letters placed must form complete words. Anytime two or more letters touch, they must form valid, legal words. For example, if you add an ‘s’ to an existing word to make it a plural and then build a separate word from that ‘s’ in the opposite direction, you would get full credit for both words. No tile can be moved or shifted once it is played (baring a successful challenge). 

For computer strategy we use greedy algorithm
