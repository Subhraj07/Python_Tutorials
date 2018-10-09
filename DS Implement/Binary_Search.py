# need to sort

def Binary_search(arr, start_index, last_index, element):
    if last_index >= start_index:
        mid = int(start_index + (last_index - start_index) / 2)

        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            return Binary_search(arr, start_index, mid - 1, element)
        else:
            return Binary_search(arr, mid + 1, last_index, element)

    else:
        return -1


arr = [2, 14, 19, 21, 99, 210, 512, 1028, 4443, 5110]
element = 4443
start_index = 0
last_index = len(arr) - 1
found = Binary_search(arr, start_index, last_index, element)
if found == -1:
    print("element not present in array")
else:
    print("element is present at position " + str(found + 1))
