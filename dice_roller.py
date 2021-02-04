
def main():
  import random
  dice_rolls=2
  dice_sum=0
  for i in range (0, dice_rolls):
    roll=random.randint(1,6)
    dice_sum+=roll
    if roll==1:
      print(f'Siiiiick!{roll}')
    elif roll==6:
      print(f'Crazy mudda!{roll}')      
    else:
      print(f'You rolled a {roll}')
  print(f'Your total:{dice_sum}')
  
  

if __name__== "__main__":
  main()
