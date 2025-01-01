total_inputs="""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

# f=open("Day8/input.txt","r")
# total_inputs=f.read()

total_inputs=total_inputs.split("\n")
                                                               
#creating path
path=total_inputs.pop(0)

#creating input table
total_inputs_temp=[]
for row in total_inputs:
  if row=="":
    continue
  row=row.split()
  row[2]=row[2][1:4]
  row[3]=row[3][:3]
  row.pop(1)
  total_inputs_temp.append(row)
total_inputs=total_inputs_temp


