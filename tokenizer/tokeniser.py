'''
#Original
import sys
import re

file = open('test.txt', 'r', encoding='utf-8')
index = 0
for word in file:
    word = word.strip().split(' ')
    for w in word:
        w = re.sub('([?!,.—:;()])', '', w)
        while index >= 0:
            index += 1
            break
        print('%d\t'% (index) + '%s\t_\t_\t_\t_\t_\t_\t_\t_\t_\t_' % (w.lower()))
file.close()
'''

#With Fran's improvements
import sys
import re

file = open('wiki.txt', 'r', encoding='utf-8')
#file = sys.stdin
sindex = 0
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
        print('%d\t'% (index) + '%s\t_\t_\t_\t_\t_\t_\t_\t_\t_\t_' % (w.lower()))
    sindex += 1
    print()
file.close()