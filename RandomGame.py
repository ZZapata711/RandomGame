# This program will choose a random game from a separate text file and return it to the user
import random

# Generate a list of games from the contents of the text file
games_list = []
with open("games.txt", "r") as games:
    for game in games:
        games_list.append(game.rstrip())


# Allow user to add game to list
def add_game():
    new_game = input("Name of game to be added: ")
    games_list.append(new_game)
    with open("games.txt", "w") as games:
        for game in games_list:
            print(game, file=games)

# Allow user to remove game from list
def remove_game():
    for game in games_list:
        print(game)
    removed_game = input("Name of game to be removed: ")
    games_list.remove(removed_game)
    with open("games.txt", "w") as games:
        for game in games_list:
            print(game, file=games)


# Allow user to view list of games
def view_games():
    for game in games_list:
        print(game)


# Choose random game and return to user
def random_game():
    rand_int = random.randint(0, len(games_list)-1)
    print("Your selected game is {}".format(games_list[rand_int]))


def main():
    while True:
        print("1: View Games")
        print("2: Add Game")
        print("3: Remove Game")
        print("4: Choose Random Game")
        print("Q: Exit Program")
        choice = input("What would you like to do?: ")
        if choice == "Q" or choice == "q":
            break
        elif int(choice) == 1:
            print("="*20)
            view_games()
            print("=" * 20)
            continue
        elif int(choice) == 2:
            add_game()
            continue
        elif int(choice) == 3:
            remove_game()
            continue
        elif int(choice) == 4:
            print("="*20)
            random_game()
            print("="*20)
            continue
        else:
            print("Invalid input")
            continue


main()

