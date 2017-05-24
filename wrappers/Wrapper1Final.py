#biblioteca usada para encontrar o value maximo dentro das keys de um dicionario
import operator
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

#função para retornar um dicionario com o abstract em questão tokenizado, com as keys sendo os tokens e os values a qunatidade de vezes que aparecem no doc
def relations(abstract):
    lista = abstract.split(' ')
    arquivo = open('/home/bmelo/stopwords','r')
    stopwords = arquivo.read()
    dic = {}
    for x in lista:
        if x not in dic.keys():
            dic[x] = 1
            continue
        else:
            dic[x] += 1
            continue
    lista2 = dic.keys()
    for x in lista2:
        if x.lower() in stopwords:
            dic.pop(x)
            continue
        elif type(x) == int:
            dic.pop(x)
            continue
        else:
            continue
    return dic
#loop onde se o indice 2 dos 5 primeiros itens da lista atual for "Comments", é printado com comments e retirado esses mesmo 5 primeiros da lista para printar
#o próximo doc. caso não seja "Comments", o doc é printado sem comments e apenas os 4 primeiros são retirados, até a lista esvaziar e quebrar o laço.
while len(arquivoLista) != 0:
    if 'Comments' in (arquivoLista[2]):
        print('Title: ' + arquivoLista[0] + '\n' + 'Autores: ' + arquivoLista[1] + '\n' + arquivoLista[2] + '\n' + arquivoLista[3] + '\n' + 'Abstract: ' + arquivoLista[4] )
        rel = relations(arquivoLista[4])
        print('Relation 1: ' + max(rel.iteritems(), key=operator.itemgetter(1))[0])
        rel.pop(max(rel.iteritems(), key=operator.itemgetter(1))[0])
        print('Relation 2: ' + max(rel.iteritems(), key=operator.itemgetter(1))[0])
        rel.pop(max(rel.iteritems(), key=operator.itemgetter(1))[0])
        print('Relation 3: ' + max(rel.iteritems(), key=operator.itemgetter(1))[0])
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        continue
    if 'Comments' not in (arquivoLista[2]):       
        print('Title: ' + arquivoLista[0] + '\n' + 'Autores: ' + arquivoLista[1] + '\n' + arquivoLista[2] + '\n' + 'Abstract: ' + arquivoLista[3])
        rel = relations(arquivoLista[3])
        print('Relation 1: ' + max(rel.iteritems(), key=operator.itemgetter(1))[0])
        rel.pop(max(rel.iteritems(), key=operator.itemgetter(1))[0])
        print('Relation 2: ' + max(rel.iteritems(), key=operator.itemgetter(1))[0])
        rel.pop(max(rel.iteritems(), key=operator.itemgetter(1))[0])
        print('Relation 3: ' + max(rel.iteritems(), key=operator.itemgetter(1))[0])
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        arquivoLista.pop(0)
        continue





