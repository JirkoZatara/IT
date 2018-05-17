# Weergeven van de rij van Fibonacci (Leonardo van Pisa) tot aan een door de gebruiker gedefinieerde waarde

def recur_fibo(n):
   """Recursieve functie om de Fibonacci reeks te printen"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# Deze waarde is door de gebruiker te veranderen. (Reeks tot aan waarde n)
ntotaan = 100

# uncomment onderstaande om input van de gebruiker te gebruiken
ntotaan = int(input("Fibonacci reeks berekenen tot aan waarde?: "))

# controleren of het aantal condities geldig is
if ntotaan <= 0:
   print("Vul een positieve integer in")
else:
   print("Zie hier de berekening van de enige echte Fibonacci reeks:")
   for i in range(ntotaan):
       print(recur_fibo(i))