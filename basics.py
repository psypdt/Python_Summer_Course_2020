#  Note: '' and "" seem to be interchangeable, doing " ' " is the same as ' \' '

#  Use [-1] (called reverse indexing) to get the last element of an array, -2 is the second last element
#  Slice follows [start:stop:step] where all are indexes, note that the stop index is NOT included, start <= x < stop
#  my_str[x:] means "grab everything from index x until and including the end of the string"
#  my_str[:x] means "grab everything from 0 until and excluding x"

some_num = 8
alph = "abcdefghijklmnopqrstuvwxyz"
num = "123456789"
name = "Boby"

print(alph[0:])  # Grab the entire string
print(alph[:3])  # Grabs the first 3 chars
print(alph[3:6])  # Grabs letters from (and including) index 3 to index 5
print(alph[4:])  # Grab all characters except for the first 4 (index 0-3)

print(num[::2])  # Grabs every second number
print(num[::-1])  # Reverses the string "take a backwards step"

mutate = 'F' + name[2:]  # Sting is immutable, so we need to get around that
print(mutate)
print(10*'h')

print('some_num: {}\nalph: {}'.format(some_num, alph))  # {} is just a place holder, like %d, %s etc.
print("Some {1} is {2} here, {0} cool right?".format("which is", "thing", "happening"))
print('The {q} {b} {f}'.format(f='fox', q='quick', b='brown'))


#  Floating point formatting {var:width.precision f} note that width means "how many numbers in total, ignoring the ."
print('100/7 is: {div:1.3f}'.format(div=100/7))  # Same as doing %.3f in C
print('Note that there are whitespaces to account for the 7 missing digits: {div:10.3f}'.format(div=100/7))

print(f'The f in front of the string allows us to pass in some_num: {some_num} directly')
print(f'Note that float formatting still works {some_num/3:1.2}, {some_num/3:1.5f}, {some_num/3:10.5}')


#  Note: Python 2 has something that may look like this:
print('Lets print a number: %d and a string %s' % (some_num, alph))  # Basically like what we do in C

# Using %r also converts whatever input into a string (like %s would) for now, there are some differences though

