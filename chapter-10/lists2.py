def average(numlist): ##sets up function 

    total = 0 ##sets starting point to 0 
    for num in numlist: ##tells function to loop until all numbers in list are done 
        total = total + num #adds all numbers in list together 

    return total / len(numlist) ##divides the total to the length of list 


list=[5,5,5]

print(average(list))
        
##6

def sum_of_squares(xs):
    
    total = 0
    
    for num in xs:
        total = total + num**2
        
    return total

list2= [2,3,4]
print(sum_of_squares(list2))
