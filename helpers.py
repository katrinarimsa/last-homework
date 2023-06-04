def neg_checked(table):
    for element in table:
        if float(element) < 0:
            print("Only provide positive values")
            return 1
        else:
            return 0

def insert_sort(arr): #taken from pp7 homework
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr