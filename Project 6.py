import random
import string
print("Gerador de Senhas")
print("--------------------------")

def password_generator(len_pass = 8):
    
    ascii_options = string.ascii_letters
    numb_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + numb_options + punt_options
    user_password = ""
    
    for i in range(0, len_pass):
        digit = random.choice(options)
        user_password = user_password + digit
    return user_password

while True:
        user_choice = input("\nDigite o número de caractéres da senha: ")
        
        if user_choice.isdigit():
            user_choice = int(user_choice)
            break
        else:
            print("Valor inválido. Por favor digite um número.") 
            continue

print(f"Senha gerada: {password_generator(len_pass=user_choice)}")