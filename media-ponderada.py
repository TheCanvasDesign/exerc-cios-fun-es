nota_mat = 7.0
nota_cie = 8.5
nota_his = 9.5

peso_mat = 2
peso_cie = 3
peso_his = 5

def media_ponderada():

    soma_notas = (7.0 * 2) + (8.5 * 3) + (9.5 * 5)
    soma_pesos = peso_mat + peso_cie + peso_his
    media = soma_notas / soma_pesos

    print(f"A média ponderada é: {media:.2f} ")

media_ponderada()

# versão com entrada de usuário

nota1 = float(input("Digite o valor da primeira nota: "))
peso1 = float(input("Digite o valor do 1º peso: "))
nota2 = float(input("Digite o valor da segunda nota: "))
peso2 = float(input("Digite o valor do 2º peso: "))
nota3 = float(input("Digite o valor da terceira nota: "))
peso3 = float(input("Digite o valor do 3º peso: "))

def media_ponderada():
    soma_notas = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
    soma_pesos = peso1 + peso2 + peso3
    media = soma_notas / soma_pesos

    print(f"A média ponderada do aluno é: {media:.2f} ")

media_ponderada()


def media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3):
    soma_notas = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
    soma_pesos = peso1 + peso2 + peso3
    media = soma_notas / soma_pesos

    print(f"A média ponderada do aluno é: {media:.2f} ")

nota1 = float(input("Digite o valor da primeira nota: "))
peso1 = float(input("Digite o valor do 1º peso: "))
nota2 = float(input("Digite o valor da segunda nota: "))
peso2 = float(input("Digite o valor do 2º peso: "))
nota3 = float(input("Digite o valor da terceira nota: "))
peso3 = float(input("Digite o valor do 3º peso: "))

media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3)
              