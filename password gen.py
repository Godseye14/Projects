import random 
import string 

def password_gen3():
    """
    This program allows user to choose length of the password,
    how many digits,uppercase,lowercase,special chars
    the user needs in his password
    ..Final implementation..
    """
    try:
        n=int(input('Length of the password(Min length 6) ??'))
        if n<6:
            raise ValueError('Less than 6,so by default length=6')
        
    except ValueError as ve:
        print(ve)
    
    finally:
        if n<6:
            n=6
    try:
        n1=int(input('Min digits?'))
        if n1>n:
            raise ValueError('Exceeds length')
    except ValueError as ve:
            print(ve)
    finally:                                                  #if it exceeds length,then init. n1 to zero
        if n1>n:
            n1=0
            
    try:
        n2=int(input('Min special chars?'))
        if n2>(n-n1):
            raise ValueError('Exceeds length')
    except ValueError as ve:
            print(ve)
    finally:                                                 #if it exceeds length,then init. n2 to zero
        if n2>n-n1:
            n2=0
    
    try:
        n3=int(input('Min lowercase?'))
        if n3>(n-(n1+n2)):
            raise ValueError('Exceeds length')
    except ValueError as ve:
            print(ve)
    
    finally:                                                 #if it exceeds length,then init. n3 to zero
        if n3>n-n1-n2:
            n3=0
    
    try:
        n4=int(input('Min Uppercase?'))
        if n4>(n-(n1+n2+n3)):
            raise ValueError('Exceeds length')
    except ValueError as ve:
            print(ve)
    
    finally:                                                #if it exceeds length,then init. n4 to zero
        if n4>n-n1-n2-n3:
            n4=0
    
    total=n1+n2+n3+n4
    password=''
    random_string = string.ascii_letters + string.digits
    
    for i in range(n1):
        password+=random.choice(string.digits)
    for i in range(n2):
        password+=random.choice(string.punctuation)
    for i in range(n3):
        password+=random.choice(string.ascii_lowercase)
    for i in range(n4):
        password+=random.choice(string.ascii_uppercase)
    
    for i in range(n-total):                                   #randomnly generate rest of the chars
        password+=random.choice(random_string)
        
    passw=list(password)
    random.SystemRandom().shuffle(passw)
    password=''.join(passw)
    
    return password 