# Importar a biblioteca do NLKT para utilizar a pontuação BLEU
from nltk.translate.bleu_score import sentence_bleu
traducaoReferencia = [['isso', 'e', 'um', 'teste']]
traducaoCandidato = ['isso', 'e', 'um', 'teste']
pontuacao = sentence_bleu(traducaoReferencia, traducaoCandidato)
# A f-score utilizada no print foi como uma medida de precisão, delimitando o resultado da pontuação em até 5 dígitos após o ponto final.
print(f'{pontuacao:.5f}')