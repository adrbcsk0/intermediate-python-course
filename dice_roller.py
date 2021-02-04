
def main():
  import random
  dice_rolls=int(input('How many rolls?  '))
  dice_sum=0
  dice_size=int(input('How big is your dice?  '))
  for i in range (0, dice_rolls):
    roll=random.randint(1,dice_size)
    dice_sum+=roll
    if roll==1:
      print(f'Siiiiick! Its a {roll}')
    elif roll==dice_size:
      print(f'Crazy mudda! Its a {roll}')      
    else:
      print(f'You rolled a {roll}')
  print(f'Your total:{dice_sum}')
  
  

if __name__== "__main__":
  main()
