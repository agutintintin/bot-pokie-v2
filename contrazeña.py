import random

def llave (long):
    
    digitos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    pasword = ""

    for i in range( long ):
        pasword += random.choice(digitos)

    return pasword  
