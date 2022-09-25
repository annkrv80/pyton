print('Hello world')
value = None
a = 123
b = 1.23
value = 12345
print (a)
print (b)
print(type(a))
print(type(b))
print(type(value))
s = 'Hello World'
print(s) # вывод строки
print(a,b,s)
print(a,'-',b,'-',s)
print('{}-{}-{}'.format(a,b,s))
print(f'{a}-{b}-{s}')
print('{1}-{2}-{0}'.format(a,b,s))
f = True
print(f)


list = [1,2,3]
print(list)
list = ['a','b','c']
print(list)


print('ВВедите а')
a = input()
print ('Введите b')
b = input()
print(f'{a} {b}')
print(a,'+',b,'=',a+b)

print('ВВедите а')
a =int (input())
print ('Введите b')
b =int (input())
print(f'{a} {b}')
print(a,'+',b,'=',a+b)

#Математические операции
a = 123
b = 321
c = a+b
print (c)

a = 123
b = -321
c = a+b
print(c)

a = 2
b = 8
c = a-b
print(c)

a = 2
b = 8
c = a/b
print(c)

a = 2
b = 8
c = a//b
print(c)

a = 2
b = 8
c = a%b
print(c)

a = 2
b = 8
c = a**b
print(c)

a = 1.3
b = 3
c = round(a*b)
print(c)

a = 1.3
b = 3
c = round(a*b,3)
print(c)

#Логические операции
a = 1>4
print(a)
a = 1<4
print(a)
a = 1<4 and 5>2
print(a)
a = 1==2  #сравнение
print(a)
a = 1 !=2 #неравенство
print(a)
a = 'two'
b = 'two'
print(a==b) #сравнение строк
a=[1,2]
b=[1,2]
print(a==b) #сравнение списков
a = 1<3<5
print(a)

f = 1>2 or 4<6
print(f) #дизЪюнкция вдух высказываний(логическое сложение) ложно только тогда когда оба высказывания ложны

f=[1,2,3,4]
print(f)
print(2 in f) # TRUE потому-что 2 содержится в списке

f=[1,2,3,4]
print(f)
print(not 2 in f) # отрицание(двойка не содержится в списке)

is_odd = f[0]%2==0 #проверка четности числа
print(is_odd)

is_odd = not f[0]%2 #проверка четности числа
print(is_odd)