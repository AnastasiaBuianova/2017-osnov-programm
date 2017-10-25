import sys
import re
#It works but the problem of tagging is that it also tags smaller parts of a word, 
#e.g. if a word contains something like 'í' that look like a CONJ, it will tag it as 'partofwordCONJtherest'

file = open('50_sentences.txt', 'r', encoding='utf-8')
letters = open('transliterated_letters.txt', 'r', encoding='utf-8')
items = open('TAGGED50sentences.txt', 'r', encoding='utf-8')
index = 0
translit = {}
tagged_items = {}

for line in letters:
    line = line.replace('\n', '')
    line = line.split('    ')
    translit[line[0]] = line[1]
    
for item in items:
    item = item.replace('\n', '')
    item = item.split('\t')
    tagged_items[item[0]] = item[1]

for word in file:
    word = word.strip().split(' ')
    for w in word:
        w = re.sub('([?!,.—:;()])', '', w)
        while index >= 0:
            index += 1
            break
        tr = w
        it = w
        for key, value in tagged_items.items():
                print(key, value)
                it = it.replace(key, value)
        for key, value in translit.items():
                tr = tr.replace(key, value)
        print('%d\t'% (index) + '%s\t_\t'% (w) + '%s\t_\t_\t_\t_\t_\t' % (it) + 'Translit=%s'% (tr))

file.close()
