import random

print("Seja bem vindo ao O Número Oculto!")
print("Tente adivinhar o número secreto no menor número de tentativas possível!")
start_prompt = ""

while start_prompt.lower() != "sim":
    start_prompt = input("\nEstá pronto para começar? \nSim/Não: ").lower()

    if start_prompt.lower() == "sim":
        print("\nPerfeito, vamos começar!")
        break
    elif start_prompt.lower() == "não":
        print("Tudo bem, você pode voltar quando quiser!")
    else:
        print("Não entendi, por favor responda com Sim ou Não.")

while True:
    max_num =  input("\nDigite o número teto do desafio: ")

    if max_num.isdigit():
        max_num = int(max_num)
        break
    else:
        print("Erro: valor informado não é numérico. Tente novamente.")

random_num = random.randint(0, max_num)
user_guess = 0
counter = 0

while True:
    user_guess = input("Advinhe o número: ")
    counter = counter + 1

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Erro: valor informado não é numérico. Tente novamente.")

    if user_guess == random_num:
        print("Você acertou, parabéns!")
        print("Número de tentativas:", counter)
        break
    elif user_guess > random_num:
        print("Chutou alto. O número aleatório é menor que isso...")
    elif user_guess < random_num:
        print("Chutou baixo. O número aleatório é maior que isso...")