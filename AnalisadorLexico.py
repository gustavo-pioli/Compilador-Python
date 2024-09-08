from Consts import *
from Classes import *

def move(s,c):
    #print(c,s.estado)
    for caractere,estado in TRANSICOES[s.estado]["transicoes"].items():
        if c in caractere:
            s.estado = estado
            return s
    for caractere,estado in TRANSICOES[s.estado]["transicoes_dif"].items():
        if c not in caractere:
            s.estado = estado
            return s
        
    s.estado = "-1"
    return s
        
 #   2, 3*, 5, 6*, 8, 10, 11, 12, 13, 15*, 16, 17, 
 #               18, 19, 20, 22*, 24, 27, 29*, 31, 33*, 36*, 38*, 42*
def acoes(s):
    if s.estado == "2":
         return Token("RELOP",s.lexema,"LE",None),s.linha,s.coluna,s.indice
    elif s.estado == "3":
        s = trata_lookahead(s)
        return Token("RELOP",s.lexema,"LT",None),s.linha,s.coluna,s.indice
    elif s.estado == "5":
        return Token("RELOP",s.lexema,"GE",None),s.linha,s.coluna,s.indice
    elif s.estado == "6":
        s = trata_lookahead(s)
        return Token("RELOP",s.lexema,"GT",None),s.linha,s.coluna,s.indice
    elif s.estado == "8":
        return Token("RELOP",s.lexema,"EQ",None),s.linha,s.coluna,s.indice
    elif s.estado == "10":
        return Token("RELOP",s.lexema,"NE",None),s.linha,s.coluna,s.indice
    elif s.estado == "11":
        return Token("OP",s.lexema,"SUM",None),s.linha,s.coluna,s.indice
    elif s.estado == "12":
        return Token("OP",s.lexema,"SUB",None),s.linha,s.coluna,s.indice
    elif s.estado == "13":
        return Token("OP",s.lexema,"DIV",None),s.linha,s.coluna,s.indice
    elif s.estado == "15":
        s = trata_lookahead(s)
        return Token("OP",s.lexema,"MULT",None),s.linha,s.coluna,s.indice   
    elif s.estado == "16":
        return Token("OP",s.lexema,"EXP",None),s.linha,s.coluna,s.indice
    elif s.estado == "17":
        return Token("(",s.lexema,None,None),s.linha,s.coluna,s.indice
    elif s.estado == "18":
        return Token(")",s.lexema,None,None),s.linha,s.coluna,s.indice
    elif s.estado == "19":
        return Token(",",s.lexema,None,None),s.linha,s.coluna,s.indice
    elif s.estado == "20":
        return Token(";",s.lexema,None,None),s.linha,s.coluna,s.indice
    elif s.estado == "22":
        s = trata_lookahead(s)
        return Token(":",s.lexema,None,None),s.linha,s.coluna,s.indice
    elif s.estado == "23":
        return Token(":=",s.lexema,None,None),s.linha,s.coluna,s.indice
    elif s.estado == "26":
        #Procurar na tabela de símbolos
        posicao,tipo_token = procura_tabela_simbolos(s,"SIMBOLO",None)
        return Token(tipo_token,s.lexema,posicao,None),s.linha,s.coluna,s.indice
    elif s.estado == "28":
        s = trata_lookahead(s)
        return None,s.linha,s.coluna,s.indice
    elif s.estado == "30":
        return None,s.linha,s.coluna,s.indice
    elif s.estado == "32": #ID
        #Procurar na tabela de símbolo
        s = trata_lookahead(s)
        posicao,tipo_token = procura_tabela_simbolos(s,"ID",None)
        return Token(tipo_token,s.lexema,posicao,None),s.linha,s.coluna,s.indice
    elif s.estado == "35":
        s = trata_lookahead(s)
        posicao,tipo_token = procura_tabela_simbolos(s,"NUM","INT")
        return Token(tipo_token,s.lexema,posicao,"INT"),s.linha,s.coluna,s.indice
    elif s.estado == "37":
        s = trata_lookahead(s)
        posicao,tipo_token = procura_tabela_simbolos(s,"NUM","FLOAT")
        return Token(tipo_token,s.lexema,posicao,"FLOAT"),s.linha,s.coluna,s.indice
    elif s.estado == "41":
        s = trata_lookahead(s)
        posicao,tipo_token = procura_tabela_simbolos(s,"NUM","FLOAT")
        return Token(tipo_token,s.lexema,posicao,"FLOAT"),s.linha,s.coluna,s.indice
    elif s.estado == "-1":
        return ERRO,None,None,None
    else:
        return None,None,None,None
    
def procura_tabela_simbolos(s,tipo_token,tipo):
    if s.lexema not in TabelaSimbolos.tabela:
        TabelaSimbolos.tabela[s.lexema] = [tipo_token,None,tipo]
    posicao = s.lexema
    tipo_token = TabelaSimbolos.tabela[s.lexema][0]
    return posicao,tipo_token

def estado_inicial(linha,coluna,indice):
    return Lexer(linha,coluna,"",str(0),indice)

def eh_final(s):
    if s.estado in ESTADOS_FINAIS:
        return True
    else:
        return False
    
def trata_lookahead(s):
    if(s.lexema[-1]==EOF):
        s.indice = -1
    else:
        s.indice-=1
    s.coluna-=1
    s.lexema=s.lexema[:-1]
    return s

def analisador_lexico(arquivo, linha, coluna, indice):
    
    s = estado_inicial(linha,coluna,indice)
    linhaInicial = linha
    colunaInicial = coluna

    while(not eh_final(s)):
        s.indice+=1
        if(s.indice == len(arquivo)):
            c=EOF #EOF
            s.lexema+=c
            s = move(s,c)
            break
        c = arquivo[s.indice]
        s.lexema+=c
        s = move(s,c)
        if (c == "\n"):
            s.linha += 1
            s.coluna = 1
        else:
            s.coluna += 1
    #token(tipo_token,lexema,valor,tipo)
    token,linha,coluna,indice = acoes(s) 
    
    #if verifica se é ws ou comentario e impede no caso de EOF
    if((token == None and indice < len(arquivo)-1) and (indice != -1)):
        return analisador_lexico(arquivo, linha, coluna, indice)
    if (token == ERRO):
        return token,linhaInicial,colunaInicial,None,None,None
    else:
        return token,linhaInicial,colunaInicial,s.linha,s.coluna,indice