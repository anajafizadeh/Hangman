from __future__ import annotations
import Words
import random


class Hangman:
    """
    The famous hangman game.
    Given a specific number of attempts the player should guess
    a random word selected by AI. In each attempt, the similar
    letters of User's input and the selected word will be pointed out.

    === Attributes ===
    num_attempts:
        The number of guesses user can make.
    word_length:
        The length of the word.
    player:
        The player.
    word:
        Player's guess.
    goal:
        AI word.
    bash:
        Unrevealed word.

    === Representation Invariants ===
    -   1 <= num_attempts <= 25
    -   word_length >= 4
    """
    num_attempts: int
    word_length: int
    player: Player
    guessed_letters: int
    word: str
    goal: str
    bash: list

    def __init__(self, num_attempts: int, word_length: int, player: Player,
                 goal: str) -> None:
        self.num_attempts = num_attempts
        self.word_length = word_length
        self.player = player
        self.guessed_letters = 0
        self.word = ''
        self.goal = goal
        self.bash = ['-'] * len(self.goal)

    def play(self):
        """ Play one round of this game."""

        while self.word != self.goal and self.num_attempts > 0:
            self.play_one_turn()

        if self.word == self.goal:
            winner = self.player
            return winner.name
        else:
            print('Game over!')
            print(f'Answer is: {self.goal}')

    def play_one_turn(self):
        """ Play a single turn of this game. """
        self.num_attempts -= 1
        guessed = self.player.move()
        if len(guessed) != len(self.goal) and len(guessed) > 1:
            self.num_attempts += 1
            print('Invalid input')
        self.word = guessed
        i = -1
        for letter in self.goal:
            i += 1
            if letter in self.word:
                self.guessed_letters += 1
                self.bash[i] = letter
        print(f'Attempts left: {self.num_attempts}')
        print(''.join(self.bash))


class Player:
    """Makes a player.
    === Attributes ===
    name:
        Player's name.
    """
    name: str

    def __init__(self, name: str):
        self.name = name

    def move(self):
        guessed = input(f'{self.name} turn, ')
        return guessed


def make_player(generic_name: str) -> Player:
    """Returns a Player based on user input."""
    name = input(f'Enter a name for {generic_name}: ')
    return Player(name)


def mode():
    print('1. Cars \n'
          '2. Countries\n'
          '3. Names\n'
          '4. Soccer clubs\n'
          '5. Random nouns')
    mode = input(f'Enter a category number: ')
    goal = ''
    if mode == '1':
        goal = Words.car_selector()
    elif mode == '2':
        goal = Words.country_selector()
    elif mode == '3':
        goal = Words.name_selector()
    elif mode == '4':
        goal = Words.club_selector()
    elif mode == '5':
        goal = Words.random_selector()
    return goal.lower()


def main() -> None:
    goal = mode()
    length = len(goal)
    print(f'Word length: {length}')
    attempts = int(
        input(f'Select a number from 1 to 25 as the allowed chances: '))
    p1 = make_player('p1')
    g = Hangman(attempts, length, p1, goal)
    winner = g.play()
    if winner is not None:
        print(f'And {winner} is the winner!!!')
    #print(p1)
    again = input('Again? (y/n) ')
    if again == 'y':
        return main()


if __name__ == '__main__':
    main()
