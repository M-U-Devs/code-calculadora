# Função para adição
def add(x, y):
   return x + y

# Função para subtração
def subtract(x, y):
   return x - y

# Função para multiplicação
def multiply(x, y):
   return x * y

# Função para divisão
def divide(x, y):
   return x / y

# Menu de opções
print("Selecione a operação.")
print("1.Adicionar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")

# Entrada de opção do usuário
choice = input("Digite sua opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))

else:
   print("Opção inválida")
