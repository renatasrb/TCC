# Transformar o texto em lista para utilizar o BLEU.
# Iremos utilizar em cada uma das traduções de referência e dos tradutores escolhidos.
# É necessário remover as aspas dos textos.

texto = 'Tinha-me lembrado a definição que José Dias dera deles, olhos de cigana oblíqua e dissimulada. Eu não sabia o que era oblíqua, mas dissimulada sabia, e queria ver se podiam chamar assim. Capitu deixou-se fitar e examinar. Só me perguntava o que era, se nunca os vira; eu nada achei extraordinário; a cor e a doçura eram minhas conhecidas. A demora da contemplação creio que lhe deu outra idéia do meu intento; imaginou que era um pretexto para mirá-los mais de perto, com os meus olhos longos, constantes, enfiados neles, e a isto atribuo que entrassem a ficar crescidos, crescidos e sombrios, com tal expressão que... Retórica dos namorados, dá-me uma comparação exata e poética para dizer o que foram aqueles olhos de Capitu. Não me acode imagem capaz de dizer, sem quebra da dignidade do estilo, o que eles foram e me fizeram. Olhos de ressaca? Vá, de ressaca. É o que me dá idéia daquela feição nova. Traziam não sei que fluido misterioso e enérgico, uma força que arrastava para dentro, como a vaga que se retira da praia, nos dias de ressaca. Para não ser arrastado, agarrei-me às outras partes vizinhas, às orelhas, aos braços, aos cabelos espalhados pelos ombros; mas tão depressa buscava as pupilas, a onda que saía delas vinha crescendo, cava e escura, ameaçando envolver-me, puxar-me e tragar-me. Quantos minutos gastamos naquele jogo? Só os relógios do Céu terão marcado esse tempo infinito e breve. A eternidade tem as suas pêndulas; nem por não acabar nunca deixa de querer saber a duração das felicidades e dos suplícios. Há de dobrar o gozo aos bem-aventurados do Céu conhecer a soma dos tormentos que já terão padecido no inferno os seus inimigos; assim também a quantidade das delícias que terão gozado no Céu os seus desafetos aumentará as dores aos condenados do inferno. Este outro suplício escapou ao divino Dante; mas eu não estou aqui para emendar poetas. Estou para contar que, ao cabo de um tempo não marcado, agarrei-me definitivamente aos cabelos de Capitu, mas então com as mãos, e disse-lhe, — para dizer alguma coisa, — que era capaz de os pentear, se quisesse.'

texto_to_list = texto.split()

print(texto_to_list)
