#Programmer Sadiq
#By@Sadiqul Islam
#Use of int() function



#int() function
#int() function convert any string or number to integer
#Syntax of int() function: int(string or float)
#It takes a string or number  and return a integer value
#For example


#Example 1

number_one = input("Enter the number of one: ")
number_two = input("Enter the number of two: ")



total = int(number_one) + int(number_two)

print(total)

#Example 2

a = int(input('enter the value of a : '))
b = int(input('enter the value of b : '))

summation = a + b
print('The result is :',summation)


#Example 3

c = float(input('enter a float number of c : '))
d = float(input('enter a float number of d : '))

result = int(c) + int(d)
print(result)


#Example 4

e = int(0b1010)
print(e)

f = int('1010',2)
print(f)

#Example 5
g = int(0o1000)
print(g)

h = int('1000',8)
print(h)

#Example 6
i = int(0x6B)
print(i)

j = int('6B',16)
print(j)
