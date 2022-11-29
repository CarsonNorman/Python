# for i in range(3):
#     print(i)

# for i in range(20, 10, -2):
#     print(i)

arr = [{"apple": "red"}, {"naranja": "orange"}, {"cherry": "dark red"}]

# for i in arr:
#     print(i.keys(), i.values())

for i in arr:
    for k, v in i.items():
        print(k, v)


