fruits =["apple","banana","mango","apple",1 ,2 ,3 ,4]
print(fruits)
print(len(fruits))
print(type(fruits))

thisList = list(("tanishq","motke"))
print(thisList)
print(thisList[:1])

Lst = [ i*i for i in range(10) if i%2==0] 
print(Lst)

#append
Numbers = [1,2,3,4,5]
Numbers.append(6)
print(Numbers)

#sort
Numbers = [2,3,4,5,1]
Numbers.append(6)
Numbers.sort()
print(Numbers)

#index
Number = [1,2,3,1]
print(Number.index(1))
print(Number.count(1))

#insert
Numbers = [1,2,3,4]
Numbers.insert(2,323)
print(Numbers)

#extend
colors = ['red']
Rainbow =['yellow']
colors.extend(Rainbow)
print(colors)



