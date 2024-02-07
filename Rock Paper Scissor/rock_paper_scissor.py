import random
user_choice=int(input("Enter your choice:type 0 for Rock,1 for Paper,2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
    print("you entered a invalid number,User Lose.")
else:
  computer_choice=random.randint(0,2)
  print("Computer Choice:")
  print(computer_choice)
  if computer_choice == user_choice:
    print("It is draw")    
  elif computer_choice == 0 and user_choice ==2 :
    print("user Lose") 
  elif user_choice == 0 and computer_choice == 2 :
    print("User win")       
  elif computer_choice > user_choice: 
    print("user Lose")
  elif user_choice > computer_choice :
    print("User Win")
print("Thanks For Playing!")       
      

