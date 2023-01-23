# Pontuação BLEU
#### Trabalho de Conclusão de Curso 'Uma Análise de Desempenho da Tradução Automática dos Sistemas DeepL e Google Tradutor' - [Universidade de Brasília - Línguas Estrangeiras Aplicadas ao Multilinguismo e à Sociedade da Informação](http://lea-msi.unb.br/index.php/pt-br/)

## Objetivos Gerais
O principal objetivo é utilizar a pontuação Bilingual Evaluation Understudy Score (BLEU) para analisar o desempenho da tradução automática dos sistemas de tradução DeepL e Google Tradutor.

## Metodologia
Para realizar a avaliação das traduções no BLEU, teve-se como primeiro passo a instalação da linguagem de programação Python, utilizando o site [Thonny](https://thonny.org/). Após a instalação, o segundo passo é baixar a biblioteca do NLTK (Natural Language Toolkit), que foi usada como base para aplicar o método (Brownlee, 2019). Partimos para a ambientação do programa para iniciar as análises.

Assim, para a utilização do método BLEU, é necessário que cada palavra dos textos traduzidos esteja separada, em aspas. Para isso, utilizamos a funcionalidade de lista, em cada tradução. O texto é a string (sentença) que está armazenada na variável “texto”. Logo a seguir, é criada a variável texto_to_list, na qual é armazenada a função texto.split(), que tem o objetivo de separar o texto em elementos de uma lista.

Após colocar os textos em listas, utilizamos a função corpus_bleu() da biblioteca importada do NLTK, para calcular a pontuação BLEU dos textos traduzidos pelos sistemas, visto que possuem frases múltiplas. Para iniciar as avaliações no BLEU, foram realizados diversos testes para verificar se o código estava funcionando corretamente, por exemplo, se mesmo alterando “erroneamente” palavras do texto, se a pontuação iria ou não variar. Após realizado os testes, foi então iniciado as análises para verificação.
