with open('input.txt') as f:
    lines = f.read().split('\n')

temp = [s.split() for s in lines]

l1, l2 = [], []
for i, j in temp:
    l1.append(int(i))
    l2.append(int(j))
    
l1.sort()
l2.sort()


## Part 1 ##
total = 0

for i in range(len(l1)):
    total += abs(l1[i] - l2[i])
    
print(total)

## Part 2 ##
total = 0

freq = {}
for num in l2:
    freq[num] = freq.get(num, 0) + 1
    
for num in l1:
    total += num * freq.get(num, 0)
    
print(total)