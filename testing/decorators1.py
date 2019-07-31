# Even number one side odd number one side
# x=sorted(range(1,10),key=lambda x:x%2==0)
# print(x)

# class Monkey_patching(object):
#     def f(self):
#         print("i am not monkey patch")
#
#
# def monkey_f(self):
#     print("yes i am monkey patch")
#
#
# Monkey_patching.f=monkey_f
# m=Monkey_patching()
# print(m.f())


# Python program to merge two unsorted lists
# in sorted order

# Function to merge array in sorted order
def sortedMerge(a, b, res, n, m):
    # Concatenate two arrays
    i, j, k = 0, 0, 0
    while (i < n):
        res[k] = a[i]
        i += 1
        k += 1
    while (j < m):
        res[k] = b[j]
        j += 1
        k += 1

    # sorting the res array
    res.sort()


# Driver code
a = [10, 5, 15]
b = [20, 3, 2, 12]
n = len(a)
m = len(b)

# Final merge list
res = [0 for i in range(n + m)]
sortedMerge(a, b, res, n, m)
print("Sorted merged list :")
for i in range(n + m):
    print(res[i])

# This code is contributed by Sachin Bisht
