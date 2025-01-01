total_input="""Time:      71530
Distance:  940200"""

f=open("Day_6/input.txt","r")
total_input=f.read()

def noof_possiblity_finder(time,distance):
  possiblity=0
  for timeindex in range(0,time):
      if distance<timeindex*(time-timeindex):
        possiblity+=1
  return possiblity

total_input=total_input.split("\n")
time_set=total_input[0].split()
distance=total_input[1].split()
time_set.pop(0)
distance.pop(0)
time_set=list(map(int,time_set))
distance_set=list(map(int,distance))
total=1

################################2nd part ###############################################
time_concat= "".join(str(x) for x in time_set)
distance_concat= "".join(str(x) for x in distance_set)
time_concat=int(time_concat)
distance_concat=int(distance_concat)
time_set=[time_concat]
distance_set=[distance_concat]
##########################################################################################
print(time_concat)
print(distance_concat)
distance_index=0
for time in time_set:
  print("sfdw")
  distance=distance_set[distance_index]
  total=total*noof_possiblity_finder(time,distance)
  distance_index+=1
print(total)