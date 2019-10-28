import stanfordnlp
import os

nlp = stanfordnlp.Pipeline(processors='tokenize,mwt,pos', lang='hi')
'''
paths = ['Clean Own Corpora/clean_freq.csv',
'Clean Own Corpora/clean_lemma_freq.txt',
'Clean Subtitles/freq.txt',
'Clean Subtitles/lemma_freq.txt',
'Clean TDIL Corpora/Clean English_Hindi_Tourism Text Corpus - EILMT/CLEAN/freq.txt',
'Clean TDIL Corpora/Clean English_Hindi_Tourism Text Corpus - EILMT/CLEAN/lemma_freq.txt',
'Clean TDIL Corpora/Clean Hindi_English_ilci2corpus Agriculture Entertainment/Hindi Clean/freq.txt',
'Clean TDIL Corpora/Clean Hindi_English_ilci2corpus Agriculture Entertainment/Hindi Clean/lemma_freq.txt',
'Clean TDIL Corpora/Clean Hindi Monolingual Text Corpus ILCI II/freq.txt',
'Clean TDIL Corpora/Clean Hindi Monolingual Text Corpus ILCI II/lemma_freq.txt',
'Clean TDIL Corpora/Clean NamedEntityAnnotatedCorporaForHindi/Clean/freq.txt',
'Clean TDIL Corpora/Clean NamedEntityAnnotatedCorporaForHindi/Clean/lemma_freq.txt',
'Clean TDIL Corpora/Clean NER Corpora Hindi Marathi Punjabi/Clean/freq.txt',
'Clean TDIL Corpora/Clean NER Corpora Hindi Marathi Punjabi/Clean/lemma_freq.txt',
'Clean TDIL Corpora/Hindi_English_Health ILCI_Clean/freq.txt',
'Clean TDIL Corpora/Hindi_English_Health ILCI_Clean/lemma_freq.txt',
'Done CFILT/Clean Final Hindi MWE Dataset/Final/freq.txt',
'Done CFILT/Clean Final Hindi MWE Dataset/Final/lemma_freq.txt',
'Done CFILT/Clean hin_corp_unicode/freq.txt',
'Done CFILT/Clean hin_corp_unicode/lemma_freq.txt',
'Done CFILT/clean hindi parallel corpus/hindi/freq.txt',
'Done CFILT/clean hindi parallel corpus/hindi/lemma_freq.txt']
'''
paths = ['/opt/PhD/Work/StopWords/pos/Corpus/Subtitles/freq.csv', '/opt/PhD/Work/StopWords/pos/Corpus/Subtitles/lemma_freq.csv']

for path in paths:
    file = open(path)
    lines = [line.split(',')[0] for line in file]
    file.close()
    i = 1
    if not os.path.exists('/opt/PhD/Work/StopWords/pos' + path[path.rfind('/', 0, path.rfind('/')):path.rfind('/')]):
        os.makedirs('/opt/PhD/Work/StopWords/pos' + path[path.rfind('/', 0, path.rfind('/')):path.rfind('/')])
    file = open('/opt/PhD/Work/StopWords/pos' + path[path.rfind('/', 0, path.rfind('/')):path.rfind('.')] + '.csv', 'w', encoding = 'utf-8')

    for sentence in lines:
        if len(sentence.strip()) == 0:
            continue
        doc=nlp(sentence)
        for sent in doc.sentences:
            for word in sent.words:
                file.write(word.text + ',' + str(i) + ',' + word.xpos + '\n')
                print(word.text + ',' + str(i) + ',' + word.xpos)
                i += 1
    file.close()
#print(*[f'word: {word.text+" "}\tupos: {word.upos}\txpos: {word.xpos}' for sent in doc.sentences for word in sent.words], sep='\n')
