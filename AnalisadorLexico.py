from Consts import *
from Classes import *

def move(s,c):
    
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
        
def acoes(s):
    if s.estado == "2":
         return Token("RELOP",s.lexema,None,"LE")
    
    elif s.estado == "3":
        s = trata_lookahead(s)
        return Token("RELOP",s.lexema,None,"LT")
    
    elif s.estado == "5":
        return Token("RELOP",s.lexema,None,"GE")
    
    elif s.estado == "6":
        s = trata_lookahead(s)
        return Token("RELOP",s.lexema,None,"GT")
    
    elif s.estado == "8":
        return Token("RELOP",s.lexema,None,"EQ")
    
    elif s.estado == "10":
        return Token("RELOP",s.lexema,None,"NE")
    
    elif s.estado == "11":
        return Token("+",s.lexema,None,None)
    
    elif s.estado == "12":
        return Token("-",s.lexema,None,None)
    
    elif s.estado == "13":
        return Token("/",s.lexema,None,None)
    
    elif s.estado == "15":
        s = trata_lookahead(s)
        return Token("*",s.lexema,None,None)  
     
    elif s.estado == "16":
        return Token("**",s.lexema,None,None)
    
    elif s.estado == "17":
        return Token("(",s.lexema,None,None)
    
    elif s.estado == "18":
        return Token(")",s.lexema,None,None)
    
    elif s.estado == "19":
        return Token(",",s.lexema,None,None)
    
    elif s.estado == "20":
        return Token(";",s.lexema,None,None)
    
    elif s.estado == "22":
        s = trata_lookahead(s)
        return Token(":",s.lexema,None,None)
    
    elif s.estado == "23":
        return Token(":=",s.lexema,None,None)
    
    elif s.estado == "26": #caractere
        #Procurar na tabela de símbolos
        posicao,tipo_token = procura_tabela_simbolos(s,"caractere",None)
        return Token(tipo_token,s.lexema,posicao,None)
    
    elif s.estado == "28": #Separador
        s = trata_lookahead(s)
        s = trata_barraN(s)
        return None
    
    elif s.estado == "30": #Comentario
        s = trata_barraN(s)
        return None
    
    elif s.estado == "32": #ID
        #Procurar na tabela de símbolo
        s = trata_lookahead(s)
        posicao,tipo_token = procura_tabela_simbolos(s,"ID",None)
        return Token(tipo_token,s.lexema,posicao,None)
    
    elif s.estado == "35": #NUM INT
        s = trata_lookahead(s)
        posicao,tipo_token = procura_tabela_simbolos(s,"NUM","INT")
        return Token(tipo_token,s.lexema,posicao,"INT")
    
    elif s.estado == "37": #NUM FLOAT
        s = trata_lookahead(s)
        posicao,tipo_token = procura_tabela_simbolos(s,"NUM","FLOAT")
        return Token(tipo_token,s.lexema,posicao,"FLOAT")
    
    elif s.estado == "41": #NUM FLOAT com E
        s = trata_lookahead(s)
        posicao,tipo_token = procura_tabela_simbolos(s,"NUM","FLOAT")
        return Token(tipo_token,s.lexema,posicao,"FLOAT")
    
    elif s.estado == "42": #EOF
        return Token("$",s.lexema,None,"EOF")
    
    elif s.estado == "-1":
        return ERRO
    
    else:
        return None

def trata_barraN(s):
    if '\n' in s.lexema:
        for car in s.lexema:
            if car == '\n':
                s.coluna = 1
                s.linha += 1
            if car == ' ':
                s.coluna += 1

    return s
    
def procura_tabela_simbolos(s,tipo_token,tipo):
    if s.lexema not in TabelaSimbolos.tabela:
        TabelaSimbolos.tabela[s.lexema] = [tipo_token,None,tipo]
    posicao = s.lexema
    tipo_token = TabelaSimbolos.tabela[s.lexema][0]
    return posicao,tipo_token

def estado_inicial(s):
    return Lexer(s.linha,s.coluna,"",str(0),s.indice)

def eh_final(s):
    if s.estado in ESTADOS_FINAIS:
        return True
    else:
        return False
    
def trata_lookahead(s):
    s.indice-=1
    s.coluna-=1
    s.lexema=s.lexema[:-1]
    return s

def analisador_lexico(arquivo, s):
    
    s = estado_inicial(s)
    linhaInicial = s.linha
    colunaInicial = s.coluna

    while(not eh_final(s)):
        s.indice+=1
        if(s.indice == len(arquivo)):
            c=EOF #EOF
            s.lexema+=c
            s.coluna += 1
            s = move(s,c)
            break
        c = arquivo[s.indice]
        s.lexema+=c
        s = move(s,c)
        s.coluna += 1

    token = acoes(s)
    
    #if verifica se é ws ou comentario
    if (token == None):
        return analisador_lexico(arquivo, s)
    if (token == ERRO):
        return token,None,linhaInicial,colunaInicial
    else:
        return token,s,linhaInicial,colunaInicial