# Hangman Game

A Python implementation of the classic Hangman word guessing game.

## Description

This Hangman game randomly selects words from three different categories:
- Cars
- Animals
- Fruits/Vegetables

The player has 7 attempts to guess the word by entering one letter at a time. The game features a visual representation of the hangman that progressively appears with each incorrect guess.

## How to Play

1. The first letter of the word is revealed; the rest are hidden as underscores.
2. You have 7 attempts to guess the word by entering one letter at a time.
3. Each correct guess reveals all occurrences of that letter.
4. Each wrong guess draws one more part of the hangman and reduces your remaining attempts.
5. If you guess all the letters before using up all attempts, you win!
6. If you use all 7 wrong guesses, the game is over and you lose.

## Features

- Multiple word categories
- Visual hangman representation
- Score tracking
- User-friendly menu system

## Files

- `hangmantrue.py`: Main game file
- `int.txt`: Instructions file

## Author

Created by Karthik