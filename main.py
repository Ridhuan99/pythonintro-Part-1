#input and output
name = input('What is your name? ')
print('Hi ' + name)
print('----------------')
#Fundamental data types
#int and float
print(2+4)
print(2*4)
print(2-4)
print(2/4)
print('----------------')
#type() is used to identify the data types
print(type(2+4))
print(type(2*4))
print(type(2-4))
print(type(2/4))
print('----------------')
#performing mathematics operation between integer and float
print(2.1+4)
print(2+4.1)
print(2.9+4.1)
print(2.5*4)
print(2-4.5)
print('----------------')
#'//' return the integer for the result
print(2//4)
print(2/4)
print(3//4)
print(3/4)
print(5//4)
print(5/4)
print('----------------')
#'**' is the power off
print(2**4)
print('----------------')
# '%' return the remainder off
print(6%4)
print('----------------')
# Math function
#round and abs
print(round(3.1))
print(round(3.5))
print(round(3.9))
print(abs(-30))
print('----------------')
#Math Precedence
# () -> ** -> */ -> +-
print((10 - 2*3) + 2**4 /2 )
print('----------------')
#Math Precedence
#assigning variable
a,b,c = 1, 2, 3
print(a)
print(b)
print(c)
print('----------------')
#augmented assignment operator
cat = 5
cat+=2
print(cat)
print('----------------')
#string data type
name = 'andrei'
father_name = 'pilipovic'
fullname = name + ' ' + father_name
print(fullname)
longstring = '''
---
O O
uWu
'''
print(longstring)
print('----------------')
dummy = str(100)
dummy1 = int(100)
realdummmy = type(dummy1)
print(realdummmy)
print('----------------')
#escape sequence
sentence = "He\'s one of the \"fastest\" aside \nfrom me."
print(sentence)
print('----------------')
print('Formatted spring')
name = 'ridhuan'
age = 55
print(f'My name is {name}, i am {age} years old')
print('My name is {}, i am {} years old'.format('salman','23'))
print('My name is {}, i am {} years old'.format(name,age))
print('My name is {1}, i am {0} years old'.format(name,age))
print('----------------')
print('String Index')
#string{start:stop:stepover}
listnumbers = 'hantu'
print(listnumbers[2])
print(listnumbers[4])
print(listnumbers[0:3])
print(listnumbers[0:])
print(listnumbers[:4])
print(listnumbers[-1])
print(listnumbers[-3])
print(listnumbers[0:5:1])
print(listnumbers[0:5:2])
print(listnumbers[0:5:3])
print('----------------')
print('Built in function and immutability')
quote = "You are piece of shite"
#built in methods
print(quote.upper())
print(quote.capitalize())
print(quote.replace('shite','art'))
print(quote)
quote2 = quote.replace('shite','art')
print(quote2)
print('----------------')
print('Boolean')
#Boolean
is_cool = True
print(is_cool)
print(bool(1))
print(bool(0))
print('----------------')
print('Type conversion')
#First Exercise
birth_age = input('What year you wear born?')
birth_age = 2022 - int(birth_age)
print('You are ' + str(birth_age) + " years old")
print('----------------')
print('Password Checker')
#Second Exercise
username = input("Username: ")
password = input('Password: ')
pass_len = len(password)
hash_pass = '*' * pass_len
print(f'{username}, your {hash_pass} is {pass_len} letters long' )
print('----------------')
print('List')
#List
amazon_cart = ['shampoo','sunglasses','racket','soap']
print(amazon_cart[0])
print(amazon_cart[1])
print(amazon_cart)
print(amazon_cart[1:4])
amazon_cart[2] = 'ball'
print(amazon_cart)
new_cart = amazon_cart[1:4]
print(new_cart)
print('----------------')
print('Matrix')
#Matrix
seat = [[0,4,2],
        [3,1,6],
        [9,8,7]]
print(seat[1][1])
print(seat[2][2])
print('----------------')
print('List Methods')
#List methods
#adding
basket = [1,2,3,4,5]
print(len(basket))
basket.append(7)
print(basket)
new_basket = basket.append(8)
print(new_basket)
print(basket)
basket.insert(5,6)
print(basket)
new_basket = basket
print(new_basket)
#removing
#remove(value)
basket.remove(8)
print(basket)
#pop(index)
basket.pop(0)
print(basket)
basket.clear()
print(basket)
basket = ['a','b','c','d','e','f','a']
#return the index of letter 'b'
print(basket.index('b'))
#check if the letter 'f' in the list
print('f' in basket)
#return the count of letter 'a' in list
print(basket.count('a'))
#copy the list
dummy_basket = basket.copy()
print(dummy_basket)
#sort the list
dummy_basket.sort()
print(dummy_basket)
#reverse item in the basket
dummy_basket.reverse()
print(dummy_basket)
#combining a list with join()
words = ['i','like','to','cook']
sentence = ' '.join(words)
print(sentence)
print(range(100))
print(list(range(100)))
print('----------------')
print('List Unpacking')
a,b,*others = ['robert','manuel','kiyosaki','autumn']
print(a)
print(b)
print(others)
print('----------------')
print('Dictionaries')
#dictionary

firstdic = {
  'a': 3,
  'b': 'towel',
  'c': True
}

print(firstdic['a'])

statuslist = [
  {
    'name': ['ahmad','abu','jeeva'],
    'age': ['21','24','55'],
    'is_single': [True,True,False]
  },
  {
    'name': ['Gayah','Anita','Yen'],
    'age': ['25','32','34'],
    'is_single': [True,True,False]
  }
]

print(statuslist[0]['name'][1] + ' is ' + statuslist[0]['age'][1] + ' years old.')
print('----------------')
print('Dictionary methods')
#.get() dictionary methods
print(statuslist[1].get('age')[0])
print(statuslist[1].get('religion','not specified'))
#clear()
print(statuslist.clear())
#copy()
secdic = firstdic.copy()
print(secdic)
print('towel' in secdic.values())
print('b' in secdic.keys())
#update()
secdic.update({'d':'try'})
print(secdic)
#remove the last key and value
print(secdic.popitem())
print(secdic)
print('----------------')
print('Tuple')
#Tuple is like list but not immutable
mytuple = (1,2,3,4,5)
print(mytuple)
print('----------------')
print('Set')
#set cannot use index
setA = {1,2,3,4,5,5}
setB = {4,5,6,7,8,9}
setC = {8,9}
print(setA)
#isdisjoint()
print(setA.isdisjoint(setB))
#intersection same as &
print(setA.intersection(setB))
#difference()
setA.difference(setB)
print(setA)
#discard
setA.discard(5)
#difference_update()
setA.difference_update(setB)
print(setA)
#union() same as |
print(setA.union(setB))
print(setA | setB)
#subset()
print(setC.issubset(setB))
#issuperset()
print(setB.issuperset(setC))



















