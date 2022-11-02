# Chapter 7 Exercises 
##7
def is_even(n):
    return(n % 2 == 0)

is_even(2)

##8
def is_odd(n)
  return(n % 2 !== 0)

is_odd(3)

##10

def is_rightangled(a, b, c):
    
    return ((a ** 2 + b ** 2) - (c ** 2)) < 0.001

is_rightangled(2,3,5)

##  11

def is_rightangled(a, b, c):
    
    if b > a and b > c:
        return abs((a ** 2 + c ** 2) - (b ** 2)) < 0.001
    elif a > b and a > c:
        return abs((b ** 2 + c ** 2) - (a ** 2)) < 0.001
    else:
        return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001
     

is_rightangled(2,3,5)

## Strings_1 "hello_name"
greeting = "Hello{0}!"

print(greeting.format(' Bob'))
print(greeting.format(' Alice'))
print(greeting.format(' x'))

##make_out_word
def make_out_word(out, word):
  return out[0:2] + word + out[2:5]

##first_two
def first_two(str):
  return str if len(str)<=2 else str[:2]

