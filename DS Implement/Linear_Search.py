# https://www.thecrazyprogrammer.com/2017/05/python-linear-search.html#
#  time complexity O (n)

items = [5, 7, 10, 12, 15]
print("list of items is", items)

x = int(input("enter item to search:"))

i = 0
flag = 0

while i < len(items):
    if items[i] == x:
        flag = 1
        break
    i = i + 1

if flag == 1:
    print("found location ", i + 1)
else:
    print("Not found")
