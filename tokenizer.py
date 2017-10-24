import sys
import re

file = open('wiki.txt', 'r', encoding='utf-8')
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