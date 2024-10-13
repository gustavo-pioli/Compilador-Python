import AnalisadorLexico as al
from Classes import *

if __name__ == '__main__':

    caminho_arquivo = "teste_lexico.txt"
    with open(caminho_arquivo, 'r') as arquivo:
        arquivo = arquivo.read()

    s = Lexer(0,0,"",str(0),0)
    s.linha = 1
    s.coluna = 1
    s.indice = -1

    while (s.indice < len(arquivo)):

        token,s,linhaInicial,colunaInicial = al.analisador_lexico(arquivo, s)

        if(token == ERRO):
            print(f"Erro Léxico na linha {linhaInicial}, coluna {colunaInicial}")
            break
        else:
            print(f"<{token.tipo_token}, lexema= {token.lexema}, posicao= {token.posicao}, tipo= {token.tipo_dado}, linha:{linhaInicial}, coluna:{colunaInicial}>")