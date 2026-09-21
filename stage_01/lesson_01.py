#Задача номер №1
x=[10,20]
y=x
y.append(30)
print(x)
y=[99]
print(x,y)
#[10,20,30],[99]

#Задача номер №2 а - не изменится, потому что в этой строчке b принимает значение a:b = b + "!" и 
# b будет равно "hello!", а а будет равно просто "hello"
a = "hello"
b = a
b = b + "!"
print(a,b)

#Задача номер №3
p = [1,2]
q = [1,2]
r = p
print(p==q, p is q, p is r) # True , False , True
print(id(p),id(q),id(r)) #совпадет r и p

#Задача номер №4

nums=[1,2,3,4]
z = nums
z.append(5)
print(z is nums,z)
print(id(z),id(nums))
nums_copy=nums.copy()
print(nums_copy==nums, nums_copy is nums)
