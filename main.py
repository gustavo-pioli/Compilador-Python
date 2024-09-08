import AnalisadorLexico as al
from Classes import *

if __name__ == '__main__':

    caminho_arquivo = "teste.txt"
    with open(caminho_arquivo, 'r') as arquivo:
        arquivo = arquivo.read()

    indice = -1
    linha = 1
    coluna = 1

    while (indice < len(arquivo)-1):
        token,linhaInicial,colunaInicial,linha,coluna,indice = al.analisador_lexico(arquivo, linha, coluna, indice)
        if(indice==-1 or indice == len(arquivo)-1):
            if(token):
                print(f"<{token.tipo_token}, lexema= {token.lexema}, valor= {token.valor}, tipo= {token.tipo}, linha:{linhaInicial}, coluna:{colunaInicial}>")
            break
        if(token == ERRO):
            print(f"ERRO NA LINHA {linhaInicial} E COLUNA {colunaInicial}")
            break
        else:
            print(f"<{token.tipo_token}, lexema= {token.lexema}, valor= {token.valor}, tipo= {token.tipo}, linha:{linhaInicial}, coluna:{colunaInicial}>")

#tok,l,c,in=al(ar,i,l,c)