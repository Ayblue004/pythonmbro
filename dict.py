keys = ["Ten", "Twenty", "Thirty"]
values = [10,20,30]

def join(key, value):
    zipped = dict(zip(key,value))
    print(zipped)

join(keys,values)


sampleDict = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])

sampleDict2 = {
    "name": "Kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
    }
poping = ["name","salary"]
for x in poping:
    sampleDict2.pop(x)
print(sampleDict2)

sampleDict3 = {
    "name": "Kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
    }
sampleDict3["location"] = sampleDict3["city"]

print(sampleDict3)
