total_input="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
f=open("Day_5/input.txt","r")
total_input=f.read()
###############################################################
def convert_rows_into_numeric(row,total_input2,setarr):
  row=row.split()
  if not row[1].isnumeric():
    setarr=[]
    total_input2.append(setarr)
  if row[0].isnumeric():
    row=list(map(int,row))
    setarr.append(row)
  return setarr

def cheak_range(row,key):
  if row[1]<=key[0] and key[0]<row[1]+row[2]:
    key[0]=row[0]+(key[0]-row[1])
    return True
  return False

def key_to_location(total_input,key,location):
  for set in total_input:
    for row in set:
      if cheak_range(row,key):
        break
  # location.append(key[0])
  return key[0]

def make_numerictable(total_input):
  total_input2=[]
  setarr=[]
  for row in total_input:
    if row=="":
      continue  
    setarr=convert_rows_into_numeric(row,total_input2,setarr)
  return total_input2



total_input=total_input.split("\n")
keys=total_input[0].split()
keys.pop(0)
keys=list(map(int,keys))

#creating numeric table
total_input=make_numerictable(total_input)

#finding seed to location map and put the location into
location=[]
for val in keys:
  key=[val]
  location.append(key_to_location(total_input,key,location))

print(min(location))
print(keys)
###################################################2nd part ##############################333333333
# total_input=total_input.split("\n")
# keys=total_input[0].split()
# location=[]
# keyupdate=0
# i=1
# while(i<len(keys)):
#   for key in range(int(keys[i]),int(keys[i])+int(keys[i+1])):  
#     for row in total_input:
#       if row == "":
#         continue
#       if row == "seed-to-soil map:" or row == "soil-to-fertilizer map:" or row == "fertilizer-to-water map:" or  row == "water-to-light map:" or  row == "light-to-temperature map:" or row=="light-to-temperature map:" or row=="temperature-to-humidity map:" or row== "humidity-to-location map:":
#         keyupdate=0
#       row=row.split()
#       if row[0].isnumeric() and keyupdate==0:
#         # print(int(row[0]))
#         # print(int(row[1]))
#         # print(int(row[2]))
        
#         if int(row[1])<=int(key) and int(key)<int(row[1])+int(row[2]):
#           key=int(row[0])+(int(key)-int(row[1]))
#           keyupdate=1
#     location.append(key)
#   print(i)
#   i+=2
# print(min(location))

    