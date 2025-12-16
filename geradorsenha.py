import random

def pass_gen(size):
    caracteres = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    senha = ""
    for _ in range(size):
        senha += random.choice(caracteres)
    return senha