print("Conversor de Temperatura")
print("--------------------------")
print("\nÍndice: \nC - Celcius \nF - Fahrenheit \nK - Kelvin\n(Exemplo de conversão: C-F / Celcius para Fahrenheit)")
repeat_prompt = "sim" 

while repeat_prompt == "sim":
    conversion = input("\nDigite a conversão: ")
    conversion = conversion.replace(" ", "").upper()
    conversions = ["C-F", "C-K", "F-C", "F-K", "K-C", "K-F"]
    result = 0

    if conversion not in conversions:
        print("Conversão inválida. Tente novamente.")
        continue
    try:
        temp = float(input("Digite o valor a ser convertido: "))
    except ValueError:
        print("Valor inválido. Por favor digite um número.")

    if conversion == "C-F":
        result = temp * 1.8 + 32
        print(f"{temp:g} °C são {result:g} °F")

    elif conversion == "C-K":
        result = temp + 273
        print(f"{temp:g} °C são {result:g} K")

    elif conversion == "F-C":
        result = (temp - 32)/ 1.8
        print(f"{temp:g} °F são {result:g} °C")

    elif conversion == "F-K":
        result = (temp - 32) * 5/9 + 273
        print(f"{temp:g} °F são {result:g} K")

    elif conversion == "K-C":
        result = temp - 273
        print(f"{temp:g} K são {result:g} °C")

    elif conversion == "K-F":
        result = (temp - 273) * 1.8 + 32
        print(f"{temp:g} K são {result:g} °F")
    
    repeat_prompt = input("\nDeseja converter outro valor? \nSim/Não: ").lower()

    if repeat_prompt == "não" or repeat_prompt == "nao":
        print("\nEncerrando o programa. Até mais!")
    elif repeat_prompt != "sim":
        print("Não entendi, por favor responda com Sim ou Não.")
        break

