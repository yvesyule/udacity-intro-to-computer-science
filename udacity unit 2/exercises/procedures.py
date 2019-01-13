#square

def _square(a):

   return a * a 
x = 5

print(_square(x))

#sum

def _sum(a,b,c):

   return a + b + c 

d = 3
r = 3
e = 4

print(_sum(d,r,e))




# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

def abbaize(a , b):
    
    return a + b + b + a

print abbaize('a' ,'b')
print abbaize('cat', 'dog')







#print abbaize('a','b')
#>>> 'abba'

#print abbaize('dog','cat')
#>>> 'dogcatcatdog'




# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(danton, audace):
    
    return danton.find('audace')
danton = "De l'audace, encore de l'audace, toujours de l'audace"

print find_second(danton, 'audace')

#answer
def find_second(search, target):
    first = search.find(target)
    second = search.find(target, target + 1)

    return second

 danton = "De l'audace, encore de l'audace, toujours de l'audace"   

print find_second(danton, 'audace')

#you can complete it in one line code
def find_second(search, target):

    return search.find(target, search.find(target) + 1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"   

print find_second(danton, 'audace')
# end



#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#print find_second(danton, 'audace')
#>>> 25

#twister = "she sells seashells by the seashore"
#print find_second(twister,'she')
#>>> 13



# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(x, y):
    
    x = 2
    y = 7
    
    if x < y:
    
    bigger = y
    
    return bigger
    
print bigger(x, y)
    
#answer

def bigger(x, y):
    
    if x > y :
        return x
    
    else:
        return y

print bigger(2, 7)

#or
def bigger(x, y):
    
    if x > y :
        return x
      return y  
print(bigger(2, 7))

#or
def bigger(x, y):
    
    if x > y :
        r = x
    else:
        r = y
        return r
print(bigger(2, 7))





#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3



# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

def is_friend(name):
    
    if name[0] == 'D':
        return True
    else:
        return False

#with one line return name[0] == 'D'

print is_friend('Diane')
print is_friend('Fred')

#print is_friend('Diane')
#>>> True

#print is_friend('Fred')
#>>> False