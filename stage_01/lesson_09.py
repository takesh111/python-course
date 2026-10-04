def greet(name, gereeting = "Привет" ):
    return f"{gereeting}, {name}"

print(greet("Алексей"))
# Привет, Алексей
print(greet("Алексей", "Здравствуйте" ))
# Здравствуйте Алексей
print(greet(gereeting="Хай", name="Алексей"))
# Хай, Алексей

def no_return(x):
    x*2
print(no_return(5))
# None

# Задача 2
def log_event(message, *tags, **details):
    print(message, tags, details)
log_event("вход")
# вход () {}
log_event ("вход", "auth", "ssh")
# Вход (auth, ssh) {}
log_event("вход", "auth", user ="admin", ip = "10.0.0.5" )
# вход, (auth),{user: admin, ip: 10.0.0.5}

# Задача 3

def add_bad(x, items = []):
    items.append(x)
    return items

def add_good(x, items = None):
    if items is None:
        items = []
    items.append(x)
    return items
print(add_bad(1), add_bad(2), add_bad(3))
# [1, 2, 3] , [1, 2, 3], [1, 2, 3]
print(add_good(1), add_good(2), add_good(3))
# 1, 2, 3

# Задача 4

def add_item(items):
    items.append("new")

def replace_items(items):
    items = ["new"]

data = ["a"]
add_item(data)
print(data)
# a, new
replace_items(data)
print(data)
# a,new

# Задача 5
logs=[
    "2026-09-20 12:31:07 ERROR auth failed for user admin from 10.0.0.5",
    "2026-09-20 12:31:09 INFO user guest logged in from 10.0.0.7",
    "2026-09-20 12:31:15 ERROR auth failed for user admin from 10.0.0.5",
    "2026-09-20 12:32:01 WARN disk usage 91% on host srv1",
    "2026-09-20 12:33:40 ERROR auth failed for user root from 172.16.0.9",
]
def parse_line(line):
    parts = line.split()
    date = parts [0]
    time = parts [1]
    level = parts [2]
    ip = parts [-1]
    return date, time, level, ip

print(parse_line(line = "2026-09-20 12:33:40 ERROR auth failed for user root from 172.16.0.9" ))

def count_levels(logs):
    counts = {}
    for line in logs:
        date, time, level, ip = parse_line(line)
        counts[level] = counts.get(level, 0) +1
    return counts

print(count_levels(logs))

def find_suspicious_ips(logs, level = "ERROR"):
    found = set()
    for line in logs:
        _,_, line_level, ip = parse_line(line)
        if line_level == level:
            found.add(ip)
    return found

print("Подозрительные ip:", sorted(find_suspicious_ips(logs)))