#text = 'съешь ещё этих мягких французских булок'
#print(len(text)) # 39
#print('ещё' in text) # True
#print(text.isdigit()) # False
#print(text.islower()) # True
#print(text.replace('ещё','ЕЩЁ')) #
#for c in text:
# print(c)

#text = 'съешь ещё этих мягких французских булок'
#print(text[0]) # c
#print(text[1]) # ъ
#print(text[len(text)-1]) # к
#print(text[-5]) # б
#print(text[:]) # print(text)
#print(text[:2]) # съ
#print(text[len(text)-2:]) # ок
#print(text[2:9]) # ешь ещё
#print(text[6:-18]) # ещё этих мягких
#print(text[0:len(text):6]) # сеикакл
#print(text[::6]) # сеикакл
#text = text[2:9] + text[-5] + text[:2] # ...

#Списки: введение
#numbers = [1, 2, 3, 4, 5]
#print(numbers) # [1, 2, 3, 4, 5]

#numbers = list(range(1, 6))
#print(numbers) # [1, 2, 3, 4, 5]

#numbers[0] = 10
#print(numbers) # [10, 2, 3, 4, 5]
#for i in numbers:
# i *= 2
# print(i) # [20, 4, 6, 8, 10]
#print(numbers) # [10, 2, 3, 4, 5]

#Списки: введение
#colors = ['red', 'green', 'blue']
#for e in colors:
# print(e) # red green blue
#for e in colors:
# print(e*2) # redred greengreen blueblue
#colors.append('gray') # добавить в конец
#print(colors == ['red', 'green', 'blue', 'gray']) # True
#colors.remove('red') #del colors[0] # удалить элемент

#Функции
#def f(x):
 #return x**2
def f(x):
 if x == 1:
    return 'Целое'
 elif x == 2.3:
    return 23
 else:
     return
print(f(1)) # Целое
#print(f(2.3)) # 23
#print(f(28)) # None
#print(type(f(1))) # str
#print(type(f(2.3))) # int
#print(type(f(28))) # NoneType