#Задача номер 1
x = [10,20]
y = x
y.append(30)
print(x)
#[10,20,30]
y = [99]
print(x,y)
#[10,20,30],[99]

#Задача номер 2 а - так как строка неизменяемая, b создает новый объект, а "a" остается без 
# изменений и висит на старом объекте
a = "hello"
b = a
b = b + "!"
print(a,b)

#Задача номер 3
p = [1,2]
q = [1,2]
r = p
print(p == q, p is q, p is r) # True , False , True
print(id(p),id(q),id(r)) #совпадет r и p

#Задача номер 4

nums = [1,2,3]
alias = nums
alias.append(4)
print("alias is nums", alias is nums,alias)
print(id(alias),id(nums))
nums_copy = nums.copy()
print(nums_copy == nums, nums_copy is nums)
