import re
import fileinput
from googletrans import Translator


FICHERO_PRUEBAS = 'file.txt'
FICHERO_TRADUCIR = 'index.html'

def traducir_en_to_es(texto: str):
    translator = Translator()
    translation = translator.translate(texto, dest='es')
    
    return translation.text

if __name__ == "__main__":
    print("Vamos a traducir")
    
    patron = re.compile('(?s)\<source\>\n(?:[^\n][\n]?)+\<\/source\>')
    
    with open(FICHERO_TRADUCIR, 'r') as file_in :
        filedata = file_in.read()
    
        # for match in re.finditer(r'(?s)\<source\>\n(?:[^\n][\n]?)+\<\/source\>', filedata):
        #     print(match.start(), match.end())
        for match in re.findall(r'(?s)\<source\>\n(?:[^\n][\n]?)+\<\/source\>', filedata):
            # print(match.start(), match.end())
            print(match)
        # print(filedata)
    
    
    # with fileinput.FileInput(FICHERO_PRUEBAS, inplace=True, backup='.bak') as file:
    #     for line in file:
    #         print(line.replace(text_to_search, replacement_text), end='')
    
    # filedata = filedata.replace(patron, '\1\<source\>\n\2+\<\/source\>' )
    
    # with open('file.txt', 'w') as file_out:
    #     file_out.write(filedata)

