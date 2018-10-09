# https://www.thecrazyprogrammer.com/2017/12/python-bubble-sort.html

arr = [21, 14, 18, 25, 9]
n = len(arr)  # length

pass_val = 1

while pass_val <= n - 1:
    index = 0
    while index <= n - pass_val - 1:
        if arr[index] > arr[index + 1]:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]
        index = index + 1

    pass_val = pass_val + 1

for item in arr:
    print(item)
