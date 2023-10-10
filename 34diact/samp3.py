from collections import Counter

import MySQLdb as mdb
con = mdb.connect('localhost', 'team1', 'test623', 'diact1'); 

with con:
  cur = con.cursor()
  cur.execute('SELECT pweight,page FROM patient where pid = 001;');
  result = cur.fetchall()
  for row in result:
    pweight = row[0] 
    page = row[1]
 
cnt1 = 0
with open("bending1.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
b1time_mins  = ((float(cnt1) * 250.0)/1000.0)/60.0
calories = (((float(page)*0.217)-(float(pweight)*0.09036)+(float(220.0-float(page))*0.65*0.6309) - 55.0969)*float(b1time_mins)) / 41.84
print('Calories spent in bending1 is:' + str(calories))

cnt1 = 0
with open("bending2.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
b2time_mins  = ((float(cnt1) * 250.0)/1000.0)/60.0
calories = (((float(page)*0.217)-(float(pweight)*0.09036)+(float(220.0-float(page))*0.72*0.6309) - 55.0969)*float(b2time_mins)) / 41.84
print('Calories spent in bending2 is:' + str(calories))

cnt1 = 0
with open("cycling.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
cytime_mins  = ((float(cnt1) * 250.0)/1000.0)/60.0
calories = (((float(page)*0.217)-(float(pweight)*0.09036)+(float(220.0-float(page))*0.80*0.6309) - 55.0969)*float(cytime_mins)) / 41.84
print('Calories spent in cycling is:' + str(calories))




