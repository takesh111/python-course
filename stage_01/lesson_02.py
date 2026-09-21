# Задача 1
n = 10
print(id(n))
n += 1
print(id(n))
# Новый

s = "py"
print(id(s))
s += "thon"
print(id(s))
# Новый

nums = [1, 2]
print(id(nums))
nums += [3]
print(id(nums))
nums = nums + [4]
# Тот же, так как дописываем элемент
print(id(nums))
# Новый

# Задача 2
t = (1,[2, 3])
t[1].append(4)
print(t)
# 1,[2, 3, 4 ] 
# TypeError: 'tuple' object does not support item assignment  потому что нельзя изменить 
# неизменяемый объект Кортеж хранит ссылки на объекты, и запрещено только менять сами ссылки
# append сработал так как t[1] ссылается на список и список изменяемый

# Задача 3 
import copy

team = [["Аня", 25],["Боря", 30]]
shallow = team.copy()
deep = copy.deepcopy(team)

team[0][1] = 26 
team.append(["Вера", 22])
print(team)
# ["Аня", 26],["Боря", 30], ["Вера", 22]
print(shallow)
# ["Аня", 26],["Боря", 30]
print(deep)
# ["Аня", 25],["Боря", 30]

# Задача 4

default_settings = {"theme": "dark", "plugins": ["git", "python"]}
user_settings=copy.deepcopy(default_settings)
# user_settings=default_settings.copy()
user_settings["theme"] = "light"
user_settings["plugins"].append("docker")
print("Это обычный словарь", default_settings)
print("Это словарь c поверхностной копией", user_settings)
# Поверхностная копия создаёт новый внешний контейнер, но вложенные объекты 
# остаются общими с оригиналом. Поэтому изменение вложенного списка или словаря видно в обоих. 
# Глубокая копия рекурсивно копирует все уровни, и копия становится полностью независимой.
# Пример: словарь настроек со списком плагинов — после .copy() добавление плагина
# в копию попадёт и в оригинал.

# Мини задача
a = [[0], [0]]
b = a.copy()
b[0].append(1)
b.append([2])
print(a)
# [0, 1], [0]
print(b)
# [0, 1 ], [0], [2]

# Контрольная задача
x = [[1], [2]]
y = x.copy()
print(x is y, x[0] is y[0])
# False, True
y[1].append(3)
y[0] = [100]
print(x)
# [1,] [2, 3]
print(y)
# [100], [2, 3]
