total_input="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
#########################first part #################################
f=open("Day_2/input.txt","r")
total_input=f.read()
exact_no={"red": 12,"green": 13, "blue": 14}
game_no=0
total_input=total_input.split("\n")
total=0

for x in total_input:
  accepted=True
  line=x.split()
  for line_index in range(0,len(line)):
    if line_index==1:
      game_no=int(line[line_index].replace(":",""))
      continue
    if not line[line_index].isnumeric():
        continue
    color=line[line_index+1].replace(",","").replace(";","")
    if color=="blue" and int(line[line_index])>exact_no["blue"]:
          accepted=False
    if color=="red" and int(line[line_index])>exact_no["red"]:

          accepted=False
    if color=="green" and int(line[line_index])>exact_no["green"]:
          accepted=False
  if accepted==True:
    total=total+game_no
print(total)
################################### 2nd part ###########################################
f=open("Day_2/input.txt","r")
total_input=f.read()
total_input=total_input.split("\n")
total=0
for x in total_input:
  red=0
  blue=0
  green=0
  line=x.split()
  for line_index in range(0,len(line)):
    if not line[line_index].isnumeric():
        continue
    color=line[line_index+1].replace(",","").replace(";","")
    if color=="blue" and int(line[line_index])>blue:
      blue=int(line[line_index])
    if color=="red" and int(line[line_index])>red:
      red=int(line[line_index])
    if color=="green" and int(line[line_index])>green:
      green=int(line[line_index])
  total=total+(red*blue*green)

print(total)
