# primeiro eu preciso pegar o dado da primeira linha e coluna da sheet do arquivo 1,
# depois comparar só esse dado com toda cooluna da sheet 2. Ao final, eu vou comparar
# o dado da segunda linha da sheet1, e assim sucessivamente.

import asyncio
from csv import writer
import pandas as pd

coluna = str()

def compara(sheet_a, sheet_b):
    
    for result in sheet_a:
        for result_2 in sheet_b:
            # print(f'Comparando {result} com {result_2}')
            if result == result_2:
                # print(f'{result} = {result_2}')
                output = open('./output.txt', 'a')
                output.writelines(f'{result}\n')
    
def abre_excel(coluna):

    data = pd.read_excel (r'sheet_a.xlsx') 
    df = pd.DataFrame(data, columns= ['host','ip'])
    
    data2 = pd.read_excel (r'sheet_b.xlsx') 
    df2 = pd.DataFrame(data2, columns= ['host','ip'])
    
    global sheet_a
    sheet_a = df[coluna].tolist()

    global sheet_b
    sheet_b = df2[coluna].tolist()
    
    return(sheet_a, sheet_b)
   
def main():
    colunas = ['host', 'ip']
    for column in colunas:
        abre_excel(column)
        compara(sheet_a, sheet_b)
    print("Comparação concluída com sucesso, verifique os itens repetidos no arquivo output.txt")

if __name__ == "__main__":
    main()