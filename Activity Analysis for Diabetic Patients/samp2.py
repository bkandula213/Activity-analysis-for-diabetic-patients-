from collections import Counter




import sqlite3
con = sqlite3.connect('diact1') 



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
p_id=int(input("Enter patient id:"))   
cnt1 = 0
total_b1time=float(input("enter total bending 1 time(in mins):"))
with open("bending1.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  #v.append(val)
  if val == 1:
    cnt1 = cnt1 + 1
#print(key,val)
#print(type(key),type(val))
#print(cnt1)
n=pweight[p_id-1]/10
b1time_mins  = n+((float(cnt1) * 250.0)/1000.0)/60.0
#calories = (((float(page[p_id-1])*0.217)-(float(pweight[p_id-1])*0.09036)+(float(220.0-float(page[p_id-1]))*0.65*0.6309) - 55.0969)*float(b1time_mins)) / 41.84
total_b1time=total_b1time*b1time_mins
print('Effective Minutes spent in bending1 is:' + str(round(b1time_mins,3)))
print('Total time spent in bending1: '+str(round(total_b1time,3)))
#print(b1time_mins)

cnt1 = 0
total_b2time=float(input("enter total bending 2 time(in mins)"))
#calories = (((float(page[p_id-1])*0.217)-(float(pweight[p_id-1])*0.09036)+(float(220.0-float(page[p_id-1]))*0.72*0.6309) - 55.0969)*float(b2time_mins)) / 41.84
total_b1time=total_b1time*b1time_mins
with open("bending2.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
b2time_mins  = n+((float(cnt1) * 250.0)/1000.0)/60.0
total_b2time=total_b2time*b2time_mins
print('Effective Minutes spent in bending2 is:' + str(round(b2time_mins,3)))
#calories = (((float(page[p_id-1])*0.217)-(float(pweight[p_id-1])*0.09036)+(float(220.0-float(page[p_id-1]))*0.65*0.6309) - 55.0969)*float(b1time_mins)) / 41.84
print('Total time spent in bending2: '+str(round(total_b2time,3)))

cnt1 = 0
'''
#calories = (((float(page[p_id-1])*0.217)-(float(pweight[p_id-1])*0.09036)+(float(220.0-float(page[p_id-1]))*0.80*0.6309) - 55.0969)*float(cytime_mins)) / 41.84
cytime_mins  = ((float(cnt1) * 250.0)/1000.0)/60.0
total_cytime=total_cytime*cytime_mins'''
with open("cycling.csv") as f:
  c = Counter(line.split()[0] for line in f)
for key,val in c.items():
  if val == 1:
    cnt1 = cnt1 + 1
total_cytime=float(input("enter total time spent in cycling(in mins):"))
cytime_mins  = n+((float(cnt1) * 250.0)/1000.0)/60.0
total_cytime=total_cytime*cytime_mins
print('Effective Minutes spent in cycling is:' + str(round(cytime_mins,3)))
print('Total time spent in cycling: '+str(round(total_cytime,3)))




