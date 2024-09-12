import random

def main():
    print("Rock-Paper-Scissors!")
    choices = {
        "0": "Rock",
        "1": "Paper",
        "2": "Scissors"
    }
    while True:
        while True:
            user_input = input("Enter your choice (0 is Rock, 1 is Paper, 2 is Scissors): ")
            if user_input in choices:
                break
            else:
                print("Invalid input. Please enter '0', '1', or '2'")
        user_choice = choices[user_input]
        cmp_ip = str(random.randint(0, 2)) 
        cmp_choice = choices[cmp_ip]

        win_cd = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }

        if win_cd[user_choice] == cmp_choice:
            print(f"You win! {user_choice} beats {cmp_choice}")
        elif user_choice == cmp_choice:
            print(f"It's a tie! Both chose {user_choice}")
        else:
            print(f"Computer wins! {cmp_choice} beats {user_choice}")

        again = input("Play again? (Y/N): ").lower()
        if again != "y" and again != "n":
            print("Invalid input. Please enter 'Y' or 'N'.")
        elif again != "y":
            print("Thanku!")
            break

if __name__ == "__main__":
    main()