import re


def grava():
    nomes = open("nomes.txt", "a")
    n = input("Digite um nome: ")
    nomes.write(n + "\n")
    nomes.close()

    endereco = open("endereco.txt", "a")
    e = input("Digite o endereC'o: " + n)
    endereco.write(e + "\n")
    endereco.close()


def imprime():
    nomes = open("nomes.txt", "r")
    print(nomes.read())
    nomes.close()

    endereco = open("endereco.txt", "r")
    print(endereco.read())
    endereco.close()


def pesquisa(quem):
    nomes = open("nomes.txt", "r")
    nome = nomes.readlines()
    endereco = open("endereco.txt", "r")
    ende = endereco.readlines()
    posicao = 0
    for n in nome:
        if re.search(quem, n, re.IGNORECASE):
            print(n + " mora no endereco " + ende[posicao])
        posicao = posicao + 1
    nomes.close()
    endereco.close()


resposta = "s"
while resposta == "s" or resposta == "S":
    grava()
    resposta = input("Deseja contiuar (S/N)? ")
imprime()
quem = input("Quem deseja procurar? ")
pesquisa(quem)