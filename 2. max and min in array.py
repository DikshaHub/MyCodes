
def max_min_element(list):
    current_max = list[0]
    current_min = list[0]

    for ma in list:
        if ma > current_max:
            current_max = ma

    for mi in list:
        if mi < current_min:
            current_min = mi

    return current_max,current_min




n = int(input(" Please enter size of array : "))
Array = [n]

print(" Please enter the array in a single line separated by space : ")
Array = list(map(int,input().split()))


max_ele , min_ele = max_min_element(Array)

print("Maximum element is " + str(max_ele) + " and Minimum element is " + str(min_ele))

