def firstKey(dict):
    dict = dict
    first_key = 0
    list_keys = []
    for key in dict:
        list_keys.append(dict[key])
    return list_keys[0]
def max_Y(arr):
    max=''
    for i in range(len(arr) - 1):
        if i == 0:
            max = arr[i]
        if max < arr[i + 1]:
            max = arr[i + 1]
    return max
def maxSort(arr):
    result = []
    temp_1 = 0
    temp_2 = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            temp_1 = arr[i]
            temp_2 = arr[i+1]
            arr[i+1] = temp_1
            arr[i] = temp_2
    return arr