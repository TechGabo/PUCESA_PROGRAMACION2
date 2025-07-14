def nazi(n):
    if n <= 1:
        return n 
    return nazi(n - 1) + nazi(n - 2)

for i in range(11):  # De 0 a 10 (inclusive)
    print(nazi(i))
