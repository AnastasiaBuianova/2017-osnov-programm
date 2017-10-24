import sys
import re
import nltk
from nltk import tokenize

#Второй вариант - честный

file = open('wiki.txt', 'r', encoding='utf-8')
lines = []
abbreviations = {'с. ш.':'#1#', 'з. д.':'#2#'}
abbreviations2 = {'т.є.':'#1#', 'т. є.':'#2#', 'т. з.':'#3#', 'т.з.':'#4#', 'ітд.':'#5#'}

for paragraph in file:
    paragraph = re.sub(r'([0-9]+)\.', r'\1[ORD]', paragraph)
    for key, value in abbreviations.items():
        paragraph = paragraph.replace(key, value)
    lines.append(paragraph)
    #print('###', lines)
    
    for line in lines:
        line = re.sub('[.]', '.$', line)
        sentences = line.split('$ ')        
    
        for s in sentences:
            s = re.sub(r'\[ORD\]', '.', s)
            for key, value in abbreviations.items():
                s = s.replace(value, key)
                print (s)


file.close()