import random
min= int(input("enter minumum num :"))
max = int(input('enter maximum number :'))
target_number = (int(input("enter your guessing number :")))
reward = 0
guess = random.randint(min,max)
if target_number == guess:
  print('congratulations your guessing number is right')
  reward +=1
else:
  print("no thats not a right number")
  reward -=1
reward = reward
print( 'reward = ' , reward)
