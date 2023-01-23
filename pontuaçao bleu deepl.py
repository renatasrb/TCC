from nltk.translate.bleu_score import corpus_bleu
traducaoReferencia = [[['I', 'had', 'been', 'reminded', 'of', 'Jose', 'Dias', 'definition', 'of', 'them,', 'oblique', 'and', 'dissimulated', 'gypsy', 'eyes.', 'I', 'didnt', 'know', 'what', 'oblique', 'was', 'but', 'dissimulated', 'I', 'did,', 'and', 'I', 'wanted', 'to', 'see', 'if', 'they', 'could', 'be', 'called', 'that.', 'Capitu', 'let', 'herself', 'be', 'stared', 'at', 'and', 'examined.', 'I', 'only', 'wondered', 'what', 'it', 'was;', 'if', 'I', 'had', 'never', 'seen', 'them.', 'I', 'found', 'nothing', 'extraordinary;', 'the', 'color', 'and', 'sweetness', 'were', 'familiar', 'to', 'me.', 'The', 'delay', 'in', 'her', 'contemplation,', 'I', 'believe,', 'gave', 'her', 'another', 'idea', 'of', 'my', 'intentions;', 'she', 'imagined', 'it', 'was', 'a', 'pretext', 'to', 'look', 'at', 'them', 'more', 'closely,', 'with', 'my', 'long,', 'constant', 'eyes', 'stuck', 'in', 'them.', 'And,', 'to', 'this,', 'I', 'attribute', 'that', 'they', 'began', 'to', 'grow', 'bigger', 'and', 'darker,', 'with', 'such', 'an', 'expression', 'that...', 'Lovers', 'rhetoric', 'gives', 'me', 'an', 'exact', 'and', 'poetic', 'comparison', 'to', 'say', 'what', 'those', 'eyes', 'of', 'Capitus', 'were.', 'I', 'have', 'no', 'image', 'that', 'can', 'tell', 'without', 'breaking', 'the', 'dignity', 'of', 'style', 'what', 'they', 'were', 'and', 'what', 'they', 'did', 'to', 'me.', 'Hangover', 'eyes?', 'Come', 'on,', 'hungover.', 'Thats', 'what', 'gives', 'me', 'an', 'idea', 'of', 'that', 'new', 'face.', 'They', 'brought', 'a', 'mysterious', 'and', 'energetic', 'fluid,', 'a', 'force', 'that', 'dragged', 'me', 'in', 'like', 'the', 'wave', 'that', 'retreats', 'from', 'the', 'beach', 'on', 'hangover', 'days.', 'To', 'avoid', 'being', 'dragged', 'away,', 'I', 'clung', 'to', 'the', 'other', 'neighboring', 'parts,', 'to', 'the', 'ears,', 'to', 'the', 'arms,', 'to', 'the', 'hair', 'spread', 'across', 'the', 'shoulders;', 'but', 'as', 'soon', 'as', 'I', 'reached', 'for', 'the', 'pupils,', 'the', 'wave', 'that', 'came', 'out', 'of', 'them', 'grew', 'bigger,', 'hollow', 'and', 'dark,', 'threatening', 'to', 'envelop', 'me,', 'pull', 'me', 'in', 'and', 'swallow', 'me.', 'How', 'many', 'minutes', 'did', 'we', 'spend', 'in', 'that', 'game?', 'Only', 'the', 'clocks', 'in', 'heaven', 'will', 'have', 'marked', 'that', 'infinite', 'and', 'brief', 'time.', 'Eternity', 'has', 'pendulums;', 'it', 'never', 'stops', 'wanting', 'to', 'know', 'the', 'duration', 'of', 'happiness', 'and', 'suffering.', 'It', 'will', 'double', 'the', 'joy', 'of', 'the', 'blessed', 'in', 'Heaven', 'to', 'know', 'the', 'sum', 'of', 'torments', 'their', 'enemies', 'will', 'have', 'already', 'suffered', 'in', 'Hell.', 'And', 'the', 'amount', 'of', 'delights', 'their', 'enemies', 'will', 'have', 'enjoyed', 'in', 'Heaven', 'will', 'increase', 'the', 'pains', 'of', 'the', 'damned', 'in', 'Hell.', 'This', 'other', 'torment', 'escaped', 'the', 'divine', 'Dante,', 'but', 'I', 'am', 'not', 'here', 'to', 'amend', 'poets.', 'Im', 'here', 'to', 'tell', 'you', 'that,', 'after', 'an', 'unmarked', 'time,', 'I', 'definitely', 'grabbed', 'Capitus', 'hair,', 'but', 'then', 'with', 'my', 'hands,', 'and', 'told', 'her', '-', 'to', 'say', 'something', '-', 'that', 'I', 'was', 'capable', 'of', 'combing', 'it', 'if', 'I', 'wanted', 'to']]]
traducaoCandidato = [['I', 'had', 'been', 'reminded', 'of', 'Jose', 'Dias', 'definition', 'of', 'them,', 'oblique', 'and', 'dissimulated', 'gypsy', 'eyes.', 'I', 'didnt', 'know', 'what', 'oblique', 'was,', 'but', 'dissimulated', 'I', 'did,', 'and', 'I', 'wanted', 'to', 'see', 'if', 'they', 'could', 'be', 'called', 'that.', 'Capitu', 'let', 'herself', 'stare', 'and', 'examine.', 'She', 'only', 'wondered', 'what', 'it', 'was,', 'if', 'she', 'had', 'never', 'seen', 'them;', 'I', 'found', 'nothing', 'extraordinary;', 'the', 'color', 'and', 'sweetness', 'were', 'familiar', 'to', 'me.', 'The', 'delay', 'in', 'her', 'contemplation,', 'I', 'believe,', 'gave', 'her', 'another', 'idea', 'of', 'my', 'intentions;', 'she', 'imagined', 'it', 'was', 'a', 'pretext', 'to', 'look', 'at', 'them', 'more', 'closely,', 'with', 'my', 'long,', 'constant', 'eyes', 'stuck', 'in', 'them,', 'and', 'to', 'this', 'I', 'attribute', 'that', 'they', 'began', 'to', 'grow', 'bigger', 'and', 'bigger', 'and', 'darker,', 'with', 'such', 'an', 'expression', 'that...', 'Lovers', 'rhetoric,', 'give', 'me', 'an', 'exact', 'and', 'poetic', 'comparison', 'to', 'say', 'what', 'those', 'eyes', 'of', 'Capitus', 'were.', 'I', 'have', 'no', 'image', 'that', 'can', 'tell,', 'without', 'breaking', 'the', 'dignity', 'of', 'style,', 'what', 'they', 'were', 'and', 'what', 'they', 'did', 'to', 'me.', 'Hangover', 'eyes?', 'Come', 'on,', 'hungover.', 'Thats', 'what', 'gives', 'me', 'an', 'idea', 'of', 'that', 'new', 'feature.', 'They', 'brought', 'I', 'dont', 'know', 'what', 'mysterious', 'and', 'energetic', 'fluid,', 'a', 'force', 'that', 'dragged', 'me', 'in,', 'like', 'the', 'wave', 'that', 'retreats', 'from', 'the', 'beach', 'on', 'hangover', 'days.', 'To', 'avoid', 'being', 'dragged', 'away,', 'I', 'clung', 'to', 'the', 'other', 'neighboring', 'parts,', 'to', 'the', 'ears,', 'to', 'the', 'arms,', 'to', 'the', 'hair', 'spread', 'across', 'the', 'shoulders;', 'but', 'as', 'soon', 'as', 'I', 'reached', 'for', 'the', 'pupils,', 'the', 'wave', 'that', 'came', 'out', 'of', 'them', 'grew', 'bigger,', 'hollow', 'and', 'dark,', 'threatening', 'to', 'envelop', 'me,', 'to', 'pull', 'me', 'in', 'and', 'swallow', 'me.', 'How', 'many', 'minutes', 'did', 'we', 'spend', 'in', 'that', 'game?', 'Only', 'the', 'clocks', 'in', 'heaven', 'will', 'have', 'marked', 'that', 'infinite', 'and', 'brief', 'time.', 'Eternity', 'has', 'its', 'pendulums;', 'it', 'never', 'stops', 'wanting', 'to', 'know', 'the', 'duration', 'of', 'happiness', 'and', 'suffering.', 'It', 'will', 'double', 'the', 'joy', 'of', 'the', 'blessed', 'in', 'Heaven', 'to', 'know', 'the', 'sum', 'of', 'the', 'torments', 'that', 'their', 'enemies', 'will', 'have', 'already', 'suffered', 'in', 'Hell;', 'and', 'the', 'amount', 'of', 'the', 'delights', 'that', 'their', 'enemies', 'will', 'have', 'enjoyed', 'in', 'Heaven', 'will', 'increase', 'the', 'pains', 'of', 'the', 'damned', 'in', 'Hell.', 'This', 'other', 'torment', 'escaped', 'the', 'divine', 'Dante;', 'but', 'I', 'am', 'not', 'here', 'to', 'amend', 'poets.', 'Im', 'here', 'to', 'tell', 'you', 'that,', 'after', 'an', 'unmarked', 'time,', 'I', 'definitely', 'grabbed', 'Capitus', 'hair,', 'but', 'then', 'with', 'my', 'hands,', 'and', 'told', 'her,', '-', 'to', 'say', 'something,', '-', 'that', 'I', 'was', 'capable', 'of', 'combing', 'it,', 'if', 'I', 'wanted', 'to.']]
pontuacao = corpus_bleu(traducaoReferencia, traducaoCandidato)
print(f'{pontuacao:.5f}')