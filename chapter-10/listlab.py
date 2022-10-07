##Find smallest value function
def min_s(m):
    values = m[0] 
    
    for num in m:
        if num < values: 
            values = num   
            
        
    return values 

list_min = [10,50000,-40,600] 

print(min_s(list_min))

##returns only odd numbers in a list

def only_odd(odd):
    ovalues = []
    for num in odd:
        if num % 2 != 0:
            ovalues.append(num)
            
    return ovalues

list_odd = [1,2,3,4,5,6,7,8,9]

print(only_odd(list_odd))

##function that returns all letters capitalized 
def cap_word(word):
    string = word.upper()
    return string

print(cap_word('wow'))

##function takes string and returns new string with every word thats longer than 5 characters turned into upper case

def findlen(word):
    cap = []
    for l in word:
        if len(l) > 5:
            letter = l[0].upper()
            full_l = letter + l[1:]
            cap.append(full_l)
            
    return cap 

listc = ['butterfly', 'pig', 'strawberry', 'cow']

print(findlen(listc))

##function takes list and returns it all squared

def square(number):
    sqr = []
    for n in number:
        n = n ** 2
        sqr.append(n)
    return sqr

sqrl = [2,3,4,5]

print(square(sqrl))

##function that takes 2 list and adds them to their correspondent

def add(o,t):
    list1 = o
    list2 = t
    totl = []
    
    for n in range (0, len(list1)): 
        totl.append(list1[n] + list2[n])
    return totl 
     
    
onel = [1,2,3,4]
twol = [10,20,30,40]

print(add(onel,twol))

##Chapter 10, 11, 12 

# 10- Count how many words in a list have length 5.

def count(word):
    listw = 0
    for l in word:
        if len(l) == 5:
            listw += 1
    return listw

wordlist = ['doors','butterfly', 'catss']
print(count(wordlist))

# 11 Sum all the elements in a list up to but not including the first even number.
def sums(num):
    total = 0
    if num[0] % 2 == 0:
        num.remove(num[0])
    for n in num:
        total = total + n 
    
    return total

listn = [2,1,3,4,5]
print(sums(listn))

#12 Count how many words occur in a list up to and including the first occurrence of the word “sam”.

listwo = ['sam', 'book','sam','book']

print(listwo.count('sam'))
      

    


    



        
            
    
            

        
    

        






            
    
    
















