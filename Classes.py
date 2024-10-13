from Consts import *

class Lexer():
    def __init__(self,linha,coluna,lexema,estado,indice):
        self.linha = linha
        self.coluna = coluna
        self.lexema = lexema
        self.estado = estado
        self.indice = indice

class Token():
    def __init__(self,tipo_token,lexema,valor,tipo):
        self.tipo_token = tipo_token
        self.lexema = lexema
        self.posicao = valor
        self.tipo_dado = tipo

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

class FIRST():
    first = {}
    first["<declaracao_variavel>"] = ["char", "int", "float"]
    first["<comando>"] = ["while", "repeat", "if", "ID"]
    first["<comando_selecao>"] = ["if"]
    first["<comando_repeticao>"] = ["while", "repeat"]
    first["<comando_atribuicao>"] = ["ID"]
    first["<bloco>"] = ["begin"]


class Node:
    def __init__(self, name):
        self.name = name
        self.child = None  # Primeiro filho
        self.sibling = None  # Irmão à direita

    def add_child(self, child):
        
        if self.child is None:
            self.child = child
        else:
            current = self.child
            while current.sibling:
                current = current.sibling
            current.sibling = child