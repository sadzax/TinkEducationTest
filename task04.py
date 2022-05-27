error = 'Please enter only integers from 1 to 100'
while True:
    try:
        n = int(input())
        if n < 1 or n > 100:
            print(error)
            continue
        break
    except:
        print(error)
        continue
a = 'abcdefghijklmnopqrstuvwxyz'

def rowing_f(num):
    row = str()
    for i in range(int(num // 2 + num % 2)):
        if i >= 26:
            while i >= 26:
                i = i - 26
            row = row + a[i]
        else:
            row = row + a[i]
    return (row)
def rowing_b(num):
    row = str()
    for i in range(int(num // 2)):
        if i >= 26:
            while i >= 26:
                i = i - 26
            row = a[i] + row
        else:
            row = a[i] + row
    return (row)

def vertical(num, iter):
    print(rowing_b(2+iter*2)[:iter] + rowing_f(num-iter*2)+rowing_b(num-iter*2) + rowing_f(1+iter*2)[1:])

m = 0
while m <= int(n / 2):
    vertical(n, m)
    m = m + 1
m = m - 1
while m > 0:
    m = m - 1
    vertical(n, m)