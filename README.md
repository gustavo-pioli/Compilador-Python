# Projeto de Construção de Compiladores

Autores: [Natan Gonçalves de Lyra](https://github.com/NatanGLyra), [Gustavo Pioli Resende](https://github.com/gustavo-pioli), [Vinicius Dias Martins Rocha](https://github.com/ViniciusDMRocha)

## Descrição

Este projeto foi desenvolvido para a disciplina de **Construção de Compiladores**, lecionada na **Universidade Federal de Uberlândia**. O principal objetivo é a construção do **front-end** para uma linguagem de programação especificada. Para isso, foram implementados o **Analisador Léxico** e o **Analisador Sintático**. Além dessas implementações, o projeto também contém a documentação da gramática e diagramas referentes ao funcionamento do compilador.

## Índice

- [Projeto de Construção de Compiladores](#projeto-de-construção-de-compiladores)
  - [Descrição](#descrição)
  - [Índice](#índice)
  - [Arquivos do Projeto](#arquivos-do-projeto)
    - [AnalisadorLexico.py](#analisadorlexicopy)
    - [AnalisadorSintatico.py](#analisadorsintaticopy)
    - [Classes.py](#classespy)
    - [Consts.py](#constspy)
    - [main\_lexica.py](#main_lexicapy)
    - [ProjetoCompiladores.pdf](#projetocompiladorespdf)
  - [Execução](#execução)
  - [Mais informações](#mais-informações)

## Arquivos do Projeto

### [AnalisadorLexico.py](https://github.com/gustavo-pioli/Compilador-Python/blob/main/AnalisadorLexico.py)
Contém o código do **Analisador Léxico**, responsável por identificar e classificar os tokens da linguagem de acordo com as definições estabelecidas.

### [AnalisadorSintatico.py](https://github.com/gustavo-pioli/Compilador-Python/blob/main/AnalisadorSintatico.py)
Implementa o **Analisador Sintático**, que faz a verificação da estrutura gramatical da linguagem, validando se a sequência de tokens está de acordo com a gramática especificada e além disso também cria e retorna uma Árvore Sintática que utiliza uma estrutura de nó vinda de uma Árvore Genérica que utiliza siblings.

### [Classes.py](https://github.com/gustavo-pioli/Compilador-Python/blob/main/Classes.py)
Este arquivo contém a definição das **classes** utilizadas no projeto, como `Lexer`, `Node`, `Token`, entre outras. Essas classes formam a base da estrutura do compilador, sendo fundamentais para a análise e construção da árvore sintática.

### [Consts.py](https://github.com/gustavo-pioli/Compilador-Python/blob/main/Consts.py)
Armazena as **constantes** usadas no projeto, incluindo o **diagrama de estados** gerado a partir da análise dos diagramas da gramática. Esse arquivo é importante para centralizar configurações e definições de valores fixos utilizados durante a análise léxica e sintática.

### [main_lexica.py](https://github.com/gustavo-pioli/Compilador-Python/blob/main/main_lexica.py)
Este arquivo contém a **função principal** que executa o Analisador Léxico, realizando a leitura do código-fonte e iniciando o processo de tokenização.

### [ProjetoCompiladores.pdf](github.com/gustavo-pioli/Compilador-Python/blob/main/ProjetoCompiladores.pdf)
Este documento PDF apresenta o **relatório completo do projeto**, contendo a descrição detalhada da implementação dos analisadores léxico e sintático, incluindo:
- Lista de **tokens**;
- **Expressões regulares** usadas no analisador léxico;
- **Grafos sintáticos** e o **Diagrama Unificado**;
- Outros detalhes técnicos e teóricos relacionados ao desenvolvimento do trabalho.

## Execução

Para realizar a execução, certifique-se de ter o Python instalado.

Tenha certeza também de ter colocado o código que queira testar nos arquivos `teste_lexico.txt` e `teste_sintatico.txt`.

Para rodar apenas o analisador léxico, você pode executar o arquivo `main_lexica.py`. 

```bash
   python main_lexica.py
```

Caso queira rodar o analisador sintático, execute o seguinte comando:

```bash
   python AnalisadorSintatico.py
```

## Mais informações

Para mais detalhes sobre o projeto, consulte o relatório completo disponível no arquivo ProjetoCompiladores.