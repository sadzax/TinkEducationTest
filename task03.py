error = 'Please enter only integers from 1 to 10^12'
while True:
    try:
        N = int(input())
        if N < 1 or N > 10**12:
            print(error)
            continue
        break
    except:
        print(error)
        continue
i = 0
for x in range(12):
    left = N % 10
    if left == 0:
        N = N / 10
        i = i + 1
    else:
        break
print (i)