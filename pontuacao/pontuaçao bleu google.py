from nltk.translate.bleu_score import corpus_bleu
traducaoReferencia = [[['I', 'remembered', 'the', 'definition', 'that', 'José', 'Dias', 'had', 'given', 'them,', 'eyes', 'of', 'an', 'oblique', 'and', 'disguised', 'gypsy.', 'I', 'didnt', 'know', 'what', 'oblique', 'was,', 'but', 'disguised', 'I', 'did,', 'and', 'I', 'wanted', 'to', 'see', 'if', 'they', 'could', 'call', 'it', 'that.', 'Capitu', 'allowed', 'herself', 'to', 'be', 'stared', 'at', 'and', 'examined.', 'I', 'only', 'asked', 'myself', 'what', 'it', 'was;', 'if', 'I', 'had', 'never', 'seen', 'them.', 'I', 'found', 'nothing', 'extraordinary;', 'the', 'color', 'and', 'sweetness', 'were', 'my', 'acquaintances.', 'The', 'delay', 'of', 'contemplation,', 'I', 'think,', 'gave', 'her', 'another', 'idea', 'of', 'my', 'intention;', 'she', 'imagined', 'that', 'it', 'was', 'a', 'pretext', 'to', 'look', 'at', 'them', 'more', 'closely,', 'with', 'my', 'long,', 'steady', 'eyes', 'fixed', 'on', 'them.', 'And,', 'to', 'this,', 'I', 'attribute', 'that', 'they', 'began', 'to', 'grow', 'larger', 'and', 'darker,', 'with', 'such', 'an', 'expression', 'that', 'gives', 'me', 'an', 'exact', 'and', 'poetic', 'comparison', 'to', 'say', 'what', 'those', 'eyes', 'of', 'Capitu', 'were.', 'I', 'cant', 'think', 'of', 'an', 'image', 'capable', 'of', 'saying,', 'without', 'breaking', 'the', 'dignity', 'of', 'the', 'style,', 'what', 'they', 'were', 'and', 'what', 'they', 'did', 'to', 'me.', 'Hangover', 'eyes?', 'Come', 'on,', 'hangover.', 'Its', 'what', 'gives', 'me', 'the', 'idea', 'of', 'that', 'new', 'face.', 'They', 'brought', 'some', 'mysterious', 'and', 'energetic', 'fluid,', 'a', 'force', 'that', 'dragged', 'them', 'inwards,', 'like', 'the', 'wave', 'that', 'leaves', 'the', 'beach', 'on', 'hangover', 'days.', 'In', 'order', 'not', 'to', 'be', 'dragged', 'away,', 'I', 'clung', 'to', 'the', 'other', 'neighboring', 'parts,', 'to', 'the', 'ears,', 'to', 'the', 'arms,', 'to', 'the', 'hair', 'spread', 'over', 'the', 'shoulders;', 'but', 'as', 'quickly', 'as', 'I', 'sought', 'the', 'pupils,', 'the', 'wave', 'that', 'came', 'out', 'of', 'them', 'was', 'growing,', 'hollow', 'and', 'dark,', 'threatening', 'to', 'envelop', 'me,', 'pull', 'me', 'in', 'and', 'swallow', 'me.', 'How', 'many', 'minutes', 'did', 'we', 'spend', 'on', 'that', 'game?', 'Only', 'the', 'clocks', 'of', 'Heaven', 'will', 'have', 'marked', 'this', 'infinite', 'and', 'brief', 'time.', 'Eternity', 'has', 'its', 'pendulums;', 'not', 'even', 'because', 'it', 'never', 'ends,', 'he', 'never', 'ceases', 'to', 'know', 'how', 'long', 'the', 'happiness', 'and', 'torments', 'will', 'last.', 'It', 'will', 'double', 'the', 'joy', 'of', 'the', 'blessed', 'of', 'Heaven', 'if', 'they', 'know', 'the', 'sum', 'of', 'torments', 'that', 'their', 'enemies', 'will', 'have', 'already', 'suffered', 'in', 'hell.', 'Also,', 'the', 'number', 'of', 'delights', 'his', 'enemies', 'will', 'have', 'enjoyed', 'in', 'Heaven', 'will', 'increase', 'the', 'pains', 'of', 'the', 'damned', 'in', 'hell.', 'This', 'other', 'torment', 'escaped', 'the', 'divine', 'Dante,', 'but', 'Im', 'not', 'here', 'to', 'amend', 'poets.', 'Im', 'about', 'to', 'tell', 'you', 'that,', 'at', 'the', 'end', 'of', 'an', 'unmarked', 'time,', 'I', 'grabbed', 'Capitus', 'hair', 'definitively,', 'but', 'then', 'with', 'my', 'hands,', 'and', 'told', 'her', '—', 'to', 'say', 'something', '—', 'that', 'I', 'was', 'capable', 'of', 'combing', 'them', 'if', 'I', 'wanted', 'to.']]]
traducaoCandidato = [['I', 'had', 'remembered', 'the', 'definition', 'that', 'José', 'Dias', 'had', 'given', 'them,', 'eyes', 'of', 'an', 'oblique', 'and', 'disguised', 'gypsy.', 'I', 'didnt', 'know', 'what', 'oblique', 'was,', 'but', 'covertly', 'I', 'did,', 'and', 'I', 'wanted', 'to', 'see', 'if', 'they', 'could', 'call', 'it', 'that.', 'Capitu', 'allowed', 'himself', 'to', 'be', 'stared', 'at', 'and', 'examined.', 'He', 'only', 'asked', 'me', 'what', 'it', 'was,', 'if', 'he', 'had', 'never', 'seen', 'them;', 'I', 'found', 'nothing', 'extraordinary;', 'the', 'color', 'and', 'sweetness', 'were', 'my', 'acquaintances.', 'The', 'delay', 'of', 'contemplation', 'I', 'think', 'gave', 'him', 'another', 'idea', 'of', 'my', 'intention;', 'he', 'imagined', 'that', 'it', 'was', 'a', 'pretext', 'to', 'look', 'at', 'them', 'more', 'closely,', 'with', 'my', 'long,', 'steady', 'eyes', 'fixed', 'on', 'them,', 'and', 'to', 'this', 'I', 'attribute', 'that', 'they', 'began', 'to', 'grow', 'larger,', 'larger', 'and', 'somber,', 'with', 'such', 'an', 'expression', 'that...', 'give', 'me', 'an', 'exact', 'and', 'poetic', 'comparison', 'to', 'say', 'what', 'those', 'eyes', 'of', 'Capitu', 'were.', 'I', 'cant', 'think', 'of', 'an', 'image', 'capable', 'of', 'saying,', 'without', 'breaking', 'the', 'dignity', 'of', 'the', 'style,', 'what', 'they', 'were', 'and', 'what', 'they', 'did', 'to', 'me.', 'Hangover', 'eyes?', 'Come', 'on,', 'hangover.', 'Its', 'what', 'gives', 'me', 'the', 'idea', 'of', 'that', 'new', 'feature.', 'They', 'brought', 'some', 'mysterious', 'and', 'energetic', 'fluid,', 'a', 'force', 'that', 'dragged', 'them', 'inwards,', 'like', 'the', 'wave', 'that', 'leaves', 'the', 'beach,', 'on', 'days', 'of', 'undertow.', 'In', 'order', 'not', 'to', 'be', 'dragged', 'away,', 'I', 'clung', 'to', 'the', 'other', 'neighboring', 'parts,', 'to', 'the', 'ears,', 'to', 'the', 'arms,', 'to', 'the', 'hair', 'spread', 'over', 'the', 'shoulders;', 'but', 'as', 'quickly', 'as', 'I', 'sought', 'the', 'pupils,', 'the', 'wave', 'that', 'came', 'out', 'of', 'them', 'was', 'growing,', 'hollow', 'and', 'dark,', 'threatening', 'to', 'envelop', 'me,', 'pull', 'me', 'in', 'and', 'swallow', 'me.', 'How', 'many', 'minutes', 'did', 'we', 'spend', 'on', 'that', 'game?', 'Only', 'the', 'clocks', 'of', 'Heaven', 'will', 'have', 'marked', 'this', 'infinite', 'and', 'brief', 'time.', 'Eternity', 'has', 'its', 'pendulums;', 'not', 'even', 'because', 'it', 'never', 'ends,', 'he', 'never', 'ceases', 'to', 'want', 'to', 'know', 'how', 'long', 'the', 'happiness', 'and', 'torments', 'will', 'last.', 'It', 'will', 'double', 'the', 'joy', 'of', 'the', 'blessed', 'of', 'Heaven', 'to', 'know', 'the', 'sum', 'of', 'the', 'torments', 'that', 'their', 'enemies', 'will', 'have', 'already', 'suffered', 'in', 'hell;', 'so', 'also', 'the', 'amount', 'of', 'delights', 'that', 'his', 'enemies', 'will', 'have', 'enjoyed', 'in', 'Heaven', 'will', 'increase', 'the', 'pains', 'of', 'the', 'damned', 'in', 'hell.', 'This', 'other', 'torment', 'escaped', 'the', 'divine', 'Dante;', 'but', 'Im', 'not', 'here', 'to', 'amend', 'poets.', 'Im', 'about', 'to', 'tell', 'you', 'that,', 'at', 'the', 'end', 'of', 'an', 'unmarked', 'time,', 'I', 'grabbed', 'Capitus', 'hair', 'definitively,', 'but', 'then', 'with', 'my', 'hands,', 'and', 'told', 'her,', '—', 'to', 'say', 'something', '—', 'that', 'I', 'was', 'capable', 'of', 'combing', 'them', 'if', 'I', 'wanted', 'to.']]
pontuacao = corpus_bleu(traducaoReferencia, traducaoCandidato)
print(f'{pontuacao:.5f}')