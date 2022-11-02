#5, #7, 8

#5
def max(m):
    values = m[0] ##sets up the first values is the first element on the list 
    
    for num in m: ##for every element in the list of variable m 
        if num > values:  #check if the element is greater than the start valuue 
            value = num  #if it is then the value is changed to the number that was greater 
            
        
    return value #returns value after every element goes through loop 

list_max = [100,50,40,600] #shows the list of numbers 

print(max(list_max))

#7 count how many odd numbers on a list

def odd_n(odd):  #defines function 
    numbers = 0  #set it to 0 as the start 
    for v in odd:  #for every element in the list of the 'odd' variable 
        if v % 2 != 0: #check if the number divied by 2 is 0 to see if even 
            numbers += 1 #add right side opperand to left opperand and assign to left side 
            
    return numbers

list_odd =[2,4,3,5,9,10]

print(odd_n(list_odd))


#8 Sum up all even numbers in a list

def even_n(even):
    value = 0 #sets start value to 0 
    for v in even: # for every element in the list 
        if v % 2 ==0: #check if divisible by 2 with no remainder 
            value = value + v # if so add the value of v to 'value' 
    return value

even_l = [1,2,3,4,5,6]

print(even_n(even_l))
