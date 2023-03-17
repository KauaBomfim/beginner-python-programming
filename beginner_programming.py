print('===PAINEL DE LOGIN===')
login = input('Nome:')
senha = input('Senha:')

passo = 0
status = 'Aguardando novo pedido'

print('===FAÇA SEU PEDIDO!===')

def entregar():
    global passo
    passo += 1
    status = 'Pedido entregue'
    print(f'Passo {passo}: {status} ao {login}!')

def destino():
    global passo
    passo += 1
    status = 'Seu pedido está indo até você!'
    print(f'Passo {passo}: {status}')
    entregar()

def preparar():
    global passo
    passo += 1
    status = 'preparando seu pedido...'
    print(f'Passo {passo}: {status}')
    destino()

def atender():
    global passo
    passo += 1
    status = 'Pedido recebido!'
    print(f'passo {passo}: {status}')
    preparar()

atender()


avaliacao = int(input('Deixe a sua avaliação de 0 a 10:'))

if avaliacao >= 7:
    print('Avaliação positiva!')
else:
    print('Avaliação negativa!')



print(f'{login} deixou uma avaliação de {avaliacao}')
print(status)