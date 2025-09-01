print("Calculadora")

while True:
    expr = input("\nDigite uma expressão matemática (ou '0' para sair): ")
    if expr == "0":
        break
    try:
        result = eval(expr, {"__builtins__": None}, {})
        print("O resultado é", result)
    except Exception as e:
        print("Erro:", e)