total_inputs="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

f=open("Day_7/input.txt","r")
total_inputs=f.read()

def longestsubsequence(hand):
  minfreq=0
  minfreqchar="M"
  newhand=list(hand)
  for i in range(0,4):
    if hand[i]!="J":
      freq=1
      for j in range(i+1,4):
        if hand[i]==hand[j]:
          freq+=1
      if freq>minfreq:
        minfreq=freq
        minfreqchar=hand[i]
  print("minfreqchar")
  print(minfreqchar)
  for i in range(0,4):
    if hand[i]=="J":
      newhand[i]=minfreqchar
  return "".join(newhand)
  
def handtype_cheak(hand):
  newhand=hand
  for x in newhand:
    if x=="J":
      newhand=longestsubsequence(newhand)
  newhand=set(newhand)       
  if len(newhand)==1:
    return 6
  if len(newhand)==2:
    for x in newhand:
      match=0
      for y in hand:
        if x==y:
          match+=1
      if match ==1:
        return 5
    return 4
  if len(newhand)==3:
    for x in newhand:
      match=0
      for y in hand:
        if x==y:
          match+=1
      if match ==3:
        return 3
    return 2
  if len(newhand)==4:
    return 1
  if len(newhand)==5:
    return 0
def power(card):
    if card=="J":
      return 1
    if card=="2":
      return 2
    if card=="3":
      return 3
    if card=="4":
      return 4
    if card=="5":
      return 5
    if card=="6":
      return 6
    if card=="7":
      return 7
    if card=="8":
      return 8
    if card=="9":
      return 9
    if card=="T":
      return 10
    if card=="Q":
      return 11
    if card=="K":
      return 12
    if card=="A":
      return 13
def sortinghands_ofset(group):
  for i in range(0,len(group)):
    for j in range(i+1,len(group)):
        hand1=group[i][0]
        hand2=group[j][0]
        swap=False
        for cardno in range(0,5):
          if power(hand1[cardno])<power(hand2[cardno]):
            break
          if power(hand1[cardno])>power(hand2[cardno]):
            swap=True
            break
        if swap == True:
          group[i],group[j]=group[j],group[i]

# creating input table 
total_inputs=total_inputs.split("\n")
total_input_temp=[]
handtype_table=[]

#creating numeric table
for row in total_inputs:
  row=row.split()
  total_input_temp.append(row)
total_inputs=total_input_temp

#crating handpower table
handtype_table=[[],[],[],[],[],[],[]]
for hand in total_inputs:
  handtype_table[handtype_cheak(hand[0])].append(hand)

# sorting of all the indivisual set of handpower_table
for i in range(0,7):
  sortinghands_ofset(handtype_table[i])
print("handpower_table")
print(handtype_table)

# rank multiplying 
rank=1
total=0
for set in handtype_table:
  for y in set:
    if len(y)>0:
      total=total+(rank*int(y[1]))
      rank+=1
print(total)


