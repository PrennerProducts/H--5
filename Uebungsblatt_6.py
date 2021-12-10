def nested_sum(array):
    int_sum = 0
    for i in array:
        if type(i) == int:
            int_sum += i
        elif type(i) == list:
            for j in i:
                if type(j) == int:
                    int_sum += j
                elif type(j) == list:
                    for k in j:
                        if type(k) == int:
                            int_sum += k
                        elif type(k) == list:
                            for l in k:
                                if type(l) == int:
                                    int_sum += l
                                elif type(l) == list:
                                    for m in l:
                                        if type(m) == int:
                                            int_sum += m
            
    print(int_sum)

#nested_sum([5, [4, "3"], 4, [3, [2.5, [1, 1]]]])

"""6.4 Teilbarkeit von Teilersummen (20%)¶
Die folgende Aufgabe wurde vorletztes Jahr bei der Klausur gestellt.

Sei die Funktion sigma(n) die Summe aller Teiler der positiven Ganzzahl n.

Zum Beispiel: Die Teiler von 4 sind 1, 2 und 4, daher gilt: sigma(4) = 1 + 2 + 4 = 7.

Sei die Funktion S(m, d) die Summe aller Zahlen i  ≤  m für die gilt: d teilt sigma(i) ohne Rest.

Zum Beispiel, die Zahlen k  ≤  20, für die gilt, dass sigma(k) durch 7 ohne Rest geteilt werden kann, sind: 4, 12, 13 und 20. Deren Summe ist 49. Also gilt S(20, 7) = 49.

Implementieren Sie die Funktion S(m, d) in Python."""

def sigma(n):
    sum_teiler = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum_teiler += i
    return sum_teiler

#sigma(20)


def S(m,d):
    sum_alle = 0
    for i in range(1, m+1):
        if sigma(i) % d == 0:
            sum_alle += i
    return sum_alle
#S(20, 7)


"""6.5 Primzahlzwillinge (20%)¶
Die folgende Aufgabe wurde letztes Jahr bei der Nachklausur gestellt.

Sei  𝑝  die Menge aller Primzahlen und  𝑝𝑖  die i-te Primzahl (aufsteigende Sortierung). Beispiel:
𝑝  = {2, 3, 5, 7, 11, 13, ...} und  𝑝1  = 2,  𝑝2  = 3,  𝑝5  = 11.

Ein Primzahlzwilling ist ein Paar aus Primzahlen, deren Abstand 2 ist. Die kleinsten Primzahlzwillinge 
sind (3, 5), (5, 7) und (11, 13).

Implementieren Sie die Funktion twinPrimeSum(n), die die Summe aller Primzahlzwillinge im Intervall von 
𝑝1  bis  𝑝𝑛  (inklusive) zurückgibt. Dabei darf jede Primzahl nur einmal aufsummiert werden.

Beispiel:  𝑡𝑤𝑖𝑛𝑃𝑟𝑖𝑚𝑒𝑆𝑢𝑚(6)=3+5+7+11+13=39 . Die  5  kommt in zwei Primzahlzwilligen vor, wird aber nur 
einmal in der Summe berücksichtigt."""   



def is_prime_number(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6. 
    f = 5
    while f <= r:
        #print('\t',f)
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True 
            
    
#is_prim_number(13)


def twinPrimeSum(n):
    prime_list= []
    prime_list_2 = []
    for i in range(2, n+1):
        if is_prime_number(i):
            prime_list.append(i)
    i = 0
    while i < len(prime_list):
        if (prime_list[i]-2) ==  prime_list[i-1]:
            prime_list_2.append(prime_list[i])
            prime_list_2.append(prime_list[i-1])
            print(prime_list_2)
            i +=1
        else:
            i += 1
    
            
    
#twinPrimeSum(6)


"""6.1 Rekursive Bestimmung von ungeraden Zahlen (20%)¶
Implementieren Sie ein Programm, welches für jede beliebige natürliche Zahl bestimmen kann,
ob diese ungerade ist. Falls eine Zahl ungerade ist, soll der Wahrheitswert "True" zurückgegeben werden.
Falls es sich um eine gerade Zahl handelt, dann "False". Im Gegensatz zu Übungsblatt 4 soll der 
Algorithmus dieses Mal mit Hilfe einer Rekursion umgesetzt werden. Wählen Sie einen passenden 
Rekursionsschritt und Rekursionsanfang

Hinweis: Implementieren Sie Ihre Lösung als wechselseitige Rekursion. Definieren Sie sich 
hierzu eine passende zweite Funktion."""


def is_odd(x):
    if x == False:
        return False
    elif x == True:
        return True
    else:
        true_or_false(x)
    return true_or_false(x)
   
def true_or_false(x):
    if x % 2 == 0:
        return False
    else:
        is_odd(True)

is_odd(4)
    
    
