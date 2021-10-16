

def Reverse(list,start,end):
    while start < end:
        # swap
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
    return list


n = int(input(" Please enter size of the array : "))
print(" Please enter the values of array in a single line using space : ")

Array = [n]
Array = list(map(int, input().split()))

print(" Entered array is : ", Array)

print(" Reveresd array  is : " + str(Reverse(Array, 0, n-1)))

# Time Complexity O(n)


# list slicing
# def Reverse(A):
#  print( A[::-1])