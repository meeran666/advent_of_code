total_inputs="""LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

f=open("Day8/input.txt","r")
total_inputs=f.read()

def indexfind(distination,total_inputs):
  for i in range(0,len(total_inputs)):
    if total_inputs[i][0]==distination:
      return i

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

#finding starting point 
starting_index=indexfind("AAA",total_inputs)

#finding end point
current_index=starting_index
currenthead="AAA"
steps=0
findflag=False
while currenthead!="ZZZ":
  if findflag==True:
    break
  for x in path:
    if total_inputs[current_index][0]=="ZZZ":
      findflag=True
      break
    if x == "L":
       current_index=indexfind(total_inputs[current_index][1],total_inputs)
    if x == "R":
       current_index=indexfind(total_inputs[current_index][2],total_inputs)
    currenthead=total_inputs[current_index][0]
    steps+=1
  
print("steps")
print(steps)