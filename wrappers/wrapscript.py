#abrir arquivo de texto e dar um split passando quebra de linha (\n) como parâmetro,
#resultando em uma lista já dividida 
f = open('/home/bmelo/teste2','r')
arquivo = f.read()
arquivoLista = arquivo.split('\n')
#checar se o 3o elemento da lista é subjects ou comments
#caso seja subjects, quer dizer que nao tem comentario, então o abstract sera do indice 3 em diante, printa titulo + autor + subject + abstract
#caso seja comments, quer dizer que tem comentario, então o abstract sera do indice 4 em diante, printa titulo + autor + comments + subject + abstract
indice2 = arquivoLista[2].split(':')
if indice2[0] == 'Subjects':
    print('Title: '+ str(arquivoLista[0]) + '\n' + 'Autores: ' + str(arquivoLista[1]) + '\n' + 'Subjects: ' + str(arquivoLista[2]) + '\n' + 'Abstract: ' + str(arquivoLista[3:]))
elif indice2[0] == 'Comments':
    print('Title: '+ str(arquivoLista[0]) + '\n' + 'Autores: ' + str(arquivoLista[1]) + '\n' + str(arquivoLista[2]) + '\n' + str(arquivoLista[3]) + '\n' + 'Abstract: ' + str(arquivoLista[4:]))


