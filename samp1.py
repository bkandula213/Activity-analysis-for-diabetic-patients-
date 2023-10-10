from collections import Counter
lis1 = []
lis2 = []
with open("samp1.csv") as f:
    c = Counter(line.split()[0] for line in f)

for key,val in c.items():
    if val == 1:
        lis1.append(key)
    else:
        lis2.extend([key]*val)
print(lis1)
print(lis2)


