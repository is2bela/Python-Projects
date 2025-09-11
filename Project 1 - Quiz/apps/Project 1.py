print("Seja bem vindo ao Quiz do Mundo!")
print("\nDescubra o quanto você sabe sobre o nosso planeta em 10 perguntas.")

start_prompt = ""
score = 0 

while start_prompt.lower() != "sim":
    start_prompt = input("\nEstá pronto para começar? \nSim/Não: ").lower()

    if start_prompt.lower() == "sim":
        print("\nPerfeito, vamos começar!")
        break

    elif start_prompt.lower() == "não":
        print("Tudo bem, você pode voltar quando quiser!")
        

    else:
        print("Não entendi, por favor responda com Sim ou Não.")

#pergunta 1
print("\nPergunta 1 \nQual é o maior planeta do sistema solar?\na) Marte\nb) Júpiter\nc) Saturno")
answer1 = input("\nResposta: ")

if answer1.lower() == "b":
    print("Correto!")
    score = score + 1
else: 
    print ("\nIncorreto!")
    print ("Júpiter é o maior planeta do Sistema Solar, com cerca de 142.984 km de diâmetro, mais de 11 vezes o tamanho da Terra.")

#pergunta 2
print("\nPergunta 2 \nQual é o planeta mais próximo do Sol?\na) Mercúrio\nb) Vênus\nc) Marte")
answer2 = input("\nResposta: ")

if answer2.lower() == "a":
    print("Correto!")
    score = score + 1
else: 
    print ("\nIncorreto!")
    print ("Mercúrio orbita o Sol a uma distância média de 57,9 milhões de km, sendo o planeta mais próximo da estrela.")

#pergunta 3 
print("\nPergunta 3 \nQual é o menor continente em área?\na) Europa\nb) Oceania\nc) América Central")
answer3 = input("\nResposta: ")

if answer3.lower() == "b":
    print("Correto!")
    score = score + 1
else: 
    print ("\nIncorreto!")
    print ("Oceania é o menor continente, com cerca de 8,5 milhões km², sendo menor que a Europa (10,2 milhões km²).")

#pergunta 4 
print("\nPergunta 4 \nQuantos oceanos existem na Terra?\na) Quatro\nb) Cinco\nc) Seis")
answer4 = input("\nResposta: ")

if answer4.lower() == "b":
    print("Correto!")
    score = score + 1
else: 
    print ("\nIncorreto!")
    print ("Existem cinco oceanos na terra: Pacífico, Atlântico, Índico, Ártico e Antártico.")

#pergunta 5 
print("\nPergunta 5 \nQuantos continentes existem na Terra?\na) Cinco\nb) Seis\nc) Sete")
answer5 = input("\nResposta: ")

if answer5.lower() == "c":
    print("Correto!")
    score = score + 1
else: 
    print ("\nIncorreto!")
    print ("Existem sete continentes na terra: África, América do Norte, América do Sul, Antártida, Ásia, Europa e Oceania.")

#pergunta 6 
print("\nPergunta 6 \nQual é a língua mais falada no mundo?\na) Inglês\nb) Espanhol\nc) Mandarim")
answer6 = input("\nResposta: ")

if answer6.lower() == "c":
    print("Correto!")
    score = score + 1
else: 
    print ("\nIncorreto!")
    print ("Mais de 1 bilhão de pessoas falam Mandarim, principalmente na China, sendo a língua com mais falantes nativos.")

#pergunta 7 
print("\nPergunta 7 \nQual continente tem mais países?\na) Ásia\nb) Europa\nc) África")
answer7 = input("\nResposta: ")

if answer7.lower() == "c":
    print("Correto!")
    score = score + 1
else: 
    print ("\nIncorreto!")
    print ("África tem 54 países reconhecidos internacionalmente.")

#pergunta 8 
print("\nPergunta 8 \nQual é o maior país do mundo em área?\na) India\nb) Russia\nc) China")
answer8 = input("\nResposta: ")

if answer8.lower() == "b":
    print("Correto!")
    score = score + 1
else: 
    print ("\nIncorreto!")
    print ("Rússia tem cerca de 17 milhões km².")

#pergunta 9 
print("\nPergunta 9 \nQual é o ponto mais alto da Terra?\na) Monte Everest\nb) Monte Kilimanjaro\nc) Monte Fuji")
answer9 = input("\nResposta: ")

if answer9.lower() == "a":
    print("Correto!")
    score = score + 1
else: 
    print ("\nIncorreto!")
    print ("Monte Everest é o ponto mais alto da terra, com 8.848 metros de altura.")

#pergunta 10 
print("\nPergunta 10 \nQuantos países são reconhecidos pela ONU?\na) 195 \nb) 98\nc) 133")
answer10 = input("\nResposta: ")

if answer10.lower() == "a":
    print("Correto!")
    score = score + 1
else: 
    print ("\nIncorreto!")
    print ("Atualmente, existem 195 países reconhecidos pela ONU, sendo 193 Estados-membros e 2 observadores (Vaticano e Palestina).")
    

print(f"\nO quiz acabou! Pontuação: {score}/10")
