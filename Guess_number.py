import random as rd

l=rd.randint(0,20)  #Generate a random number in range --> 0 to 20 
print(l)
i=0
while(i<=2):
    
    n=int(input('Guess a number between 0 and 20'))
    
    
    
    if n==l:
        print('Yay!! You guessed it right')   
        break                   #Come out if guessed right
    elif n-l in range(4,19):
        print('Ur guess is too high')
    elif n-l in range(-19,-4):
        print('Ur guess is too low')
    elif n-l in range(0,4):
        print('Ur guess is high')
    elif n-l in range(-3,0):
        print('Ur guess is low')
    
    if i>=2:        # 3 Chances
        print('Sorry!!..You ran out of chances')     
        break
    
    i+=1