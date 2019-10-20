import stanfordnlp
import os

#nlp = stanfordnlp.Pipeline(lang = 'hi')
files = os.listdir('lemmas')
#files = ['union_public.txt']
lemmas = dict()
for f in files:
    file = open('lemmas/' + f, 'r', encoding = 'utf-8')
    for complete_line in file:
        line = complete_line.split(',')[0]
        count = int(complete_line.split(',')[1].strip('\n'))
        word_form = line.strip('\n')
        if word_form !=  None and len(word_form) > 0:
            #doc = nlp(word_form)
            #for sent in doc.sentences:
            #    for word in sent.words:
            if word_form in lemmas.keys():
                lemmas[word_form] = lemmas[word_form] + count
            else:
                lemmas[word_form] = count
            #lemmas.add(word_form)

    file.close()
print(lemmas)
file = open('union_corpora_lemma.txt', 'w', encoding = 'utf-8')
for lemma, count in lemmas.items():
    file.write(lemma + ',' + str(count) + '\n')
file.close()
