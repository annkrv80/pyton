users='user1','user2','user3','user4'
ids=[2,5,7,8]
salary=[111,222,333]#zip обрезает ро наименьшему списку
data=list(zip(users,ids,salary))
data=list(enumerate(users))
print(data)
