
import sys

WordSet = set()

def addWords(Words):
    global WordSet
    for word in Words:
        word = word.strip()
        WordSet.add(word)

for Line in sys.stdin.readlines():
    Line = Line.strip()
    Words = Line.split()
    addWords(Words)

print(len(WordSet))
    
