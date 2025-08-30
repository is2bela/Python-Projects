import random
import time

print("Seja bem vindo ao Jo-Ken-Po Virtual!")
print("Jogue pedra, papel e tesoura contra o computador e teste sua sorte!")
start_prompt = ""

while start_prompt.lower() != "sim":
    start_prompt = input("\nEstá pronto para começar? \nSim/Não: ").lower()

    if start_prompt.lower() == "sim":
        user_nick = input("\nDigite o seu nome: ")
        print("\nPerfeito, vamos começar!")
        break
    elif start_prompt.lower() == "não":
        print("Tudo bem, você pode voltar quando quiser!")
    else:
        print("Não entendi, por favor responda com Sim ou Não.")

plays = ["pedra", "papel", "tesoura"]

user_points = 0
pc_points = 0 
repeat_prompt = "sim" 

while repeat_prompt == "sim":
    pc_choice = random.choice(plays)
    user_choice = input("\nPedra, papel ou tesoura? ").lower()

    print(user_nick +":", user_choice)
    time.sleep(1)
    print("X")
    time.sleep(1.2)
    print("Computador" + ":", pc_choice)
    time.sleep(1)

    if user_choice == pc_choice:
        print("\nAhh, empate! Tente novamente.")
    elif (user_choice == "pedra" and pc_choice == "tesoura") or \
        (user_choice == "papel" and pc_choice == "pedra") or \
        (user_choice == "tesoura" and pc_choice == "papel"):
        user_points = user_points + 1 
        print("\nUhuu! Você venceu!")
    else:
        pc_points = pc_points + 1
        print("\nOps, o computador ganhou...")
    
    repeat_prompt = input("\nJogar de novo? \nSim/Não: ").lower()

    if repeat_prompt == "não" or "nao":
        print("\nAté a próxima!")
        print(f"\nPontos\n{user_nick}: {user_points}\nComputador: {pc_points}")
    elif repeat_prompt != "sim":
        print("Não entendi, por favor responda com Sim ou Não.")
