
import random
import string
print("Welcome to Password Picker")

adjectives = ['slEEy', 'sLoW', 'sMELly', 'wEt', 
              'fAt', 'rEd', 'OraNGe', 'yeLLow', 'gRee7N', 
              'bLUe', 'pURpLe', 'FLuffy', 'WhiTe', 'p8ROUd', 'BRavE']

nouns = ['aPp*Le', 'DiN#oSAur', 'BaLl', 'tOAs+tEr', 
         'Go(At', 'Dra$GoN', 'h/aMMer', 'Du=Ck', 'pa+NdA']
         
adjective = random.choice(adjectives)
noun = random.choice(nouns)

number = random.randrange(0, 100)
special_char = random.choice(string.punctuation)

password = adjective + noun + str(number) + special_char
print("Your Password is : %s" % password)
