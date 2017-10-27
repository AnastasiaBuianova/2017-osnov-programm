import sys
import re
'''
#Original
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
'''

file = open('wiki.txt', 'r', encoding='utf-8')
#file = open('test.txt', 'r', encoding='utf-8')
letters = open('transliterated_letters.txt', 'r', encoding='utf-8')
#file = sys.stdin
sindex = 0

translit = {}

for line in letters:
    line = line.replace('\n', '')
    line = line.split('    ')
    translit[line[0]] = line[1]
    
for word in file:
    if word.strip() == '': continue
    index = 0
    word = re.sub('([?!,.—:;()])', ' \g<1> ', word)
    word = word.strip().split(' ')
    for w in word:
        if w.strip() == '': continue
        while index >= 0:
            index += 1
            break
        tr = w
        for key, value in translit.items():
                tr = tr.replace(key, value)
        print('%d\t'% (index) + '%s\t_\t_\t_\t_\t_\t_\t_\t'% (w.lower()) + 'Translit=%s'% (tr))
    sindex += 1
    print()
file.close()
