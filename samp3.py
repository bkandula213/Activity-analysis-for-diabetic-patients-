from collections import Counter

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'diact1');

import sqlite3
con = sqlite3.connect('diact1') 
p_id=int(input("Enter patient id:"))
with con:
  cur = con.cursor()
  cur.execute('SELECT pid,pweight,page FROM patient');
  result = cur.fetchall()
  pid=[]
  pweight=[]
  page=[]
  for row in result:
    pid.append(int(row[0]))
    pweight.append(int(row[1]))
    page.append(int(row[2]))

#print("pweight is",pweight)
cnt1 = 0
total_b1time=float(input("enter total bending 1 calories: "))
with open("bending1.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
b1time_mins  = ((float(cnt1) * 250.0)/1000.0)/60.0
calories = (((float(page[p_id-1])*0.217)-(float(pweight[p_id-1])*0.09036)+(float(220.0-float(page[p_id-1]))*0.65*0.6309) - 55.0969)*float(b1time_mins)) / 41.84
total_b1time=total_b1time*calories
print('Calories spent in bending1 is:' + str(calories))
print('Total calories spent in bending1: '+str(round(total_b1time,3)))

cnt1 = 0
total_b2time=float(input("enter total bending 2 calories: "))
with open("bending2.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
b2time_mins  = ((float(cnt1) * 250.0)/1000.0)/60.0
calories = (((float(page[p_id-1])*0.217)-(float(pweight[p_id-1])*0.09036)+(float(220.0-float(page[p_id-1]))*0.72*0.6309) - 55.0969)*float(b2time_mins)) / 41.84
total_b2time=total_b2time*calories
print('Calories spent in bending2 is:' + str(calories))
print('Total calories spent in bending2: '+str(round(total_b2time,3)))

cnt1 = 0
total_cycalories=float(input("enter total cycling calories: "))
with open("cycling.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
cytime_mins  = ((float(cnt1) * 250.0)/1000.0)/60.0
calories = (((float(page[p_id-1])*0.217)-(float(pweight[p_id-1])*0.09036)+(float(220.0-float(page[p_id-1]))*0.80*0.6309) - 55.0969)*float(cytime_mins)) / 41.84
total_cycalories=total_cycalories*calories
print('Calories spent in cycling is:' + str(calories))

print('\nTotal calories spent in cycling: '+str(round(total_cycalories,3)))
exit()



