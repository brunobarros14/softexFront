print("calculadora da solftex")
f1 = float (input("digite o primeiro numero"))
f2 = float (input("digite o segundo numero"))
op = (input("Digite a operação desejada (Soma: +, Subtrair: -, Multiplar: *, Dividir: /) :"))
print (f1, op, f2"=" calculadora)

def calculadora(f1, f2, op):
    if op == '+':
        return f1 + f2
    elif op == '-':
        return f1 - f2
    elif op == '*':
        return f1 * f2
    elif op == '/':
        return f1 / f2
    else:
        return 0
    