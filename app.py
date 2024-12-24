numbers = [19, 23, 4, 16, 28, 13, 31, 8, 29, 14, 6, 35, 2, 11, 17, 5, 9, 27, 12, 30]
primeArray = []

for n in numbers:
    count = 0
    for i in range(2,n):
        if n%i == 0:
            count += 1

    if count == 0:
        primeArray.append(n)

mini = min(primeArray)
maxi = max(primeArray)
sumArr = 0

for i in primeArray:
    sumArr += i 

print(mini)
print(maxi)
print(sumArr)