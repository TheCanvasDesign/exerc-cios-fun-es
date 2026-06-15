

def quadrado():
    lado = 3
    tapete = lado * 4
    print(f"O perímetro total do tapete é: {tapete:.2f} ")

quadrado()



def quadrado(lado):
    tapete = lado * 4
    print(f"O perímetro total do tapete é: {tapete:.2f} ")

lado = float(input("Digite o valor do lado: "))

quadrado(lado)
