def seila()
    for ndp in range(0, int(qcn)) :
        qnd = (l[aux - 1 :qbn])
        print(qnd)
        print(comando[0], comando[1], comando[2], 'isso é só um teste', comando[2], comando[1] + qnd)
        qbn = qbn + 256
        if tl > 255 :
            aux = aux + 256


titulo = str(input('qual o titulo: '))
autor = str(input('escritor: '))
comando = ['/give @p written_book{pages:[', "'", '"','] ,title:', ',author:', '}', titulo, autor] #estrutura do comando
l = str(input('cole aqui: ')) #livro em si.
tl = len(l) #total de caracteres do livro
print(tl)
qcn = int(tl/256) #quantidade de cortes nessessarios
print(qcn)
qbn = 256
aux = 1
input('s? ')
    qnd = (l[aux -1:qbn])
    print(qnd)
    print(comando[0], comando[1], comando[2], 'isso é só um teste', comando[2], comando[1] + qnd)
    qbn = qbn + 256
    if tl > 255:
        aux = aux + 256
print('fim conferencia')
controle = (comando[0], comando[1], comando[2], 'isso é só um teste',comando[2], comando[1],comando[3],comando[2], comando[6],comando[2], comando[4],comando[2], comando[7],comando[2], comando[5])
print(comando[0], comando[1], comando[2], 'isso é só um teste',comando[2], comando[1],comando[3],comando[2], comando[6],comando[2], comando[4],comando[2], comando[7],comando[2], comando[5])
