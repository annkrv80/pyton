li = [x for x in range(1, 20)]
li = list(map(lambda x: x+10, li))
print(li)

#data=list(map(int,input().split()))#ввод с клавиатуры развелитель пробел
#print(data)

#data=list(map(int,input().split(',')))#ввод с клавиатуры развелитель запятая
#print(data)

#data = map(int,input().split(','))
#for i in data:
    #print(i)

data = map(int,'1 2 3 88 52 41 '.split())#map позволяет пробежать по данным только один раз.
for e in data: #если необходимо делать это многократно переводим в список
    print(e)

