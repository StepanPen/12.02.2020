num_even = -1
num_noteven = -1
element = -1
while element != 0:
    element = int(input())
    if element % 2 == 0:
        num_even += 1
        if element % -1 == 0:
            num_noteven += 1
print(num_even, num_noteven)