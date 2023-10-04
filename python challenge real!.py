import random
import time
from colorama import Fore

def main():
    print(Fore.CYAN + "GUESS THE MUSIC GENRE")
    print("---------------------")
    print("")
    name = input(Fore.BLUE + "Please enter your name: ")
    print(Fore.CYAN + "Welcome, " + name)

    genre = [
        "Jazz",
        "HipHop",
        "Pop",
        "Rock",
        "Rap",
        "Latin",
        "Hindi",
        "Classic",
    ]

    x = random.choice(genre)
    guess = None
    start_time = time.time()  # Record the start time
    time_limit = 20  # Set the time limit (in seconds)

    while x != guess:
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        remaining_time = time_limit - elapsed_time  # Calculate remaining time
        
        if remaining_time <= 0:
            print("\nTime's up! You didn't guess in time.")
            break

        guess = input(Fore.BLUE + f"Guess the music genre ({remaining_time:.1f} seconds left): ")
        
        if x.lower() == guess.lower():
            print(Fore.GREEN + f"\nCongratulations, you got it right in {elapsed_time:.2f} seconds!")
            break
        else:
            print(Fore.RED + "\nUnfortunately, you got the wrong answer. Please try again!")

    print('Game over!')
    print("The correct answer is", x)

if __name__ == "__main__":
    main()
