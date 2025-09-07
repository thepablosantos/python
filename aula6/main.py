nome = input("Qual o seu nome?")
idade = int(input("Qual a sua idade?"))
altura = float(input("Qual a sua altura?"))
estudante = input("Voce e estudante?").lower() == "true"

if idade >= 18:
    print("Voce e maior de idade")
else:
    print("Voce e menor de idade")

if altura >= 1.77:
    print("Voce e alto")
else:
    print("Voce e baixo")

if estudante and idade>18:
    print("Voce e estudante")
else:
    print("Voce nao e estudante")