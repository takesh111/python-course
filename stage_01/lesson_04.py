# Задача 1
s = "cybersecurity"
print(len(s))
# 13
print(s[0], s[-1])
# c,y
print(s[0::5])
# csi ( берем каждый 5 символ от 0)
print(s[5::])
# security
print(s[::2])
#  c b r e u i y
print(s[::-1])
# ytirucesrebyc

# Задача 2 

log = "  2026-09-20 ERROR failed login from 10.0.0.5  "
clean = log.strip()
print(repr(log))
#   2026-09-20 ERROR failed login from 10.0.0.5  
print(repr(clean))
#2026-09-20 ERROR failed login from 10.0.0.5
parts = clean.split()
print(parts)
#[2026-09-20], [ERROR] , [failed], [login], [from], [10.0.0.5]
print(len(parts))
# 6
print(clean.replace("ERROR","WARN"))
print(clean) # Потому что строка это неизменяемая последовательность символов, оригинал не меняется.

# Задача 3
word = "Привет"
data = word.encode("utf-8")
print(len(word), len(data))
# 6 , 12
print(data.decode("utf-8"))
print("hello".encode("utf-8"))
#"Привет".encode("cp1251").decode("uft-8")
#File "<stdin>", line 1, in <module>
# "Привет".encode("cp1251").decode("utf-8")
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xcf in position 0: invalid continuation byte 
# декодировка произошла не в том формате, битый лог .

# Задача 4
line = "2026-09-20 12:31:07 ERROR auth failed for user admin from 10.0.0.5"
stroka = line.split()
date = stroka[0]
time = stroka[1]
level = stroka[2]
address = stroka[-1]
print(f"[{level}] {date} {time} - {address}")
result = " ".join(stroka)
print(result)