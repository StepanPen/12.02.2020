max = 0
min = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
        if element < min:
            min = element
print(max, min)
