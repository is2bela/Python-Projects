def is_palindrome(word):
    # bl (back letter) / fl (front letters)
    bl = len(word) - 1
    for fl in range(len(word)):
        if word[fl] == word[bl]:
            bl = bl - 1
            if fl == bl:
                break
        else:
            return False
    return True

print("Bem vindo ao programa de verificação de Palíndromo!")

while True:
    word = input("Digite uma palavra (ou 'sair' para encerrar): ")
    if word.lower() == "sair":
        print("Programa encerrado.")
        break

    if is_palindrome(word.lower()):
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
