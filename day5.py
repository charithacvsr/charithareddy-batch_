###  day 5###
 # ! -----> common functions for list
'''
l1=[6,7,8,9,0]
print(len(l1))
print(len(l1))




l1=[6,7,8,"P","u"]
print(max(l1)) #---> error coz its a combination of int and string
print(min(l1)) #---> error coz its a combination of int and string


l1=[6,7,8,9,0,8.89,-5,0.78]
count() ----> how mant num of times an element is repeated
print(l1.count(6))

'''
'''''
#! some functions which is specifically used for list


* to add element inside the list
# ? insert(index_value,element)----> to add element at specific index position
l1=[6,6,6,8,9,0,8.89,-5,0.78]
l1.insert(2,"cars")
print(l1)


#? to delete element from list
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
pop()---> last element will be deleted
l1.pop()
print(l1)

pop(index_value)---> used to delte element at specific index
l1.pop(4) # 4 is index value
print(l1)
'''
'''

remove(element) ---> used to delete element directly
l1.remove(8.89)
print(l1)




clear() ---> to complete delete in list
l1.clear()
print(l1)




del -> to delete the list
del l1 # or del(l1)
print(l1)


#? ---> join 2 lists
l1=[9,0,8]
l2=["p","o","t",34]
print(l1+l2)



or
# extend() ---> to combine 2 lists
l1.extened(l2)
print(l1)




#?----> copy()
print(12)
print(l1)

print(id(l1))
print(id(l2))

'''

'''
#! diff b/w shallow copy and deep copy
shallow copy
import copy
l1=[8,9,0[5,6],[3,2,1]]
l2=copy.copy(l1)
l1.append(890)
print(l1)
print(l2)




# deep copy
import copy
l1=[8,9,0[5,6],[3,2,1]]
print(l1[-1][1] ---> to index nested list
      l2= copy.copy(l1)
      l1[-1].append('cars')
      print(l1)
      print(l2)

'''
'''
#? sort ---> arrange elements in list in ascending or descending order
l1=[9,7,45,0,-6,5,12]
l1.sort()# to arrange in ascending order
      print(l1)
l1=['i','0','i','p',9]
 l1.sort()
      print(l1)#---> error

'''

'''
#? list constructor
list()---> to conver other collection datatypes to list
      13=((8,9,0))
      print(list(14))


#! ---> nested list
      l1=[8,9,[0,8,7],["p","o",'y'],[8,'t']]
      print(l1[1:4])
       print(l1[1:-1])


#? to delete "t" from l1

l1=[-1].remove('t')
      print(l1)
'''
'''
#? combine these ["p","o",'y'],[8,'t'] lists in l1 to
      #["p","o",'y',8,'t']



l1[-2].extend(l1[-1]
              l1.pop(-1)
              print(l1)




'''
'''
#! ----> tuple
* char of tuple
* tuple have to be surrouned bt()
* the elements inside tuple are not changable
* the elements inside tuple are indexed
*the element will execute in order
* it is heterogeneous
* it allow duplicate elements
              
      
# * eg:
              
t1=(8,8,9,5.78,[9,0],(6,8),"hey",9+6j)
 print(t1)
 print(type(t1))
              
print(type(t1))
  '''
'''   
#! indexing,slicing are all same as list
              
l1=(8)
 print(type(l1)) # int
l1=(8,)
  print(type(l1)) #tuple
t1=8,9
      print(type(t1)) # tuple
t2=8,
      print(type(t2)) # tuple
l1=(8,)
 print(type(t2)) # tuple
              
 len(),min(),max(),index(),count() ---> all same as list
# to add elment inside tuple ---> cannot add
# cannot delete any element from tuple
              
#* join 2 tuples
t1=(8,9,0)              
t2=(6,7,8)
print(sum(l1))


'''
'''
#* sort tuple
              
              
t1=(8,9,0,89,12)
print(tuple(sorted(t1)))
print (tuple(sorted(t1,reverse=true)))
#? interate based on elements
              l1=[9,8,0,6,5]
            for i in l1:
print(i)
'''
'''
#! interate based on index value
              l1=[9,8,0,6,5]
              for in range (0,len(l1)):
              print(l1[i])
              

'''
'''
#! ----> strings
s1='o'
print(type(s1))
s1="u"
print(type(s1))


s1="hello world"

'''
'''
#* to access string
print(s1)
# indexing and slicing ----> same as list and tuple
str=("hello world")
print(stg[0:5]


'''
'''
#*=>  common functions




len(),min(),max(),index(),count()
 s1="hello world"
      print(len(s1))
      print(max(s1))
      print(max(s1))

'''

'''
ord() ----> used to find the ASCII value of a character
      s1="u"
      print(ord(s1))

'''
'''
#! function of string
      s1="hello world"

# to convert all characters to upper case
 print(s1.upper())



#? strip()---> to eliminate the space in begining and end of string
 s1="where are you?"
 print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())

'''



# splict function
s1="where are you"
print(s1.split())
print(s1.split("r"))




print(s1.count('e'))





#* replace ()----> to replace a specific char in the string
s1="where are you?"
print(s1.swapcase())




#* replace()----> to convert capital to small and small to capital at a 
ss1='never giveup'
print(s1.tittle())



#* capitalize()----> lst char of string will be coverted to capital
s1="hello"
s2="world"
print(s1+s2)


s1='''
how are you
iam fine
hey there
'''
'''


#* spliliness()---> used to split the string based onlines
print(s1.splitlines())


#* find()----> to find th index based on character
s1="hello world"
print(s1.find('z'))
#* print the string in reverse manner
s1="wlecome to all"
print(s1[::-1])

'''
#! ---->eg:1

s1=' restarter'
print(s1.count('r'))
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the
1500s, when an unknown printer took a galley of type and scrambled it
to make a type specimen book. It has survived not only five centuries,
but also the leap into electronic typesetting, remaining essentially
unchanged. It was popularised in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop
publishing software like Aldus PageMaker including versions of Lorem
Ipsum.
characters = len(s1)
print(characters)
words=s1.splict("")
print(len(words))

sentense = s1.split("")
for val in sentences:
    if val=='':
        index = sentences.index('')
        sentences.pop(index)
 print(len(sentenses))       
 for val ins1:
     if val =="":
         space=space+1
         print(space)



 




                    



              

































