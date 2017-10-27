import sys
import re

file = open('50_sentences.txt', 'r', encoding='utf-8')
letters = open('transliterated_letters.txt', 'r', encoding='utf-8')
items = open('TAGGED50sentences.txt', 'r', encoding='utf-8')
#f = open('tagged_corpus.txt', 'w', encoding='utf-8')
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

for word in file: # for each of the lines in the input
    if word.strip() == '': continue # if the line is blank, skip it 
    index = 0 # index is the token id
    it = word # it is the line
    #for key, value in tagged_items.items():
     #   it = re.sub(key, value, it)
    
    word = re.sub('([?!,.—:;()«»])', ' \g<1> ', word) # replace all punctuation with punct + space
    word = word.strip().split(' ') # split the line into tokens
    for w in word: # for each token in the line
        if w.strip() == '': continue # if the token is blank
        while index >= 0: # increase the index by 1 
            index += 1
            break
        tr = w # tr is the current token
        it = w # it is the current token
        for key, value in translit.items(): # for each of the key,value pairs in translit
            tr = tr.replace(key, value) # replace the key with value in the transliterated token

        tag = 'X'
        if it in tagged_items:
                tag = tagged_items[it]

        print('%d\t'% (index) + '%s\t_\t'% (w) + '%s\t_\t_\t_\t_\t_\t' % (tag) + 'Translit=%s'% (tr))
    sindex += 1
    print()
    #f.write('%d\t'% (index) + '%s\t_\t'% (w) + '%s\t_\t_\t_\t_\t_\t' % (tag) + 'Translit=%s'% (tr))
        
#f.close()  
file.close()