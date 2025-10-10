def gravaInformacao():
    pessoa=open('pessoa.txt','a')
    data=open('data.txt','a')
    fone=open('fone.txt','a')
    
    nome=input('Informe o seu nome: ')
    idade=input('Digite sua idade: ')
    telefone=input('Digite seu telefone: ')
    
    pessoa.write(nome+'\n')
    data.write(idade+'\n')
    fone.write(telefone+'\n')
    
    pessoa.close()
    data.close()
    fone.close()

def gravaHabilidade():
    habilidade=open('habilidade.txt','a')
    
    habil=input('Quais são suas habilidades: ')
    habilidade.write(habil+'\n')
    
    habilidade.close()
    
def gravaTrabalho():
    trabalho=open('trabalho.txt','a')
    
    trab=input('Digite onde já trabalhou: ')
    trabalho.write(trab+'\n')
    
    trabalho.close()
    
def criacaocurriculo():

with open("pessoa.txt",'r') as pessoas:
pessoa = pessoas.read()

 with open("curriculo.txt", 'w') as arquivo:

html = [
"<html>",
"<body>",
"<h1>",
pessoa,
"</h1>",
"</body>",
"</html>",


]

for i in html:
arquivo.write(i)

    
resposta='s'
resp='s'
gravaInformacao()
while resposta == 's' or resposta == 'S':
    gravaHabilidade()
    resposta = input('Deseja continuar (S/N)? ')
while resp == 's' or resp == 'S':
    gravaTrabalho()
    resp = input('Deseja continuar (S/N)? ')
criacaoCurriculo()