# Projeto: Tech News Scraping
Este projeto foi desenvolvido enquanto estudante da Trybe no módulo de Ciências da Computação.

---
## Objetivo
Utilizar o **Python** para resolver problemas e otimizar algoritmos, desenvolvendo minha capacidade de implementar soluções para diversos tipos de problemos.

---
## Habilidades desenvolvidas
 - Lógica.
 - Interpretação de problema.
 - Interpretação de código de terceiros.
 - Otimização da resolução de problemas.
 - Otimização de algoritmos.

---
## Requisitos
### 1. Encontre o horário em que o maior número de estudantes esta presente (Algotimo de busca)
  <details>
    <summary>Detalhes</summary>
    
  Você trabalha na maior empresa de educação do Brasil. Certo dia, a pessoa Product Manager `(PM)` quer saber qual horário tem a maior quantidade de pessoas estudantes acessando o conteúdo da plataforma. Com esse dado em mãos, a pessoa PM saberá qual é o melhor horário para disponibilizar os materiais de estudo para ter o maior engajamento possível.

  O horário de entrada e saída do sistema é cadastrado no banco de dados toda vez que uma pessoa estudante entra e sai do sistema. Esses dados estarão contidos em uma lista de tuplas (`permanence_period`) em que cada tupla representa o período de permanência de uma pessoa estudante no sistema com seu horário de entrada e de saída.

  Seu trabalho é descobrir qual o melhor horário para disponibilizar os conteúdos de estudo. Para isso, utilize a estratégia de resolução de problemas chamada `força bruta` em que a função desenvolvida por você será chamada várias vezes com valores diferentes para a variável `target_time` e serão analisados os retornos da função.
  </details>

### 2. Criptografia de inversões (Testes)
  <details>
    <summary>Detalhes</summary>
    
  Durante a dinâmica em grupos de um processo seletivo, a empresa contratante definiu um desafio em duplas, e cada pessoa terá um papel. A primeira pessoa deve criar uma função de criptografia, e a segunda pessoa deve implementar os testes da função implementada pela primeira pessoa.

  Você fará o papel da _**segunda pessoa**_ nessa dinâmica, ou seja: deve implementar os testes de uma função de criptografia.

  Esse teste deve se chamar `test_encrypt_message`, e ele deve garantir que a função de criptografia `encrypt_message` deve respeitar uma lógica específica.
  </details>

### 3. Palíndromos (Recursividade)
  <details>
    <summary>Detalhes</summary>
    
  Escreva uma função que irá determinar se uma palavra é um palíndromo ou não. A função irá receber uma string de parâmetro e o retorno será um _booleano_, `True` ou `False`.

  > Um palíndromo é uma palavra, frase ou número que mantém seu sentido mesmo sendo lido de trás para frente. Por exemplo, `"ABCBA"`. 
  </details>

### 4. Anagramas (Algoritmo de ordenação)
  <details>
    <summary>Detalhes</summary>
    
  Faça um algoritmo que consiga comparar duas _strings_, ordená-las e identificar se uma é um anagrama da outra. Ou seja, sua função irá receber duas strings de parâmetro e o retorno da função será uma tupla `()` com a primeira string ordenada, a segunda string ordenada e um _booleano_, `True` ou `False` representando se são anagramas.

  O algoritmo deve considerar letras _maiúsculas_ e _minúsculas_ como iguais durante a comparação das entradas, ou seja, ser _case insensitive_. 

  > "Um anagrama é uma espécie de jogo de palavras criado com a reorganização das letras de uma palavra ou expressão para produzir outras palavras ou expressões, utilizando todas as letras originais exatamente uma vez." 
  </details>

### 5. Números repetidos (Algoritmo de busca)
  <details>
    <summary>Detalhes</summary>
    
  Dada um _array_ de números inteiros contendo `n + 1` inteiros, chamado de `nums`, em que cada inteiro está no intervalo `[1, n]`.

  Retorne apenas um número duplicado em `nums`. 
  </details>

### 6. Palíndromos (Iteratividade)
  <details>
    <summary>Detalhes</summary>
    
  Resolva o mesmo problema apresentado no `requisito 2 - Palíndromos`, porém dessa vez utilizando a solução iterativa. 
  </details>

---
## O que foi utilizado?
 - Python.
 - Pymongo.
 - Pytest, Pytest-Cov, Pytest-Json.
 - Big-O, MatPlotLib.
 - Flake8, Black, Wheel.

---
## Rodando Localmente
1. Clone o repositório e abra a pasta raiz.
2. Ative o ambiente virtual do python pelo terminal:
  ```bash
    python3 -m venv .venv && source .venv/bin/activate
  ```
3. Instale as dependências pelo terminal:
  ```bash
    python3 -m pip install -r dev-requirements.txt
  ```
4. Na pasta `challenges` você encontrara todos os modulos desenvolvidas, você pode executa-los usando o modo iterativo
  ```bash
    python3 -i <PATH-DO-ARQUIVO>
  ```
