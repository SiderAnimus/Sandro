def gravaDebito():
    devedor=open('devedor.txt','a')
    divida=open('divida.txt','a')
    
    nome=input("Informe o nome do devedor: ")
    valor=input("Digite o valor em aberto: ")
    devedor.write(nome+'\n')
    divida.write(valor+'\n')
    
    devedor.close()
    divida.close()
    
def cobrancaDebitos():
    cobranca=open('carta.txt','w')
    devedor=open('devedor.txt','r')
    divida=open('divida.txt','r')
    dev = devedor.readlines()
    div = divida.readlines()
    i=0
    for d in dev:
        texto="Prezado"+d+"\n"
        texto= texto + "Venho"+"\n"
        texto= texto + "Consta"+div[i]+"\n"
        i=i+1
    cobranca.write(texto)
    cobranca.close()
    devedor.close()
    divida.close()
resposta='s'
while resposta == 's' or resposta == 'S':
    gravaDebito()
    resposta = input("Deseja continuar (S/N)? ")
cobrancaDebitos()