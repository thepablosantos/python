def coleta_dados():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    return x, y

x, y = coleta_dados()

def soma(x, y):
    return x + y

print(soma(x, y))

def subtrai(x, y):
    return x - y

print(subtrai(x, y))

