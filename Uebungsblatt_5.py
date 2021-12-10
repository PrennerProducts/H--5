

def search_array(array, x):
    for i in range(0, len(array)):
        if array[i] == x:
            return i
        else:
            continue
    




#print(search_array([1,2,3,3,4,5,3 ], 9))

def selection_sort(array, asc):  
    if asc:
        for i in range(0, len(array)):
            current_value = array[i]
            j = i-1
            while current_value < array[j] and j >=0:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = current_value
        return array      
    else:
         for i in range(0, len(array)):
            current_value = array[i]
            j = i-1
            while current_value > array[j] and j >=0:
                array[j+1] = array[j]
                j -= 1
                array[j+1] = current_value
    return array 
    
    
    
    
    
#selection_sort([2,4,6,5,3,1], True)


        
    
    
    
    
    
# Diese Funktion implementiert Bubblesort
def bubbleSort(array):
    # Die Anzahl unser Durchgänge ist gleich Anzahl der Elemente -1
    for upperlimit in range(len(array)-1,0,-1):
        # Hier gehen wir das Array von links nach rechts durch
        # Aus Effizienzgründen gehen wir nie bis ganz ans Ende, und mit jedem Durchgang um eins weniger nach rechts
        for i in range(upperlimit):
            # Das hier könnten wir uns sparen, es steht hier nur, damit wir die aktuellen Elemente im Debugger sehen
            e1 = array[i]
            e2 = array[i+1]
            # Hier überprüfen wir, ob das erste Element größer als das zweite Element ist
            if e1 > e2:
                # Wenn das der Fall ist, vertauschen wir hier die Elemente
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    # Hier geben wir das sortierte Array zurück
    return array


# Hier führen wir Bubblesort aus
#result = bubbleSort([54, 26, 93, 17, 77, 31])
# Und geben das Ergebnis aus
#print(result)

stack = [5,5,9]

def push(stack, element):
    stack.append(element)
    
def pop(stack):
    if stack == []:
        return None
    else:
        temp = stack[-1]
        del stack[-1]
        return temp

def top(stack):
    if stack == []:
        return None
    else:
        return stack[-1]


def is_empty(stack):
    if stack == []:
        return True
    else:
        return False
    
def size(stack):
    return int(len(stack))
    
#size(stack)

def get_digits(n):
    l = []
    for i in str(n):
        l.append(int(i))
    return l


def digit_power_sum(digits, power):
    e = sum(digits)
    e = e ** power
    return e
    
def is_interesting_number(n):
    x = 1
    interesting = 2
    digits = get_digits(n)
    while interesting < n:
        interesting = digit_power_sum(digits, x)
        if interesting == 1:
            break
        x += 1
    if interesting == n:
        print("truhu")
        return True
    else:
        print("fahlsch")
        return False
    
 
            
    
    
    
get_interesting_numbers(400, 600)
    
