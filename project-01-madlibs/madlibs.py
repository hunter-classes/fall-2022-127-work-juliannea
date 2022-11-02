import random #imports random function

def story_maker(s,h,iv,pln,tv,persn,adj):

    sl = s.split() #takes each word in string to a list

    for i in range(len(sl)): #sets up for loop to look at every element in the length of the list 'ls'
   
        if sl[i] == '<iverb>':
            sl[i] = random.choice(iv)

        if sl[i] == '<iverb>.': #accounts for if 'IVERB' is at the end of sentence with period ('<iverb>.')
            sl[i] = random.choice(iv) + '.'
       
        if sl[i] == '<plnoun>':
            sl[i] = random.choice(pln)
        
        if sl[i] == '<plnoun>.': #accounts for if 'PLNOUN' is at the end of a sentence with period ('<plnoun>.')

            sl[i] = random.choice(pln) + '.'
    
        if sl[i] == '<tverb>':
            sl[i] = random.choice(tv)

        if sl[i] == '<tverb>.': #accounts for if 'TVERB' is at the end of a sentence with period ('<tverb>.')
            sl[i] = random.choice(tv)
        
        if sl[i] == '<pnoun>':
            sl[i] = random.choice(persn)

        if sl[i] == '<pnoun>.': #accounts for if 'PNOUN' is at the end of a sentence with period ('<pnoun>.')
            sl[i] = random.choice(pers_n) + '.'

        if sl[i] == '<adjective>':
            sl[i] = random.choice(adj)

        if sl[i] == '<adjective>.':
            sl[i] = random.choice(adj) + '.' #account for if '<adjective>' is at the end of a sen
            
    #Sentence Structure

    sl = ' '.join(sl) #Joins list of words into a sentence

    sl = sl.split('. ') # Splits each sentence into a list of sentences, removing the period and space

    sl = [s.capitalize() for s in sl] #EXTRA capitalizes every first letter of element in list

    sl = '''.
'''.join(sl) ##makes the sentence mulitline

    #Hero extra 

    heron = [] #creates empty list
    
    heron = heron + h #adds list with all hero names into empty list, needed to use the .replace function
    
    heron = [h.capitalize() for h in heron] #makes sure to capitalize proper noun of Hero name 

    sl = sl.replace('<hero>',random.choice(heron)) #replaces every instance of 'HERO' in string with a random choice of hero name from hero list
                                                    #EXTRA randomly chooses only once for every instance so hero name is the same throughout  

    return sl


#Read Text File EXTRA
story_file = open('story.txt','r') # EXTRA opens text file to read, file has story in it 
f = story_file.readlines() #creates a variable which has the lines read 

newList=[] #new variable with empty list in order
for line in f:
    newList.append(line.strip())
    
sentence = ' '.join(newList) #makes list into string of sentences


#List of Parts of Speech 

hero = ['aelin', 'mannon', 'dorian','chaol','rowan','nesryn','elide','lorcan']

intransitive_v = ['ran','walked','jumped','drove','crawled','waddled']

pl_n =['castle','house','woods','cabin','living room','library','ballroom']

transitive_v = ['talked','danced','listened','fought','bickered','laughed','read']

pers_n = ['hunter','prince','thief','witch','dragon','vampire','assassin','royal','doctor','teacher','trainer']

adj = ['beautiful','smart','funny','manipulative','magnificent']


print(story_maker(sentence,hero,intransitive_v,pl_n,transitive_v,pers_n,adj))
