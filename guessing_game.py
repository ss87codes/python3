"""
This game allows the user to guess names from a list. The user
"""

list_to_be_guessed = ["sho","gar","dd"]
guess = ""
chance_count = 0
correct_guess_count = 0
total_to_be_guessed = list_to_be_guessed.__len__()
total_chances = total_to_be_guessed + 3

print("You have to guess %d names and have %d chance" %(total_to_be_guessed,total_chances))

while correct_guess_count!=total_to_be_guessed and chance_count<total_chances:

    user_guess = input("Please enter the name: ")
    chance_count += 1
    if user_guess in list_to_be_guessed:
        correct_guess_count += 1
        remaining = total_to_be_guessed - correct_guess_count
        if remaining>0:
            print("thats right. %d more to be guessed correctly" %remaining)
        else:
            print("You win")
    else:
        remaining = total_to_be_guessed - correct_guess_count
        print("Try again. you have %d to be guessed and %d chance remaining" %(remaining,total_chances-chance_count))

