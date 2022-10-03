def online_count(dict):
    x = 0
    values = dict.values()
    for i in values:
        if i == "online":
            x += 1
    print(x)
status = { 
"Alice": "online", 
"Bob": "offline", 
"Eve": "online", 
}
online_count(status)
