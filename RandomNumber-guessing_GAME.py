import random

Cnumber = random.randrange(1,102)
max_attempts = 3
attempts = 0
print("Welcome to random number guessing game!")

while attempts < max_attempts:

  userinput = int(input('Enter a number b/w 1-100 :'))

  if userinput == Cnumber :
        print("Congratulations...You have guessed the correct number!")
  else:
      print("Incorrect guess...Please try again.")  
      attempts+=1

      if attempts == 1 :
          print(f"You have only {max_attempts-attempts} attempts to guess a number..")
         
          if userinput<Cnumber:
              print("Hint: Gues any higher number... ")  
          else:
              print("Hint: Guess any lower number") 
      elif  attempts == 2:
          print(f"You have only {max_attempts-attempts} attempts to guess a number..")
          if userinput<Cnumber:
              print("Hint: Gues any higher number... ")  
          else:
              print("Hint: Guess any lower number") 

print("Oops You have lost the game ..") 
print(f"The correct number was :{Cnumber}")           
              


   
