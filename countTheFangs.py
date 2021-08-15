import random
rand = random.randint(1, 9)
chances = 5



while chances > 0:
   guess = int(input("How Many Supporters Does Mr. Py Have In The Parliament! (In Thousands) "))
   if guess < rand:
      print("Come on! Mr. Py's pretty popular!")
      
   elif guess == rand:
      print("Yep, that's correct!")
      break
      
   else:
      print("Woah, Parliament doesn't even have that many people!Try again")
   chances = chances - 1
      
   #Please work?
   
    
