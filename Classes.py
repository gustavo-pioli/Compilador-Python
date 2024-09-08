from Consts import *

class Lexer():
    def __init__(self,linha,coluna,lexema,estado, indice):
        self.linha = linha
        self.coluna = coluna
        self.lexema = lexema
        self.estado = estado
        self.indice = indice

class Token():
    def __init__(self,tipo_token,lexema,valor,tipo):
        self.tipo_token = tipo_token
        self.lexema = lexema
        self.valor = valor
        self.tipo = tipo

class TabelaSimbolos():
    #self.tabela["lexema"] = ["tipo_token", "valor", "tipo"]
    tabela = {}
    tabela["main"] = ["main", None, None]
    tabela["begin"] = ["begin", None, None]
    tabela["end"] = ["end", None, None]
    tabela["int"] = ["int", None, None]
    tabela["char"] = ["char", None, None]
    tabela["float"] = ["float", None, None]
    tabela["if"] = ["if", None, None]
    tabela["then"] = ["then", None, None]
    tabela["else"] = ["else", None, None]
    tabela["while"] = ["while", None, None]
    tabela["do"] = ["do", None, None]
    tabela["repeat"] = ["repeat", None, None]
    tabela["until"] = ["until", None, None]