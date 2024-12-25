import random 

number1,number2 = sorted(map(int, input("Please enter 2 numbers to chose the range: ").split()))
random_number =random.randint(number1,number2)


try:
    while True:  
        is_guessed = int(input("Please enter your prediction: "))
        
        if not number1 <= is_guessed <= number2:
           print("Please enter a number from the range you specified:")
           continue

        if is_guessed > random_number:
           print("Enter more small number:")
        elif is_guessed < random_number:
           print("Enter more big number:")
        else:
           print("You are right :)")
           break
except ValueError:
    print("Please enter a number !")


"""
Created By: Aytuğ Yürük

"""