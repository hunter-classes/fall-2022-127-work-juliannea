##Bondify
def bondify(name):
    location = name.find(' ') #Finds space in name typed 
    last = name[location+1:].capitalize() #makes last name the space + first letter to the end and capitlizes it 
    last_name = last[0] #only prints out the first letter 
    first = name[0:location].capitalize() #makes the first name from first letter to the location with a space and capitlize it 
    


    
    b_name = last_name + "." + first
    
    return b_name

print(bondify("james bond"))

##Piglatin 

def piglatin(word):
    
    first_l = word[0].lower()   #Find first letter of the word
    vowel = 'a' or 'e' or 'i' or 'o' or 'u' ##Defines what first letters are vowel in the word
    r_word = word[1:2].upper()
    f_word = word[2:]
    
    if first_l == vowel: ##if the first letter is a vowel 
        p_word = r_word + f_word +'yay'## add yay to the end of the word
        
        return p_word ##returns the word 
    
    else:
        p_word = r_word + f_word + 'ay' #Has the word from the letter after the first letter + first letter at end + ay at the ens 
        return p_word
    
pword = input('Type in word to turn into piglatin') #ask for word 

print(piglatin(pword)) #calls function on input of word 

