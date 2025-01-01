total_input="""1abc2
pqr3stu8vwx
treb7uchet
a1b2c3d4e5f"""
arr=[]
total=0

f=open("input.txt","r")
total_input=f.read()
for x in total_input:
  if x.isnumeric():  
    arr.append(int(x))
    continue
  if x =="\n":
    total=total+(arr[0]*10)+arr[-1]
    arr=[]
total=total+(arr[0]*10)+arr[-1]

print(total)