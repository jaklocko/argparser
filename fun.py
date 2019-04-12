import itertools as it

print("Count\n------")
for i in it.count(1,2):
    print(i)
    if i > 30:
        break

data = []
for x in range(1,101):
    data.append(x)

# print(data)
print("\nAccumulate\n------")

print(list(it.accumulate(data))[-1])