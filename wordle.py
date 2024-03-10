import sys

WoD = sys.argv[1].lower()
counter = 0

while counter < 6:
    guess = input("Please enter a five letter word: ").lower()
    counter += 1

    if len(guess) != 5:
        print("The length of the word must be five!")
        continue

    if guess == WoD:
        print(f"Congratulations! You guessed right in {counter} try!")
        break

    for i in range(5):
        if guess[i] == WoD[i]:
            print(f"{i+1}. letter exists and is located in the right position.")
        elif guess[i] in WoD:
            print(f"{i+1}. letter exists but is located in the wrong position.")
        else:
            print(f"{i+1}. letter does not exist.")

print("You failed!")
