from .addition import add
from .subtraction import subtract
from .division import divide
from .multiplication import multiply


def main():
    print("Bem-vindo à calculadora Python!")
    while True:
        print("\nEscolha a operação:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        print("5. Sair")
        choice = input("Digite o número da operação desejada: ")

        if choice == '1':
            num1, num2 = get_numbers()
            print(f"Resultado da adição: {add(num1, num2)}")
        elif choice == '2':
            num1, num2 = get_numbers()
            print(f"Resultado da subtração: {subtract(num1, num2)}")
        elif choice == '3':
            num1, num2 = get_numbers()
            try:
                print(f"Resultado da divisão: {divide(num1, num2)}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif choice == '4':
            num1, num2 = get_numbers()
            print(f"Resultado da multiplicação: {multiply(num1, num2)}")
        elif choice == '5':
            print("Saindo da calculadora.")
            break
        else:
            print("Escolha inválida. Tente novamente.")

def get_numbers():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

if __name__ == "__main__":
    main()
