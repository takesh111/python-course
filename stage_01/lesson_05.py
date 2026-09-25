# Задача 1
a = [1,2]
a.append([3, 4])
print(a, len(a))
# [1,2, [3, 4]] , 3
b = [1,2]
b.extend([3, 4])
print(b, len(b))
#[1, 2, 3, 4] 4
c = [1, 2, 3]
c.insert(0, 0)
print(c)
#[0, 1, 2, 3]
print(c.pop())
# 3
print(c.pop(0))
# 0
print(c)
# [1, 2]

# Задача 2
nums = [3, 1, 2]
result = nums.sort()
print(nums)
# [1, 2, 3]
print(result)
# None
print(sorted([3, 1, 2], reverse=True))
[3, 2, 1]

# Задача 3
data = [[1], [2]]
copy_slice = data[:]
print(data is copy_slice, data[0] is copy_slice[0])
# False , True во втором случае True так как [0] - указывает на [1] и это является подсписком
copy_slice.append([3])
copy_slice[0].append(99)
print(data)
# 1 ,99, 2
print(copy_slice)
# 1, 99, 2, 3

# Задача 4 - Кортежи
t = (5)
t2 = (5,)
print(type(t),type(t2))
# int, tuple
x, y = 10, 20
x, y = y, x
print(x, y)
# 20, 10
first, second, *rest = [1, 2, 3, 4, 5]
print(first, second, rest)
# 1, 2, [3, 4, 5]

# Задача 5
ips = ["10.0.0.5", "192.168.1.1", "10.0.0.7"]
ips.append("10.0.1.15")
ips.extend(["10.0.2.15", "10.0.3.15"])
removed_ip = ips.pop(0)
print(f"Удаленное значение {removed_ip}")
print(f"Оригинал: {ips}")
print(f"Отсортированный дубликат {sorted(ips)}")

first, second, *rest = sorted(ips)
print(first, second, rest)
