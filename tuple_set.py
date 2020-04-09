# tuple is almost same as list, tuple is imutale but list is mutable
tup = (21,36,13,14,25)
tup
(21, 36, 13, 14, 25)
tup[1]
36
tup[1] = 50
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
# value assignment is not possible in tuple
tup.count(50)
0 # if given input is not in tuple...
tup
(21, 36, 13, 14, 25)
tup.count(14)
1

#set:
# set is a collection of unique element
s = {10,25,50,45,2,1}
s
{1, 2, 10, 45, 50, 25}
s = {15,15,2,6,1,5}
s
{1, 2, 5, 6, 15}
# in set value is not repeated
# set is uses the concept like HASH, it is use for increasing the value fetching performance
s[1]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'set' object is not subscriptable
# in set indexing is not perform because sequence is not fix