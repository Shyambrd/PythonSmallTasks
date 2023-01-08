import random

#A function do shuffle all the characters of a string
def shuffle(string):
    # create a temp List to shuffle and mix up password
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#getting letters for passwords by Ascii values

uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90)) 
lowercaseLetter1= chr(random.randint(97,122))
lowercaseLetter2= chr(random.randint(97,122))
digit1 = chr (random.randint(48,57))
digit2 = chr (random.randint(48,57))
punctuationSign1 = chr (random.randint(34,47))
punctuationSign2 = chr (random.randint(58,64))

#Generate password using all the variables
password = uppercaseLetter1 +uppercaseLetter1+ uppercaseLetter2 +lowercaseLetter1+ lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
password = shuffle(password)

#Ouput
print(password)