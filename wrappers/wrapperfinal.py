#abrir arquivo de texto e dar um split passando quebra de linha (\n) como parâmetro,
#resultando em uma lista já dividida 
f = open('/home/bmelo/teste2','r')
arquivo = f.read()
arquivoSemiPronto = arquivo.split('\n')
#filtrar a lista, removendo todos os itens nulos ('')
arquivoLista = filter(None, arquivoSemiPronto)
#loop pra iterar sobre os artigos e tirar a primeira linha com informação desnecessária (se a primeira linha possuir '[', é retirada)
counter=0
for x in arquivoLista:
    if '[' in x:
        arquivoLista.remove(x)
        continue
    else:
        continue

#loop onde se o indice 2 dos 5 primeiros itens da lista atual for "Comments", é printado com comments e retirado esses mesmo 5 primeiros da lista para printar
#o próximo doc. caso não seja "Comments", o doc é printado sem comments e apenas os 4 primeiros são retirados, até a lista esvaziar e quebrar o laço.
while len(arquivoLista) != 0:
    if 'Comments' in (arquivoLista[2]):
        print('Title: ' + arquivoLista[0] + '\n' + 'Autores: ' + arquivoLista[1] + '\n' + arquivoLista[2] + '\n' + arquivoLista[3] + '\n' + 'Abstract: ' + arquivoLista[4] + '\n')
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        continue
    if 'Comments' not in (arquivoLista[2]):       
        print('Title: ' + arquivoLista[0] + '\n' + 'Autores: ' + arquivoLista[1] + '\n' + arquivoLista[2] + '\n' + 'Abstract: ' + arquivoLista[3]+'\n')
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        continue





