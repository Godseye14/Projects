import random as rd

"""
Rock , Paper , Scissor Game
"""
    
c=['Rock','Scissor','Paper']
    
i=0
while i<3:
        
    computer = rd.choice(['Rock','Paper','Scissor']) #randomnly choose one 
        
    print(computer)  #to verify if output is correct
        
    user = input('Enter Rock / Paper / Scissor : ')  #Get input from User
         
    if user in c:
        pass
    else:
        print('Wrong input')
            
    if user=='Rock':
        if computer=='Paper':
            print('Computer won')
        elif computer=='Scissor':
            print('User won')
       
    if user=='Paper':
        if computer=='Scissor':
            print('Computer won')
        elif computer=='Rock':
            print('User won')
        
    if user=='Scissor':
        if computer=='Rock':
            print('Computer won')
        elif computer=='Paper':
            print('User won')
        
    if computer==user:
        print('There was a Draw')
            
        
    i+=1