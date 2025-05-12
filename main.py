
def fun():
    count = 0
    for i in range(101):
        if '9' in str(i):
            count += 1
    return count

res = fun()
print(res)