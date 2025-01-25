import random



random_num = random.randint(1, 100)
attempts = 0
guessed = False

while not guessed:
        user_guess = int(input("Enter your guess(Note:After 10 failed attempts,the number will be revealed.): "))
        attempts += 1


        if user_guess < random_num:
            print("You're too low.")
        if user_guess > random_num:
            print("You're too high.")
        if user_guess == random_num:
            print(f"Congratulations! you have guessed the number in {attempts} attempts!")
        


            if attempts == 10:
                print(f"The number is {random_num}")
                
            
               
    

  
      
















print(random_num)