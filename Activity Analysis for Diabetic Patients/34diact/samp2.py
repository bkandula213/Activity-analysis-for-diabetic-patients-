from collections import Counter

cnt1 = 0
with open("bending1.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
b1time_mins  = ((float(cnt1) * 250.0)/1000.0)/60.0
print('Effective Minutes spent in bending1 is:' + str(b1time_mins))

cnt1 = 0
with open("bending2.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
b2time_mins  = ((float(cnt1) * 250.0)/1000.0)/60.0
print('Effective Minutes spent in bending2 is:' + str(b2time_mins))

cnt1 = 0
with open("cycling.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
cytime_mins  = ((float(cnt1) * 250.0)/1000.0)/60.0
print('Effective Minutes spent in cycling is:' + str(cytime_mins))



