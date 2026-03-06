# Calculadora Universal do Samuel
print("--- Calculadora Universal ---")
print("Digite a conta completa (ex: (5+5)*2) ou 'sair' para encerrar.")
print("""
SÍMBOLOS DISPONÍVEIS:
 [+] Soma          [-] Subtração
 [*] Multiplicação [/] Divisão
 [**] Potência     [%] Resto da divisão
 [( )] Parênteses  [//] Divisão inte
""")
while True:
    expressao = input("\nDigite a conta: ")

    if expressao.lower() == 'sair':
        break

    try:
        # A função eval() resolve a conta inteira de uma vez
        resultado = eval(expressao)
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except Exception:
        print("Erro: Expressão inválida. Use apenas números e operadores (+, -, *, /).")
