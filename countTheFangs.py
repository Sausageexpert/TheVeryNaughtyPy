import random
rand = random.randint(1, 9)
chances = 5

guess = int(input("How Many Supporters Does Mr. Py Have In The Parliament! (In Thousands) "))

while chances > 0:
   if guess < rand:
      print("Come on! Mr. Py's pretty popular!")
      break
   if guess == rand:
      print("Yep, that's correct!")
      break
   if guess > rand:
      print("Woah, Parliament doesn't even have that many people!")
      break
   
chances = chances - 1
   
   #Please work?