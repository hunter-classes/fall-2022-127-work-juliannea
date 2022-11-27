#Extra 1 done was having the option to translate into different languages:pirate, chef, and fudd 
#EXTRA 2 done was handling upper/lower case and punctuation

#created pirate dictionary 
pirate_dict = {
    "Hi": "Ahoy",
    "my": "me",
    "boss": "admiral",
    "captain": "cap'n",
    "erase": "scuttle",
    "erased": "scuttled",
    "myself": "meself",
    "your": "yer",
    "you": "ye",
    "friend": "matey",
    "friends": "maties",
    "worker": "shipmate",
    "workers": "shipmates",
    "person": "landlubber",
    "people": "landlubbers",
    "guys": "scurvey dogs",
    "before": "afore",
    "earlier": "afore",
    "old": "auld",
    "the": "th'",
    "of": "o'",
    "don't": "dern't",
    "never": "ne'er",
    "ever": "e'er",
    "over": "o'er",
    "yes": "aye",
    "yeah": "aye",
    "yup": "aye",
    "no": "nay",
    "nah": "nay",
    "nope": "nay",
    "had": "ha'nae",
    "haven't": "ha'nae",
    "didn't": "di'nae",
    "wasn't": "weren't",
    "for": "fer",
    "between": "betwixt",
    "around": "aroun'",
    "to": "t'",
    "don't know": "dinna",
    "it's": "tis",
    "woman": "wench",
    "wife": "lady",
    "girl": "lass",
    "girls": "lassies",
    "dude": "lubber",
    "boy": "lad",
    "boys": "laddies",
    "am": "be",
    "are": "be",
    "children": "little sandcrabs",
    "kids": "minnows",
    "him": "that scurvey dog",
    "her": "that comely wench",
    "he's": "he be",
    "she's": "she be",
    "they're": "they be",
    "was": "were bein'",
    "hey": "avast",
    "ocean": "high seas",
    "food": "chow",
    "road": "sea",
    "freeway": "high seas",
    "street": "river",
    "streets": "rivers",
    "damn": "arrrr",
    "pirate": "buccaneer",
    "beer": "grog",
    "punished": "keel-hauled",
    "dollar": "doubloon",
    "dollars": "doubloons",
    "money": "gold",
    }

#created chef.l dictionary

chef_dict = [
    ('an', 'un'),
    ('au', 'oo'),
    ('a','e'),
    ('en','ee'),
    ('ew','oo'),
    ('e', 'i'),
    ('f', 'ff'),
    ('ir', 'ur'),
    ('ow','oo'),
    ('the','zee'),
    ('th', 't'),
    ('v', 'f'),
    ('w', 'v'),
    ('c', 'k'),
    ('o', 'oo'),
    ('i', 'ee')
    
]

#fudd dictionary

fudd_dict = [
    ('r', 'w'),
    ('l', 'w'),
    ('qu', 'qw'),
    ('th', 'f'),
    ('n.' , 'uh-hah-hah-hah.')
]
    
    
#read story 
p_story = open('input.txt','r') 
f = p_story.readlines()
newList=[]
for line in f:
    newList.append(line.strip())

text = ' '.join(newList)


#function 
def story(s,t,ct,ft):

    option = input('What translation do you want: pirate, chef, or fudd?') #asks for user input 
    p_s = s.split() #split into list

    #if user mistypes

    if option != 'pirate' or 'chef' or 'fudd':
        print('Not an option')

    option = input('What translation do you want: pirate, chef, or fudd?')

    #pirate translation 
    if option == 'pirate':
        translations = t #set equal to chef dictionary

        pt = ' '.join(translations.get(word,word) for word in p_s) #replaces specific word in list with translation stored in dictionary

        pt = pt.split('. ') #split string into list removing period 

        pt = [p.capitalize() for p in pt] # capitlizes every first letter in list 

        pt = '''. 
'''.join(pt)  #turns list back into multiline sentences 

        return pt

    #chef translation
    if option == 'chef':
        translation = ct #sets equal to chef dictionary 

        c = s #sets equal to story 

        for x, y in translation: 

            c = c.replace(x,y) #replaces x with y 

        c = c.split('. ')

        c = [ct.capitalize() for ct in c]        

        c = '''.
'''.join(c)

        return c

    #fudd translation
    if option == 'fudd':
        translation = ft #sets equal fudd dictionary 

        f = s #sets equal to story 

        for x, y in translation:

            f = f.replace(x,y)

        f = f.split('. ')

        f = [ft.capitalize() for ft in f]        

        f = '''.
'''.join(f)

        return f
                

              
print(story(text,pirate_dict,chef_dict,fudd_dict))


   
    
