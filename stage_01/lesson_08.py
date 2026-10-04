# Задача 1 
print([x * x for x in range(5)])
# [0, 1, 4, 9, 16]
print([x for x in range (10) if x % 2 == 0])
# [0, 2, 4 , 6, 8]

nums = [3, -1, 4, -5]
print([x for x in nums if x > 0])
# 3, 4
print([x if x > 0 else 0 for x in nums ])
# 3, 0, 4, 0

words = ["admin", "root", "guest"]
print ({ word:len(word) for word in words })
#[admin: 5, root: 4 , guest: 5]
print({len(word) for word in words})
# {4,5}

# Задача 2 

matrix = [[1, 2], [3, 4],[5, 6]]
print([x for row in matrix for x in row ])
# 1, 2, 3, 4, 5, 6
print([[x * 10  for x in row ] for row in matrix])
# [10, 20], [30, 40], [50, 60], во втором случае у нас подпсписок и он разделяет каждые
# значения на отдельный подсписки,  а не выводит 1 единый списко 

# Задача 3
import sys

squares_list = [x * x for x in range (100_000)]
squares_gen = (x * x for x in range (100_000))

print(type(squares_list), type(squares_gen))
# list, generator
print(sys.getsizeof(squares_list),sys.getsizeof(squares_gen))
# хранит данные в оперативной памяти, ничего не хранит это генератор, он не считает ничего сразу
print(sum(x * x for x in range(100_000)))

# Задача 4

ip = ["10.0.0.5", "192.168.1.1", "10.0.0.7"]
print([x for x in ip if x.startswith("10.")])

word1 = ["admin", "root", "guest"]
print({word:len(word) for word in word1})


print([user.upper() for user in ["admin", "root"]])

logs =  [
    "2026-09-20 12:31:07 ERROR auth failed for user admin from 10.0.0.5",
    "2026-09-20 12:31:09 INFO user guest logged in from 10.0.0.7",
    "2026-09-20 12:31:15 ERROR auth failed for user admin from 10.0.0.5",
    "2026-09-20 12:32:01 WARN disk usage 91% on host srv1",
    "2026-09-20 12:33:40 ERROR auth failed for user root from 172.16.0.9",
]

suspicious_ip = {log.split()[-1] for log in logs if log.split()[2]=="ERROR"}
print(suspicious_ip)

