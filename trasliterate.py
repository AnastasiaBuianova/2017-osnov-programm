import sys
import re

file = open('test.txt', 'r', encoding='utf-8')
letters = open('transliterated_letters.txt', 'r', encoding='utf-8')

index = 0
translit = {}

for line in letters:
    line = line.replace('\n', '')
    line = line.split('    ')
    translit[line[0]] = line[1]
    
for word in file:
    word = word.strip().split(' ')
    for w in word:
        w = re.sub('([?!,.—:;()])', '', w)
        while index >= 0:
            index += 1
            break
        tr = w
        for key, value in translit.items():
                tr = tr.replace(key, value)
        print('%d\t'% (index) + '%s\t_\t_\t_\t_\t_\t_\t_\t'% (w.lower()) + 'Translit=%s'% (tr))

file.close()
