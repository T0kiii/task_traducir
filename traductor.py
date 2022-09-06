import re
import fileinput
from googletrans import Translator


FICHERO_PRUEBAS = 'index.html'
FICHERO_TRADUCIR = 'fichero_prueba.xlf'

def traducir_en_to_es(textos):
    translator = Translator()
    translation = translator.translate(textos, dest='es')
    
    return translation.text

if __name__ == "__main__":
    print("Vamos a traducir")
    
    # FUNCIONA: (?s)\<source\>\n*(?:[^\n][\n]?)+\<\/source\>
    # a ver si funciona ---> (?s)\<source\>\n*([^\n][\n]?)+\<\/source\>
    patron = re.compile('(?s)\<source\>\n*(?:[^\n][\n]?)+\<\/source\>')
    
    with open(FICHERO_TRADUCIR, 'r') as file_in :
        filedata = file_in.read()
        # print(filedata)
    
        # for match in re.finditer(r'(?s)\<source\>\n(?:[^\n][\n]?)+\<\/source\>', filedata):
        #     print(match.start(), match.end())
        matches = re.findall(patron, filedata)
        # for match in re.findall(patron, filedata):
            # print(match.start(), match.end())
        print(matches)
        # print(filedata)
    
    
    # with fileinput.FileInput(FICHERO_PRUEBAS, inplace=True, backup='.bak') as file:
    #     for line in file:
    #         print(line.replace(text_to_search, replacement_text), end='')
    
    # filedata = filedata.replace(patron, '\1\<source\>\n\2+\<\/source\>' )
    
    # with open('file.txt', 'w') as file_out:
    #     file_out.write(filedata)

