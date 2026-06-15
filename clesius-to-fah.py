celsius = 25
fahrenheit = 0

def temperatura():
    temp = (25*9/5)+32
    print(f"25 graus em celsius é equivalente a: {temp:.2f} graus em Fahrenheit")

temperatura()



# Fiz essa versão com entrada de usuário
def temperatura():
    celsius = float(input("Digite o valor em Celsius: "))
    
    temp = (celsius*9/5)+32

    print(f"Graus em celsius é equivalente a: {temp:.2f} graus em Fahrenheit")

temperatura()