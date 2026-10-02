# Задача 1
items=[]
if items:
    print("есть элементы")
else:
    print("список пуст")
#список пуст, так как питон не видит в нём никаких данных
x = 7
print(0 < x < 10)
# True
print(None or "default")
# default
print('admin' and 'root')
# root
print(not "")
# True
print(bool(0), bool("0"), bool([]), bool([0]))
# False, True, False, True 
# Потому что в питоне bool реагирует на 0 это False и на пустоту в списках массивах и т.д
# В нашем случае в строке, что-то есть и bool("0") - присваивает ему Истину, Что соотвественно и в массиве
# У нас есть определенное значение  bool([0]) - следовательно тоже Истина.

code = 404
print("ok" if code == 200 else "fail")
#fail

# Задача 2
for i in range(3):
    print(i)
#0,1,2
print(list(range(2, 10, 3)))
# 2 5 8
ips = ["10.0.0.5", "10.0.0.7"]
for number, ip in enumerate(ips, start=1):
    print(number, ip)
# 1:10.0.0.5, 2:10.0.0.7

users = ["admin", "guests"]
for user, ip in zip(users, ips):
    print(user, ip)
# admin 10.0.0.5 , ip 10.0.0.7

server = {"host":"srv1", "port": 22}
for key, value in server.items():
    print(key, "=", value)
#host = srv1, port = 22

# Задача 3 
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("нашли чётное", n)
        break
else:
    print("четных чисел нет ")
# четных чисел нет 
for n in [1, 2, 3, 4, 5, 6 ]:
    if n % 2:
        continue
    print("четное", n)

# четное -1, чётное - 3, чётное - 5 continue - когда у нас истина программа не доходит до строки print
# а когда число нечётное блок if пропускается и просто ошибочное печается это число

# Задача 4 
nums = [1, 2, 4, 5, 6]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)
# 1, 4, 5 из - за того, что мы прям в цикле убрали число 2, число четыре сдвинулось на его место 
#  и питон просто пропустил его не проверив.

# Задача 5 
logs = [
    "2026-09-20 12:31:07 ERROR auth failed for user admin from 10.0.0.5",
    "2026-09-20 12:31:09 INFO user guest logged in from 10.0.0.7",
    "2026-09-20 12:31:15 ERROR auth failed for user admin from 10.0.0.5",
    "2026-09-20 12:32:01 WARN disk usage 91% on host srv1",
    "2026-09-20 12:33:40 ERROR auth failed for user root from 172.16.0.9",
]

counts = {}
suspicious_ips = set()    

for line in logs:
    parts = line.split()
    level = parts[2]
    counts[level] = counts.get(level, 0) + 1

    if level == "ERROR":
        ip = parts[-1]
        suspicious_ips.add(ip)
    
print("Количество по уровням:", counts)
print("Подозрительные IP:", sorted(suspicious_ips))
print("всего подозрительных адресов:", len(suspicious_ips))
