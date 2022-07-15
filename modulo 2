
import random

def bubble_sort(v):
    
    fim = len(v)
    
    while fim > 0:
        
        i = 0
        #percorrendo vetor de 0 até fim
        while i < fim-1:
            if v[i] > v[i+1]:
                #realizando a troca da posição atual pela a proxima
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
                print(v)
            i += 1
        fim -= 1

vetor = list(range(0,10))
random.shuffle(vetor)

bubble_sort(vetor)

print (vetor)
