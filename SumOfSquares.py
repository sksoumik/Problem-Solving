# Write a program to print the sum of squares of the elements of an array of size N.
#  N can be any integer between 1 and 100. 1≤N≤100
N = input()
numArray = map(int, input().split())
sum_integer = 0
for i in numArray:
    sum_integer = sum_integer + (i*i)

print(sum_integer)