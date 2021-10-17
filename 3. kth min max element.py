# Program to find kth max and min element

def merge(left, right):
    # if first is empty return second array
    if len(left) == 0:
        return right

    # if first is empty return second array
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # check both arrays until they're added to result
    while len(result) < (len(left) + len(right)):

        # sorting the elements using both arrays
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If end of either array is reached, then add elements from other array and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    # if input has less than 2 elements return it without split
    if len(array) < 2:
        return array
    # find midpoint
    midpoint = len(array) // 2
    # recursively split input into two equal halves
    # we'll sort them individually and merge them
    return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))


print(" Program to find kth max and min element \n ")

n = int(input(" Please enter size of array : "))
Array = [n]

print(" Enter elements of the array in a single line separated by space : ")
Array = list(map(int, input().split()))

if len(Array) == n:
    print(" Given array is " + str(Array))

    # sort the array
    sorted_array = merge_sort(Array)

    k = int(input(" Enter the value of k "))
    print(str(k) + " min element is ", sorted_array[k - 1])
    print(str(k) + " max element is ", sorted_array[n - k])

else:
    print(" Enter " + str(n) + " elements only. ")



# sorted_array = sorted(Array)
# print(sorted_array)


# Time complexity : O(nlogn)
