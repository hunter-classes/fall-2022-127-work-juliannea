##Find Largest which takes in a list of numbers and returns the
#value of the smallest number

def findLargest(i):
    values = i[0] #sets first to be the first element in list

    for num in i:
        if num < values:
            values = num

    return values

list_i = [1,2,3,4,5,6,2,4,8]

print(findLargest(list_i))

#find frequency of v 

def freq(l,v):
    f = 0 #sets frequency count to 0 
    for i in l: #for every element in the list 
        if i == v: #see if i is equal to the number you want frequency of 
            f += 1 #add to count to f 
    return f

list_n = [1,1,1,1,1,3,3,3,3,4,2,2,2,2]

print(freq(list_n,1))

#fastmode 
def fastMode(dataset):
    n = 100
    lists = [0] * n

    for item in dataset:
        lists[item] += 1

    values = lists[0]
    for num in lists:
        if num > values:
            values = lists.index(num)
       

    return values

data = [1,1,1,2,2,2,2,3,3,4,4,4,4,4]

print(fastMode(data))
    
