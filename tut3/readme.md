Welcome to tut3.  This tutorial, like all others in this repo is inspired by https://docs.python.org/3/tutorial/introduction.html. please read the og tutorial in case something is not clear.
1. Comments in python
Python interpretter treats characters written after a # sign as comments, and does not interpret that part of the code. Hence comments can be used to doucment what a line in the code does. This improves readability of the code.
2. Numeric operations in python.
Some common binary operators in python are the +, -, *, /, %
** is the power operator(exponent)
/ always returns float type.
// is for integer division. 
operations with int and float will return float
3. Strings
String are written in single quotes '' or double quotes "". \ is used to escape characters
print() function prints the argument as a string but removes the '' from it to make it look good.
Triple quotes can be used to make a string span multiple lines without explicitly using the \n character.
+ operator can concatenate 2 strings, * operator repeats the string.
Strings are 0 indexed. negative index means start looking from the last character. With -1 being the last character, -2 being the second last char and so on.
Strings can be sliced to obtain substrings and subsequences. Index out of range error is thrown when index is out of range. However, slicing out of range is handled in python.
Python strings are immutable. That is ince assigned, you can't change a character in the string by re assigning it.
len() function returns the length of the string.
4.Lists
Lists are a compound datatype in python. Lists are collections of comma separated objects enclosed in []. They are indexed and can be sliced just like a string
Lists are mutable.
5. misc.
Multiple assignments can be done in python. ex. a,b = b,a+b. In this the RHS is evaluated first. from left to right, then assignment happens.
Any block of code needs to be indented.
print() function can be given any number of arguements. It just appends a ' ' and prints them out together. you can also use a keyword arguement ( an arguement with a variable declaration) 'sep' to specify how to append 2 arguements together.
the precedence of ** operator is higher than -.
when using a """ to enter a multi line string. we can escape newline by ending the line with \.
