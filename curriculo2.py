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
    resposta='s'
    i=0
    while resposta == 's' or resposta == 'S':
        habilidade=open('habilidade.txt','a')
        habil=input('Quais são suas habilidades: ')
        habilidade.write(habil+'\n')
        habilidade.close()
        resposta = input('Deseja continuar (S/N)? ')
    i=i+1
    return i

def gravaTrabalho():
    resposta='s'
    j=0
    while resposta == 's' or resposta == 'S':
        trabalho=open('trabalho.txt','a')
        trab=input('Digite onde já trabalhou: ')
        trabalho.write(trab+'\n')
        trabalho.close()
        resposta = input('Deseja continuar (S/N)? ')
    j=j+1
    return j
    
def criacaoCurriculo(m,n):
    curriculo=open('curriculo.txt','w')
    dat=open('data.txt','r')
    da=dat.readlines()
    
    curriculo.write('<!DOCTYPE html>\n')
    curriculo.write('<html>\n')
    curriculo.write('   <head>\n')
    curriculo.write('       <style>\n')
    curriculo.write('           *{\n')
    curriculo.write('               backgroud-color:#00ffff\n')
    curriculo.write('               font-family: Verdana, Geneva, Tahoma, sans-serif;\n')
    curriculo.write('           }\n')
    curriculo.write('       </style>\n')
    curriculo.write('   </head>\n')
    curriculo.write('   <body>\n')
    curriculo.write('       <p>Idade:'+da+'</p>\n')
    curriculo.write('   </body>\n')
    curriculo.write('</html>\n')
    
    curriculo.close()
    data.close()

gravaInformacao()
gravaHabilidade()
gravaTrabalho()
criacaoCurriculo()