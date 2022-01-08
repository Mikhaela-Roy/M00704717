L1 = list(range(1,31))
print(L1)
L2 = [num for num in L1 if num%2 == 0]
print(L2)
L3 = []
L3.append(L2[0:5])
print(L3)

high = []
low = []
integers = [20,9,51,81,50,42,77]

for i in integers:
    if i%4 == 0 or i >50:
        print("high category")
        high.append(i)
        print(high)
    else:
        print("low category")
        low.append(i)
        print(low)


Tuple = (1,3,5,7)
test = list(Tuple)

