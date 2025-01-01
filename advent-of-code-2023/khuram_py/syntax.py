l=[24,234,43]
for i in range(len(l)):
  if l[i]%5==0:
    l[i]//=5
    if l[i]%3==0:
      l[i]//=3
    else:
      l[i]//=2
for i in l:
  print(l,end='#')