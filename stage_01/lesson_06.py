# Задача 1
server = {"host": "srv1", "port": 22}
print(server["host"])
# srv1
print(server.get("user"))
# None
print(server.get("user", "anonymous")) # anonymous - значение по умолчанию если нет user выводим его
# anonymous
print("port" in server, "user" in server)
# True, False
print(len(server))
# 2

server["user"] = "admin"
server["port"] = 2222
print(server)
# host: srv1 , port: 2222, user: admin
del server["port"]
print(server)
# host: srv1, user: admin
print(list(server.keys()), list(server.values())) # ключи, значения.
# host, user, srv1, admin
# KeyError: 'missing'h

# Задача 2
print(hash("admin"))
# невозможно предсказать 
print(hash((1, 2)))
# невозможно предсказать 
#TypeError: unhashable type: 'list, кортеж в котором не все элементы хешируемы.
# огромное количество времени будь он огромным.

# Задача 3

ips = ["10.0.0.5", "10.0.0.7", "10.0.0.5", "10.0.0.9", "10.0.0.7"]
unique = set(ips)
print(unique)
# "10.0.0.5", "10.0.0.7", "10.0.0.9" - уникальные элементы массива.
print(len(ips),len(unique))
# 5, 3

a = {1, 2, 3}
b = {3, 4}
print(a | b, a & b, a - b, a ^ b)
# {1, 2, 3 , 4}, {3} {1, 2}, {1, 2, 4}

# Задача 4 

yesterday = ["10.0.0.5", "10.0.0.7", "192.168.1.1"]
today = ["10.0.0.7", "192.168.1.1", "172.16.0.9", "10.0.0.5"]

unique_yesterday = set(yesterday)
unique_today = set(today)

print("Новые адреса:" , sorted(unique_today - unique_yesterday))
print("Пропавшие адреса: " , sorted(unique_yesterday - unique_today))
print("Общие адреса: ", sorted(unique_today & unique_yesterday))