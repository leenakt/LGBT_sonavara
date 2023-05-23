from estnltk import Text #Laen vajalikud paketid
from estnltk.taggers import VabamorfTagger

import os

kaust = "C:/Users/leena/OneDrive/DisneyGames/Documents/馬鹿/Parandatud_failid/Textgrid_analüüs/morfanaluus" #Salvestan kausta teekonna muutujasse

morph_tagger = VabamorfTagger(slang_lex=True) #Morfoloogiline analüüs slängileksikoniga

for failinimi in os.listdir(kaust): #Tsükkel failide läbi käimiseks
    if failinimi.endswith('.txt'):
        fail = os.path.join(kaust, failinimi)
        with open(fail, 'r', encoding='utf-8') as file: #Morfoloogiline analüüs
            tekst = file.read()
            tekst = Text(tekst)
            tekst.tag_layer(['words', 'sentences'])
            morph_tagger.tag( tekst )
            fail_uus = fail.rstrip(".txt") + "_lemma.txt" #Loon failid lemmade salvestamiseks
            with open(fail_uus, "a", encoding="UTF-8") as file: #Salvestan lemmad failidesse
                for lemma in tekst.lemma:
                    if lemma[0].isalpha() == True:
                        file.write(lemma[0])
                        file.write('\n')