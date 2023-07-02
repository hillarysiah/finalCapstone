# I found it interesting how when something is similar they will receive a higher score. For those who has 
# little similarity ie. cat and banana I was surprised to find that there were some similarity - perhaps
# because there is a monkey and banana in the list and the program tries to link it back to the cat

import spacy
nlp = spacy.load ('en_core_web_md')

tokens = nlp ('london tokyo sushi pasta')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

nlp = spacy.load ('en_core_web_sm')

tokens = nlp ('london tokyo sushi pasta')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        

# i noticed that the values for en_core_web_md similarities are lower and some values are even in negataives - perhaps en_core_web_md 
# is a more sensitive and rigid measure for testing similarities. 
