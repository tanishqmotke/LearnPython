i = 0
while i < 6:
    print(i)
    i +=1

print("Break Concept")
j = 0
while j < 6:
    print(j)
    if j==4:
        break
    j+=1

print("Else Concept")
k=0
while k<6:
    k += 1
    if k==4:
     continue
    print(k)

print("Continue Concept")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
