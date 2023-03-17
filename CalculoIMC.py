nome = ''
altura = 0.
peso = 0
imc = 0.



print('=====CÁLCULO DE IMC=====')




def le_dados():
    global nome
    global altura
    global peso

nome = input('Digite seu nome:')
altura = float(input('Digite sua altura:'))
peso = float(input('Digite seu peso:'))



def calculo_imc():
    global altura
    global peso

    imc = peso / pow(altura, 2)
    return round(imc, 2)




def avalia_imc():
    imc = calculo_imc()
    if imc < 18.5:
        return('Abaixo do peso.')
    elif imc >= 18.5 and imc <25:
        return('Com peso normal.')
    else:
        return('Acima do peso.')
    
le_dados()
imc = calculo_imc()
msg = avalia_imc()

print(f'{nome} tem IMC de {imc} e está {msg}')