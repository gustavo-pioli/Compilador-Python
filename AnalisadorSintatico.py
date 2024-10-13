from Consts import *
from Classes import *
import AnalisadorLexico as al

class Parser:
    def __init__(self):
        self.current_token = None
        self.i = -1
        self.linha = 1
        self.coluna = 1
        self.s = Lexer(1,1,"",str(0),-1)
        self.next_token()
    
    def next_token(self):
        """Chama o analisador léxico para obter o próximo token."""
        tok, s, linha, coluna = al.analisador_lexico(arquivo, self.s)
        if(tok == ERRO):
            raise Exception(f"Erro Léxico na linha {linha}, coluna {coluna}")
        self.current_token = tok
        self.i = s.indice
        self.linha = linha
        self.coluna = coluna
        self.s = s
    
    def error(self, expected):
        """Emite uma mensagem de erro sintático."""
        if self.current_token:
            raise Exception(f"Erro sintático na linha {self.linha}, coluna {self.coluna}: "
                            f"Esperado '{expected}', encontrado '{self.current_token.tipo_token}'")
        else:
            raise Exception(f"Erro sintático: esperado '{expected}', mas chegou ao final do arquivo")
    
    def match(self, expected_type):
        """Verifica se o token atual é do tipo esperado e avança."""
        if self.current_token.tipo_token == expected_type:
            token = self.current_token
            self.next_token()
            return Node(token.lexema)
        else:
            self.error(expected_type)
    
    def INICIO(self):
        """<INICIO> ::= main ID <bloco>"""
        node = Node("<INICIO>")
        node.add_child(self.match("main"))
        node.add_child(self.match("ID"))
        node.add_child(self.bloco())
        if (self.current_token.tipo_token == "$"):
            node.add_child(Node("EOF"))
        return node
    
    def bloco(self):
        """<bloco> ::= begin <declaracao_variaveis> <sequencia_comandos> end"""
        node = Node("<bloco>")
        node.add_child(self.match("begin"))
        node.add_child(self.declaracao_variaveis())
        node.add_child(self.sequencia_comandos())
        node.add_child(self.match("end"))
        return node

    def declaracao_variaveis(self):
        """<declaracao_variaveis> ::= <declaracao_variavel> <declaracao_variaveis> | ε"""
        node = Node("<declaracao_variaveis>")
        if self.current_token.tipo_token in FIRST.first["<declaracao_variavel>"]:
            node.add_child(self.declaracao_variavel())
            node.add_child(self.declaracao_variaveis())
        else:
            node.add_child(Node("ε"))
        return node
    
    def declaracao_variavel(self):
        """<declaracao_variavel> ::= <tipo> : <lista_ids> ;"""
        node = Node("<declaracao_variavel>")
        node.add_child(self.tipo())
        node.add_child(self.match(":"))
        node.add_child(self.lista_ids())
        node.add_child(self.match(";"))
        return node
    
    def tipo(self):
        """<tipo> ::= char | int | float"""
        node = Node("<tipo>")
        if self.current_token.tipo_token in ["char", "int", "float"]:
            node.add_child(self.match(self.current_token.tipo_token))
        else:
            self.error("char, int ou float")
        return node
    
    def lista_ids(self):
        """<lista_ids> ::= ID<lista_ids’>"""
        node = Node("<lista_ids>")
        node.add_child(self.match("ID"))
        node.add_child(self.lista_ids_linha())
        return node

    def lista_ids_linha(self):
        """<lista_ids’> ::= ,ID<lista_ids’> | ε"""
        node = Node("<lista_ids’>")
        if self.current_token.lexema == ",":
            node.add_child(self.match(","))
            node.add_child(self.match("ID"))
            node.add_child(self.lista_ids_linha())
        else:
            node.add_child(Node("ε"))
        return node

    def sequencia_comandos(self):
        """<sequencia_comandos> ::= <comando> <sequencia_comandos> | ε"""
        node = Node("<sequencia_comandos>")
        if self.current_token.tipo_token in FIRST.first["<comando>"]:
            node.add_child(self.comando())
            node.add_child(self.sequencia_comandos())
        else:
            node.add_child(Node("ε"))
        return node

    def comando(self):
        """<comando> ::= <comando_selecao> | <comando_repeticao> | <comando_atribuicao>"""
        node = Node("<comando>")
        if self.current_token.tipo_token in FIRST.first["<comando_selecao>"]:
            node.add_child(self.comando_selecao())
        elif self.current_token.tipo_token in FIRST.first["<comando_repeticao>"]:
            node.add_child(self.comando_repeticao())
        elif self.current_token.tipo_token in FIRST.first["<comando_atribuicao>"]:
            node.add_child(self.comando_atribuicao())
        else:
            self.error("while, repeat, if ou ID")
        return node

    def comando_selecao(self):
        """<comando_selecao> ::= if ( <condicao> ) then <comando_ou_bloco> <comando_selecao’>"""
        node = Node("<comando_selecao>")
        node.add_child(self.match("if"))
        node.add_child(self.match("("))
        node.add_child(self.condicao())
        node.add_child(self.match(")"))
        node.add_child(self.match("then"))
        node.add_child(self.comando_ou_bloco())
        node.add_child(self.comando_selecao_linha())
        return node

    def comando_selecao_linha(self):
        """<comando_selecao’> ::= else <comando_ou_bloco> | ε"""
        node = Node("<comando_selecao’>")
        if self.current_token.tipo_token == "else":
            node.add_child(self.match("else"))
            node.add_child(self.comando_ou_bloco())
        else:
            node.add_child(Node("ε"))
        return node

    def comando_ou_bloco(self):
        """<comando_ou_bloco> ::= <comando> | <bloco>"""
        node = Node("<comando_ou_bloco>")
        if self.current_token.tipo_token in FIRST.first["<comando>"]:
            node.add_child(self.comando())
        elif self.current_token.tipo_token in FIRST.first["<bloco>"]:
            node.add_child(self.bloco())
        else:
            self.error("while, repeat, if, ID ou begin")
        return node

    def comando_repeticao(self):
        """<comando_repeticao> ::= while ( <condicao> ) do <comando_ou_bloco> | repeat <comando_ou_bloco> until ( <condicao> ) ;"""
        node = Node("<comando_repeticao>")
        if self.current_token.tipo_token == "while":
            node.add_child(self.match("while"))
            node.add_child(self.match("("))
            node.add_child(self.condicao())
            node.add_child(self.match(")"))
            node.add_child(self.match("do"))
            node.add_child(self.comando_ou_bloco())
        elif self.current_token.tipo_token == "repeat":
            node.add_child(self.match("repeat"))
            node.add_child(self.comando_ou_bloco())
            node.add_child(self.match("until"))
            node.add_child(self.match("("))
            node.add_child(self.condicao())
            node.add_child(self.match(")"))
            node.add_child(self.match(";"))
        else:
            self.error("while ou repeat")
        return node

    def comando_atribuicao(self):
        """<comando_atribuicao> ::= ID := <expressao> ;"""
        node = Node("<comando_atribuicao>")
        node.add_child(self.match("ID"))
        node.add_child(self.match(":="))
        node.add_child(self.expressao())
        node.add_child(self.match(";"))
        return node

    def condicao(self):
        """<condicao> ::= <expressao> relop <expressao>"""
        node = Node("<condicao>")
        node.add_child(self.expressao())
        node.add_child(self.match("RELOP"))
        node.add_child(self.expressao())
        return node

    def expressao(self):
        """<expressao> ::= <termo><expressao’>"""
        node = Node("<expressao>")
        node.add_child(self.termo())
        node.add_child(self.expressao_linha())
        return node

    def expressao_linha(self):
        """<expressao’> ::= + <termo> <expressao’> | - <termo> <expressao’> | ε"""
        node = Node("<expressao’>")
        if self.current_token.tipo_token in ["+", "-"]:
            node.add_child(self.match(self.current_token.tipo_token))
            node.add_child(self.termo())
            node.add_child(self.expressao_linha())
        else:
            node.add_child(Node("ε"))
        return node

    def termo(self):
        """<termo> ::= <exp><termo’>"""
        node = Node("<termo>")
        node.add_child(self.exp())
        node.add_child(self.termo_linha())
        return node

    def termo_linha(self):
        """<termo’> ::= * <exp> <termo’> | / <exp> <termo’> | ε"""
        node = Node("<termo’>")
        if self.current_token.tipo_token in ["*", "/"]:
            node.add_child(self.match(self.current_token.tipo_token))
            node.add_child(self.exp())
            node.add_child(self.termo_linha())
        else:
            node.add_child(Node("ε"))
        return node

    def exp(self):
        """<exp> ::= <fator><exp’>"""
        node = Node("<exp>")
        node.add_child(self.fator())
        node.add_child(self.exp_linha())
        return node

    def exp_linha(self):
        """<exp’> ::= ** <fator> <exp’> | ε"""
        node = Node("<exp’>")
        if self.current_token.tipo_token == "**":
            node.add_child(self.match("**"))
            node.add_child(self.fator())
            node.add_child(self.exp_linha())
        else:
            node.add_child(Node("ε"))
        return node

    def fator(self):
        """<fator> ::= num | caractere | ID | (<expressao>)"""
        node = Node("<fator>")
        if self.current_token.tipo_token == "NUM":
            node.add_child(self.match("NUM"))
        elif self.current_token.tipo_token == "caractere":
            node.add_child(self.match("caractere"))
        elif self.current_token.tipo_token == "ID":
            node.add_child(self.match("ID"))
        elif self.current_token.tipo_token == "(":
            node.add_child(self.match("("))
            node.add_child(self.expressao())
            node.add_child(self.match(")"))
        else:
            self.error("num, caractere, ID ou (")
        return node

def print_tree(node, level=0):
        if node is None:
            return
        
        # Imprime o nó atual com a indentação correspondente ao nível
        indent = ""
        for i in range (level):
            indent += "  "
        print(f"{indent}{node.name}")
        
        # Primeiro imprime o filho (com nível incrementado)
        if node.child:
            print_tree(node.child, level + 1)
        
        # Depois imprime os irmãos (no mesmo nível)
        if node.sibling:
            print_tree(node.sibling, level)

if __name__ == '__main__':

    caminho_arquivo = "teste_sintatico.txt"
    with open(caminho_arquivo, 'r') as arquivo:
        arquivo = arquivo.read()

    parser = Parser()
    try:
        arvore_sintatica = parser.INICIO()
        print_tree(arvore_sintatica)
    except Exception as e:
        print(e)