def gravaInformacao():
    pessoa=open('pessoa.txt','a')
    data=open('data.txt','a')
    fone=open('fone.txt','a')
    
    nome=input("Informe o seu nome: ")
    idade=input("Digite sua idade: ")
    telefone=input("Digite seu telefone: ")
    
    pessoa.write(nome+'\n')
    data.write(idade+'\n')
    fone.write(telefone+'\n')
    
    pessoa.close()
    data.close()
    fone.close()

def gravaHabilidade():
    habilidade=open('habilidade.txt','a')
    
    habil=input("Quais são suas habilidades: ")
    habilidade.write(habil+'\n')
    
    habilidade.close()
    
def gravaTrabalho():
    trabalho=open('trabalho.txt')
    trabalho=input("Digite onde já trabalhou: ")
    trabalho.close()
    
def criacaoCurriculo():
    curriculo=open('curriculo.html','w')
    pessoa=open('pessoa.txt','r')
    idade=open('data.txt','r')
    fone=open('fone.txt','r')
    
    pes = pessoa.readlines()
    ida = idade.readlines()
    fon = fone.readlines()
    z=0
    for m in pes:
        texto=title+"curriculo"+title+"\n"
        texto=head+"\n"
        texto="Nome"+m+"\n"
        texto= texto + "Idade"+ida[z]+"\t\t"+"Fone:"+fon[z]
        z=z+1
    curriculo.write(texto)
    
    pessoa.close()
    idade.close()
    fone.close()
resposta='s'
gravaInformacao()
while resposta == 's' or resposta == 'S':
    gravaHabilidade()
    resposta = input("Deseja continuar (S/N)? ")
while resposta == 's' or resposta == 'S':
    gravaTrabalho()
    resposta = input("Deseja continuar (S/N)? ")
    
criacaoCurriculo()