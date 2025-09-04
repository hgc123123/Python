arr = []
while True:
    line=input()
    if line.strip() == "":
        break
    arr.append(list(map(int,line.split())))
print(arr)
for i in arr:
    print(i)
