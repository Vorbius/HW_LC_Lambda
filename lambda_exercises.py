''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
numbers=[1,2,3,4,5,6,7,8,9,10]
filter_odd=list(filter(lambda num: not num %2, numbers))

filter_even=list(filter(lambda num: num % 2, numbers))

print(filter_even)
print(filter_odd)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


count = lambda i: len(i)

for i in weekdays:
    if count(i) ==6:
        print(i)






''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

colors= ['orange', 'red', 'green', 'blue', 'white', 'black']
remove=['orange','black']

new_colors=list(filter(lambda x: x not in remove ,colors))
print(new_colors)

#print(new_colors)





''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''


list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2= [2, 4, 6, 8]

new_list=list(filter(lambda x: x not in list2,list1))
print(new_list)

''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
o_list=['red', 'black', 'white', 'green', 'orange']
test1=list(filter(lambda x: 'ack' in x,o_list))
test2=list(filter(lambda x: 'abc' in x,o_list))
print(test1)
print(test2)





''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world"
str1 = "HELLO"
str1= "hello"

check= lambda x: any( x.islower for x in str1) and any (x.isupper for x in str1) and len(str1)>=8
#check=list(map(lambda x: any(str(x).lower in str(x) and str(x).upper in str(x) and len(x)>8),str1))
if check(str1):
    print("Password Accepted")
else:
    print("Password missing important part")








''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

l=sorted (original_scores, key = lambda x: x[1])

print(l)