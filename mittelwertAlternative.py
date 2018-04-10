# Anzahl der Wuerfelanzahlen

import random
import sys

n = int(sys.argv[1])     #an erster stelle da
b = []
for i in range (0,n-1):
  a = random.randint(1, 6)
  b.append(a)

#print("der Verktor aller Wuerfelergebnisse ist: " + str(b))

summeVonB = sum(b)

print("Summe aller Wuerfelergebnisse: " + str(summeVonB))
mittelwert = 0
mittelwert = summeVonB/n
print("der mittelwert der Wuerfelergebnisse ist: "+str(mittelwert))
