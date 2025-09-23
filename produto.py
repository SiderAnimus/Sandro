import re

def grava():
    produtos = open('produtos.txt', "a")
    p = input("Digite um produto: ")
    produtos.write(p + "\n")
    produtos.close()

def imprime():
    produtos = open('produtos.txt', "r")
    print(produtos.read())
    produtos.close()

def pesquisa(qual):
    produtos = open('produtos.txt', "r")
    produto = produtos.readlines()
    for p in produto:
        if re.search(qual, p, re.IGNORECASE):
            print(p)
    produtos.close()

resposta = "s"
while resposta == "s" or resposta == "S":
    grava()
    resposta = input("Deseja contiuar (S/N)? ")
imprime()
qual = input('Qual produto? ')
pesquisa(qual)