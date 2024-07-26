estados = []
alfabeto = []
funcaoTransicao = {}
estadoIncial = None
estadosFinais = []

while True:
    estado = input('Informe um estado: ')
    if estado == '':
        break
    estados.append(estado)

while True:
    caractere = input('Informe um caractere: ')
    if caractere == '':
        break
    alfabeto.append(caractere)

for estado in estados:
    transicaoLocal = {}
    for caractere in alfabeto:
        temp = input(f'({estado}, {caractere})= ')
        transicaoLocal[caractere] = temp 
    funcaoTransicao[estado] = transicaoLocal

estadoIncial = input('Informe o estado incial: ')

while True:
    estadoFinal = input('Informe um estado final: ')
    if estadoFinal == '':
        break
    estadosFinais.append(estadoFinal)

while True:
    estadoAtual = estadoIncial
    palavra = input('Informe uma palavra: ')
    if palavra == '':
        break
    for caractere in palavra:
        proximoEstado = funcaoTransicao[estadoAtual][caractere]
        estadoAtual = proximoEstado
    if estadoAtual in estadosFinais:
        print('Palavra aceita!')
    else:
        print('Palavra não aceita. :(')


print(f'Estados: {estados}\nAlfabeto: {alfabeto}\nFunção de Transição: {funcaoTransicao}\nEstado Inicial: {estadoIncial}\nEstado(s) Fina(l/is): {estadosFinais}')
