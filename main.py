import requests
import pyjokes
from art import *
import tableprint as tp
import random


def interface():
    command = input("""Select from menu:
    1 - Advice Movie
    2 - Advice Music
    3 - Play Games
    4 - Get Joke
    5 - Get Quote from Kanye West
    6 - Get Art by Theme
    : """)
    match command:
        case '1': movie_advice()
        case '2': music_search()
        case '3': play_game()
        case '4': get_joke()
        case '5': get_quote()
        case '6': get_art()
        case _: 'sorry...not available. Try again'


def get_art():
    theme = input('What shall it be like: ')
    try:
        print(art(theme))
    except artError:
        print('it was too difficult🐒 maybe try "coffee" instead 😉')


def get_joke():
    joke = pyjokes.get_joke('en', 'all')
    print(joke)


def get_quote():
    response = requests.get(url='https://api.kanye.rest/')
    response.raise_for_status()
    data = response.json()
    quote = data['quote']
    print('Kanye says:', quote)


def play_game():
    game = input("""Choose Game:
    1 - Tic-Tac-Toe
    2 - Guess the Number
    3 - Rock Paper Scissors
    4 - Hangman
    : """)
    match game:
        case '1': tic_tac_toe()
        case '2': guess_number()
        case '3': rock_paper_scissors()
        case '4': hangman()
        case _: 'sorry, we dont have this one 🤔'


def tic_tac_toe():
    tp.banner("Welcome to Tic-Tac-Toe! Let's play!")
    table_grid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    tp.table([table_grid[0:3], table_grid[3:6], table_grid[6:]], style='round')
    steps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    game = []
    comp_game = []
    win_combinations = (['a', 'd', 'g'],
                        ['b', 'e', 'h'],
                        ['c', 'f', 'i'],
                        ['a', 'b', 'c'],
                        ['d', 'e', 'f'],
                        ['g', 'h', 'i'],
                        ['a', 'e', 'i'],
                        ['c', 'e', 'g'])
    continue_game = True

    def step():
        global steps
        next_step = input('Your turn! Write a letter of your step: ')
        for i in range(len(table_grid)):
            if table_grid[i] == next_step:
                table_grid[i] = '✖'
                tp.table([table_grid[0:3], table_grid[3:6], table_grid[6:]], style='round')
        if next_step in steps:
            steps.remove(next_step)
            game.append(next_step)
            game.sort()
            print(game[:3])
        else:
            print('This is not available. Try again!')

    def computer_step():
        global steps
        next_comp_step = random.choice(steps)
        for i in range(len(table_grid)):
            if table_grid[i] == next_comp_step:
                table_grid[i] = '◎'
                tp.table([table_grid[0:3], table_grid[3:6], table_grid[6:]], style='round')
        steps.remove(next_comp_step)
        comp_game.append(next_comp_step)
        comp_game.sort()
        print(f'computer steps: {comp_game[:3]}')

    step()

    while continue_game:
        if game[:3] in win_combinations:
            continue_game = False
            print('You Won!')
        elif comp_game in win_combinations:
            continue_game[:3] = False
            print('You Lost 😟 ')
        else:
            computer_step()
            step()


def guess_number():
    number = random.randint(0, 9)
    while True:
        user_number = input('Make a guess: ')
        if not user_number.isdigit():
            print('it shall be a number ;)')
        else:
            user_number = int(user_number)
            if user_number < number:
                print('Its too low')
            elif user_number > number:
                print('Its too hight')
            else:
                print('You got it!')
                break


def hangman():
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    word_list = ["ardvark", "baboon", "camel"]
    game_is_finished = False
    lives = len(stages) - 1

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    display = []
    for _ in range(word_length):
        display += "_"

    while not game_is_finished:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                game_is_finished = True
                print("You lose.")

        if not "_" in display:
            game_is_finished = True
            print("You win.")

        print(stages[lives])

def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    choises = [rock, paper, scissors]
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    if choice not in ['0', '1', '2']:
        print("please use correct command")
    else:
        choice = int(choice)
        print(f"your step: {choises[choice]}")

        computer_choice = random.randint(0, 2)
        print(f"computer step: {choises[computer_choice]}")

        if choice == computer_choice:
            print("try again")
        elif choice == 0 and computer_choice == 2:
            print("you won!")
        elif choice == 1 and computer_choice == 0:
            print("you won!")
        elif choice == 2 and computer_choice == 1:
            print("you won!")
        else:
            print("you lost")


def music_search():
    row_search = input('what music would you like to find: ')
    search = row_search.replace(' ', '%20')
    link = f'https://open.spotify.com/search/{search}'
    print(f'Please follow this link: {link}')


def movie_advice():
    row_search = input('what kind of movie would you like to find: ')
    search = row_search.replace(' ', '+')
    link = f'https://www.themoviedb.org/search?query={search}'
    print(f'Please follow this link: {link}')
    'https://www.themoviedb.org/search?query={search}'

while True:
    print()
    interface()
