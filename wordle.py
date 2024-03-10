import sys                                             # To provide the (WoD) as command-line argument.
WoD = sys.argv[1]
counter = 0

for i in range(0, 6):                                  # To provide six guesses thanks to variable p .
    p = input("Please enter a five letter word: ")     # To enter a guesses.
    counter = counter+1                                #

    if len(p) != 5:                                    # To determine if the length of the word is 5 or not.
        print("The length of WoD must be five!")
    else:
        if p == WoD:                                   # To check the accuracy of the prediction.
            print("Congratulations! You guess right in " + str(counter)+"th shot!")
            exit()                                     # To stop program if the prediction is accuracy.

        else:                                          # To check the accuracy of the word letter by letter.
            if p[0] == WoD[0]:                         # To check first letter.
                print("1. letter exists and located in right position.")
            elif p[0] == WoD[1]:
                print("1. letter exists but located in wrong position.")
            elif p[0] == WoD[2]:
                print("1. letter exists but located in wrong position.")
            elif p[0] == WoD[3]:
                print("1. letter exists but located in wrong position.")
            elif p[0] == WoD[4]:
                print("1. letter exists but located in wrong position.")
            else:
                print("1. letter does not exist.")

            if p[1] == WoD[1]:                          # To check second letter.
                print("2. letter exists and located in right position.")
            elif p[1] == WoD[0]:
                print("2. letter exists but located in wrong position.")
            elif p[1] == WoD[2]:
                print("2. letter exists but located in wrong position.")
            elif p[1] == WoD[3]:
                print("2. letter exists but located in wrong position.")
            elif p[1] == WoD[4]:
                print("2. letter exists but located in wrong position.")
            else:
                print("2. letter does not exist.")

            if p[2] == WoD[2]:                          # To check third letter.
                print("3. letter exists and located in right position.")
            elif p[2] == WoD[0]:
                print("3. letter exists but located in wrong position.")
            elif p[2] == WoD[1]:
                print("3. letter exists but located in wrong position.")
            elif p[2] == WoD[3]:
                print("3. letter exists but located in wrong position.")
            elif p[2] == WoD[4]:
                print("3. letter exists but located in wrong position.")
            else:
                print("3. letter does not exist.")

            if p[3] == WoD[3]:                           # To check fourth letter.
                print("4. letter exists and located in right position.")
            elif p[3] == WoD[0]:
                print("4. letter exists but located in wrong position.")
            elif p[3] == WoD[1]:
                print("4. letter exists but located in wrong position.")
            elif p[3] == WoD[2]:
                print("4. letter exists but located in wrong position.")
            elif p[3] == WoD[4]:
                print("4. letter exists but located in wrong position.")
            else:
                print("4. letter does not exist.")

            if p[4] == WoD[4]:                           # To check fifth letter.
                print("5. letter exists and located in right position.")
            elif p[4] == WoD[0]:
                print("5. letter exists but located in wrong position.")
            elif p[4] == WoD[1]:
                print("5. letter exists but located in wrong position.")
            elif p[4] == WoD[2]:
                print("5. letter exists but located in wrong position.")
            elif p[4] == WoD[3]:
                print("5. letter exists but located in wrong position.")
            else:
                print("5. letter does not exist.")

print("You are failed!")                                 # To report failing when all predictions are wrong.
