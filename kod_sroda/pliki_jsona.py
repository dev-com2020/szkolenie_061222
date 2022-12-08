import json

with open("../dane.json", 'r') as f:
    data = json.load(f)

print(data)
print(data['members'])
print(data['members'][2])
print(data['members'][2]['powers'])
data['members'][2]['powers'][3] = 'Teleportacja'

slownik = '{"name": "Tomek", "lang": "Python", "number": [54, 324, 53, 1, 56, 2322]}'
person = json.loads(slownik)
print(json.dumps(person, indent=4))

lista = []
for i in data['members'][2]['powers']:
    lista.append(i)

print(lista)

with open("../dane2.json", 'w') as f:
    data = json.dump(data, f, indent=4)
