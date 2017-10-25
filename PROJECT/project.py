import sys
import re

file = open('sample_corpus.txt', 'r', encoding='utf-8')
letters = open('project_letters.txt', 'r', encoding='utf-8')
lexics = open('project_lexics.txt', 'r', encoding='utf-8')
phon_morph = open('project_phon_morph.txt', 'r', encoding='utf-8')

translit = {}
ph_mo = {}
lexic = {}

for line in letters:
    line = line.replace('\n', '')
    line = line.split('\t')
    translit[line[0]] = line[1]

for line in lexics:
    line = line.replace('\n', '')
    line = line.split('\t')
    lexic[line[0]] = line[1]

for line in phon_morph:
    line = line.replace('\n', '')
    line = line.split('\t')
    ph_mo[line[0]] = line[1]
    
for word in file:
    word = word.strip().split(' ')
    for w in word:
        w = re.sub('([?!,.—:;()])', '', w)
        tr = w
        p_m = w
        lex = w
        for key, value in translit.items():
                tr = tr.replace(key, value)
        for key, value in ph_mo.items():
                p_m = p_m.replace(key, value)
        for key, value in lexic.items():
                lex = lex.replace(key, value)
        print('%s\t_'% (w) + '%s'% (tr) or (p_m) or (lex))
        #I want to have two columns - original and changes. Changes might be 3 diff categories, but I want to print them all in one goal

file.close()