total_input="""226.241.893%..........257..312............69........792............/...........+...................$257..................790........./...184
................................................854*.............909.139..*276.680..&.........432............580....248.................*...
....136*755...@.950......................173.............95..........+...............2.877.......*668......+..+.........918*.......62....571"""

f=open("Day_3/input2.txt","r")
total_input=f.read()
f.close()
##################################################old way ###########################################
# total_input=total_input.split("\n")
# isnumber=False
# arr_2d=[]
# total=0
# for x in total_input:
#   arr_2d.append(list(x))
# for i in range(0,len(arr_2d)):
#   rowlen=len(arr_2d[i])
#   val=""
#   for j in range(0,rowlen):
#     if arr_2d[i][j].isnumeric():
#       val=val+arr_2d[i][j] 
#     if isnumber==False and arr_2d[i][j].isnumeric():
#       if j-1>-1  and arr_2d[i][j-1]!="." and not arr_2d[i][j-1].isnumeric():
#         isnumber=True
#       if j+1<rowlen  and arr_2d[i][j+1]!="." and not arr_2d[i][j+1].isnumeric():
#         isnumber=True
#       if i-1>-1  and arr_2d[i-1][j]!="." and not arr_2d[i-1][j].isnumeric():
#         isnumber=True
#       if i+1<len(arr_2d) and arr_2d[i+1][j]!="." and not arr_2d[i+1][j].isnumeric():
#         isnumber=True
#       if i+1<len(arr_2d) and j-1>-1 and arr_2d[i+1][j-1]!="." and not arr_2d[i+1][j-1].isnumeric() :
#         isnumber=True
#       if i+1<len(arr_2d) and j+1<rowlen and arr_2d[i+1][j+1]!="." and not arr_2d[i+1][j+1].isnumeric() :
#         isnumber=True
#       if j-1>-1 and i-1>-1 and arr_2d[i-1][j-1]!="." and not arr_2d[i-1][j-1].isnumeric():
#         isnumber=True
#       if  i-1>-1 and j+1<rowlen  and arr_2d[i-1][j+1]!="." and not arr_2d[i-1][j+1].isnumeric():
#         isnumber=True
#     if val!="" and j==rowlen-1 or not arr_2d[i][j].isnumeric():
#       if isnumber==True:
#         total=total+int(val)
#         isnumber=False
#       val=""
# print(total)   
######################################new way ###########################################################
# def isvalid_index(row,column,rowlen):
#   if row>-1 and row<len(arr_2d) and column>-1 and column<  rowlen:
#     return True
#   return False
# def isself(row,column):
#   if row==i and column==j:
#     return True
#   return False
# def issymbol(row,column):
#   if not arr_2d[row][column].isnumeric() and arr_2d[row][column]!=".":
#     return True
#   return False
# def islastcolumn_element_valid(j,rowlen,isnumber):
#   if j==rowlen-1  and isnumber==True:
#     return True
#   return False
# def boxtraversing(i,j,isnumber,string_list,rowlen):
#   if isnumber==False:
#     for subindex_row in range(i-1,i+2):
#       for subindex_column in range(j-1,j+2):
#         if not isvalid_index(subindex_row,subindex_column,rowlen):
#           continue
#         if isself(subindex_row,subindex_column):
#           continue
#         if not issymbol(subindex_row,subindex_column):
#           continue
#         isnumber=True
#   string_list[0]=string_list[0]*10+int(arr_2d[i][j])
#   return isnumber

# arr_2d=total_input.split("\n")
# isnumber=False
# total=0

# for i in range(0,len(arr_2d)):
#   rowlen=len(arr_2d[i])
#   val=0
#   string_list=[val]
#   for j in range(0,rowlen):
#     if arr_2d[i][j].isnumeric():
#       isnumber=boxtraversing(i,j,isnumber,string_list,rowlen)
#       if not islastcolumn_element_valid(j,rowlen,isnumber):
#         continue
#       total=total+string_list[0]
#       isnumber=False

#     else:
#       if isnumber==True:
#         total=total+string_list[0]
#         isnumber=False
#       string_list[0]=0
          
# print(total)
#################################################################### 2nd part ###############################################################
def isvalid_index(i,j,rowlen,total_input):
      if j<rowlen and i<len(total_input) and j>-1 and i>-1:
        return True
      return False
def isvalid_gearratio(valupdateno):
  if valupdateno[0]==2:
    return True
  return False
def lastcolumn_valsetter(index,box_i,val,total_input,rowlen):
  leftindex=index
  rightindex=index+1
  exp=0
  while total_input[box_i][leftindex].isnumeric():
    val[0]=int(total_input[box_i][leftindex])*pow(10,exp)+val[0]
    exp=exp+1
    leftindex=leftindex-1
    if leftindex==0:
      break
  if rightindex >= rowlen:
    return 
  while total_input[box_i][rightindex].isnumeric():
    val[0]=val[0]*10+int(total_input[box_i][rightindex])
    rightindex=rightindex+1
    if rightindex==rowlen:
      break
def valsetter(i,index,val,total_input):
  if not total_input[i][index+1].isnumeric():
        exp=0
        while total_input[i][index].isnumeric():
          val[0]=int(total_input[i][index])*pow(10,exp)+val[0]
          exp=exp+1
          index=index-1
          if index==-1:
            break
def boxtraversing(i,j,total_input,gearratio,valupdateno):
  for box_i in range(i-1,i+2):
    for box_j in range(j-1,j+2):
      if isvalid_index(box_i,box_j,rowlen,total_input):
        val=[0]
        index=box_j
        if box_j==j+1:
          lastcolumn_valsetter(index,box_i,val,total_input,rowlen)
        else:
          valsetter(box_i,index,val,total_input)
        if val[0]!=0:
          valupdateno[0]=valupdateno[0]+1
          gearratio[0]=gearratio[0]*val[0]

# total_input="""467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""
total=0
total_input=total_input.split("\n")
for i in range(0,len(total_input)):
  rowlen=len(total_input[i])
  for j in range(0,rowlen):
    if total_input[i][j]=="*":
      gearratio=[1]
      valupdateno=[0]
      boxtraversing(i,j,total_input,gearratio,valupdateno)
      if isvalid_gearratio(valupdateno):
        total=total+gearratio[0]
          
print(total)
      
    
