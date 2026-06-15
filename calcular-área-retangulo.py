

def retangulo(largura = 5, comprimento = 8):
    area = largura * comprimento
    print(f"A largura total da área do jardim é: {area} m²")

retangulo(largura = 5, comprimento = 8)

# Com entrada de usuário

def retangulo(largura, comprimento):
    
    area = largura * comprimento
    print(f"A área total do jardim é: {area:.2f} m²")

largura = float(input("Digite o valor da largura: "))
comprimento = float(input("Digite o valor do comprimento: "))

retangulo(largura, comprimento)