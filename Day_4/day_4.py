total_input="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# f=open("Day_4/input.txt","r")
# total_input=f.read()
# f.close()


# def pushingin_winningarr(line,index,winning_arr):
#   while(line[index]!="|"):
#     winning_arr.append(int(line[index]))
#     index+=1
#   index+=1
#   return index
# def pushingin_myarr(line,index,myarr):

#    while(index!=rowlen):
#     myarr.append(int(line[index]))
#     index+=1
# def machingfunc(winning_arr,myarr,):
#   point=0
#   for x in winning_arr:
#     if x in myarr:
#       if point==0:
#         point=1
#       else:
#         point*=2
#   return point
# total=0
# total_input=total_input.split("\n")
# for x in total_input:
#   line=x.split()
#   index=2
#   winning_arr=[]
#   myarr=[]
#   rowlen=len(line)
#   print(line[2])
#   index=pushingin_winningarr(line,index,winning_arr)
#   pushingin_myarr(line,index,myarr)
#   point=machingfunc(winning_arr,myarr)
#   print(point)
#   total=total+point
# print("\n")
# print(total) 
############################################# 2nd part ##########################################
def pushingin_winningarr(line,index,winning_arr):
  while(line[index]!="|"):
    winning_arr.append(int(line[index]))
    index+=1
  index+=1
  return index
def pushingin_myarr(line,index,myarr):
   while(index!=rowlen):
    myarr.append(int(line[index]))
    index+=1
def machingfunc(winning_arr,myarr):
  matchingno=0
  for x in winning_arr:
    if x in myarr:
      matchingno+=1
  return matchingno

total_input=total_input.split("\n")
input_arr_2d=[]
card_instance_struct={}
for x in total_input:
  line=x.split()
  cardno=line[0]+line[1]
  print(cardno)
  card_instance_struct[cardno]=0
  input_arr_2d.append(line)

for i in range(0,len(input_arr_2d)):
  rowlen=len(input_arr_2d[i])
  index=2
  winning_arr=[]
  myarr=[]
  index=pushingin_winningarr(input_arr_2d[i],index,winning_arr)
  pushingin_myarr(input_arr_2d[i],index,myarr)
  matchingno=machingfunc(winning_arr,myarr)
  
  cardstart_no=input_arr_2d[i][0]+input_arr_2d[i][1]
  cardno=input_arr_2d[i][0]+input_arr_2d[i][1]
  card_instance_struct[cardno]+=1
  if i==rowlen-1:
    break
  for x in range(0,card_instance_struct[cardno]+1):
    for below_index in range(i+1,i+matchingno+1):
      cardno=input_arr_2d[below_index][0]+input_arr_2d[below_index][1]
      card_instance_struct[cardno]+=1
      if below_index==rowlen-1:
        break
total=0
for no in range(1,len(input_arr_2d)+1):
  cardno="Card"+str(no)+":"
  print(cardno)
  total+=card_instance_struct[cardno]
print(total)