"""
Write a program to add the corresponding elements of two arrays, each of size $$N$$ and print the sums.
$$N$$ can be any integer between 1 and 100. $$1 \le N \le 100$$

Sample Input:
$$N$$ = 3
$$numArrayA$$ = 3 9 8
$$numArrayB$$ = 8 12 74

Sample Output:
11 21 82

"""

N = int(input())

numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

for i in range(0,N):
    sumArray.append(numArray1[i]+numArray2[i])


# Printing the sumArray
for element in sumArray:
    print(element, end=" ")

