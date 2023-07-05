# create a function that reverses a string

# this is way too easy using splicing
# def usinglistsplicing_reverse(anystring):
#     reverse_string = anystring[::-1]
#     print(reverse_string)

# usinglistsplicing_reverse("Hi my name is Andrei")


# def easy_reverse(anystring):
#     n_string = []
#     for i in range(len(anystring)-1, -1, -1):
#         n_string.append(anystring[i])
#     print(''.join(n_string))

# easy_reverse("Hi my name is Andrei")

# Some built-in function
string1 = 'Hi my name is Andrei'
string2 = reversed(string1)
print(''.join(string2))

list1 = list(string1)
list1.reverse()
print(''.join(list1))