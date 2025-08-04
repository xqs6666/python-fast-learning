for i in "hello":
    print(i)

for i in [1,2,3]:
    print(i)

for i,j in {"a1":100,"a2":200}.items():
    print(i,j)

for i in {1,2,3,4,4}:
    print(i)

for i in (1,2,3,4):
    print(i)


for i in range(4):
    print(i)

for i in range(2,11):
    print(i)

for i in range(2,16,5):
    print(i)

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}x{j}={i*j}\t")